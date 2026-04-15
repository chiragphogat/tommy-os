
# voice_engine.py
import os
import time
import webbrowser
import pyautogui
import requests
import uiautomation as auto
import screen_brightness_control as sbc
import pvporcupine
import speech_recognition as sr
from dotenv import load_dotenv
from pvrecorder import PvRecorder
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import sys
import ctypes
sys.coinit_flags = 0 # Force COINIT_MULTITHREADED globally to prevent WinError -2147417850 in background Dictation loop
import threading
import subprocess

import spacy
import json

import tkinter as tk

# --- 🔴🟢🟡 TKINTER OVERLAY ---
class VoiceOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.geometry("120x40+20+20")
        self.root.configure(bg='black')

        self.canvas = tk.Canvas(self.root, width=120, height=40, bg='black', highlightthickness=0)
        self.canvas.pack()

        self.dot_r = self.canvas.create_oval(5, 5, 15, 15, fill='darkred', outline='darkred')
        self.dot_y = self.canvas.create_oval(25, 5, 35, 15, fill='darkgoldenrod', outline='darkgoldenrod')
        self.dot_g = self.canvas.create_oval(45, 5, 55, 15, fill='darkgreen', outline='darkgreen')

    def set_color(self, color="red"):
        self.root.after(0, self._update_color, color)

    def _update_color(self, color):
        self.canvas.itemconfig(self.dot_r, fill='darkred')
        self.canvas.itemconfig(self.dot_y, fill='darkgoldenrod')
        self.canvas.itemconfig(self.dot_g, fill='darkgreen')

        if color == "red":
            self.canvas.itemconfig(self.dot_r, fill='red')
        elif color == "yellow":
            self.canvas.itemconfig(self.dot_y, fill='yellow')
        elif color == "green":
            self.canvas.itemconfig(self.dot_g, fill='lime')
        
        self.root.update()

voice_ui = None

# --- 🛰️ INITIALIZATION ---
load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", ".env"))
ACCESS_KEY = os.getenv("PORCUPINE_ACCESS_KEY")
WAKE_WORD_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "assets", "hey_tommy.ppn")

# --- 🧠 LONG-TERM RAG & STATE MEMORY ---
import json
MEMORY_FILE = os.path.join(os.path.expanduser("~"), ".tommy_memory.json")
STATE_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", ".tommy_state.json")

CURRENT_VOICE_MODE = "normal"
state_lock = threading.Lock()

def store_memory(key, value):
    try:
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, 'r') as f: mem = json.load(f)
        else: mem = {}
        mem[key.lower()] = value
        with open(MEMORY_FILE, 'w') as f: json.dump(mem, f)
        return True
    except: return False

def recall_memory(key):
    try:
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, 'r') as f: mem = json.load(f)
            return mem.get(key.lower(), None)
        return None
    except: return None

# --- 🗣️ VOICE ENGINE (Swara) ---
def speak(text):
    """Speaks text using Edge-TTS Swara (Hindi Female) SYNCHRONOUSLY to prevent Microphone overlap."""
    if not text: return
    try:
        import tempfile, uuid
        # Clean string for command line
        escaped_text = text.replace('"', '').replace("'", "")
        file_id = uuid.uuid4().hex
        filepath = os.path.join(tempfile.gettempdir(), f"response_{file_id}.mp3")
        alias = f"audio_{file_id}"
        
        # Use python's sys.executable to cleanly bypass PATH issues in sub-shells
        cmd = f'"{sys.executable}" -m edge_tts --voice hi-IN-SwaraNeural --text "{escaped_text}" --write-media "{filepath}"'
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        
        # Lock the Thread until the Cloud responds and downloads the audio
        res = subprocess.run(cmd, shell=True, startupinfo=startupinfo, creationflags=subprocess.CREATE_NO_WINDOW)
        
        if not os.path.exists(filepath):
            print("❌ TTS Generation Failed: edge-tts did not render the .mp3")
            return
            
        # PHASE 14: CRITICAL AUDIO BYPASS
        # Forcibly UNMUTE the master volume matrix immediately before Microsoft TTS playback natively.
        set_system_mute(False)
        
        # Play MP3 invisibly using Windows MCI synchronously ('wait' completely blocks execution)
        ctypes.windll.winmm.mciSendStringW(rf"close {alias}", None, 0, None)
        ctypes.windll.winmm.mciSendStringW(rf'open "{filepath}" type mpegvideo alias {alias}', None, 0, None)
        ctypes.windll.winmm.mciSendStringW(rf"play {alias} wait", None, 0, None)
        ctypes.windll.winmm.mciSendStringW(rf"close {alias}", None, 0, None)
        
        try: os.remove(filepath)
        except: pass
    except Exception as e:
        print(f"TTS Error: {e}")

# --- 🖱️ GOD-LEVEL UI AUTOMATION ---
def find_and_click(name):
    """Smartly finds and clicks an element containing 'name' in the active window."""
    try:
        # Quick search in foreground window tree
        fg = auto.GetForegroundControl()
        if fg:
            # Traverse a bit into the tree looking for the name
            for c, d in auto.WalkTree(fg, maxDepth=4):
                if c.Name and name.lower() in c.Name.lower():
                    # Focus on interactive elements
                    if c.ControlType in [auto.ControlType.ButtonControl, auto.ControlType.MenuItemControl, 
                                         auto.ControlType.TabItemControl, auto.ControlType.ListItemControl, 
                                         auto.ControlType.HyperlinkControl, auto.ControlType.DocumentControl]:
                        c.Click()
                        return f"Clicked {c.Name}"
    except Exception:
        pass # Fallback to OCR if UIA crashes
        
    # --- OCR FALLBACK (Phase 4) ---
    try:
        import numpy as np
        import cv2
        reader = get_ocr()
        screenshot = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        read_results = reader.readtext(img)
        
        for (bbox, text, prob) in read_results:
            if name.lower() in text.lower():
                center_x = int((bbox[0][0] + bbox[2][0]) / 2)
                center_y = int((bbox[0][1] + bbox[2][1]) / 2)
                pyautogui.click(center_x, center_y)
                return f"OCR Clicked '{text}'"
    except Exception as e:
        print(f"OCR Error: {e}")
        
    return f"UI Interaction Failed completely for {name}"

# --- 🧠 DETERMINISTIC NLP ENGINE ---
try:
    nlp = spacy.load("en_core_web_sm")
except BaseException:
    nlp = None

# --- 🔊 HARDWARE KERNEL (+-15 UNITS) ---
def adjust_volume(direction):
    try:
        import comtypes
        comtypes.CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        volume = devices.EndpointVolume
        current = volume.GetMasterVolumeLevelScalar()
        change = 0.15 if direction == "up" else -0.15
        volume.SetMasterVolumeLevelScalar(max(0.0, min(1.0, current + change)), None)
        return f"Volume {direction}"
    except: return "Audio Error"

def adjust_brightness(direction):
    try:
        change = 15 if direction == "up" else -15
        current = sbc.get_brightness()[0]
        sbc.set_brightness(max(0, min(100, current + change)))
        return f"Brightness {direction}"
    except: return "Display Error"

# --- 🧠 RECURSIVE TASK PLANNER & KERNEL EXECUTION ---
import re
import threading
ui_lock = threading.Lock()
def execute_logic_chain(full_command):
    # Sophisticated pipeline for multi-step tasks
    # Only split on " and " or " then " if they are command boundaries, 
    # but to be safe with dictation, we will just use a simpler split:
    # If the user says "open notepad and type X", we want to split right before "type " or "write "
    cmd_str = full_command.lower()
    cmd_str = re.sub(r'\s+and\s+type\s+', ' | type ', cmd_str)
    cmd_str = re.sub(r'\s+and\s+write\s+', ' | write ', cmd_str)
    cmd_str = re.sub(r'\s+then\s+type\s+', ' | type ', cmd_str)
    cmd_str = re.sub(r'\s+then\s+write\s+', ' | write ', cmd_str)
    
    tasks = cmd_str.split("|")
    results = []
    
    for task in tasks:
        cmd = task.strip()
        if not cmd: continue
        print(f"   ↳ [PROCESSING]: {cmd}")
        
        global CURRENT_VOICE_MODE
        
        # --- PHASE 15: DYNAMIC WAKE WORDS ---
        if cmd.startswith("change model name to "):
            new_name = cmd.replace("change model name to ", "").strip()
            if new_name:
                store_memory("dynamic_wake_word", new_name)
                results.append(f"Model Name changed to {new_name}")
                speak(f"Configured. I will now respond to the wake word {new_name}.")
            continue
            
        # --- PHASE 10: CONTEXTUAL VOICE MODES & VISION TOGGLES ---
        if cmd in ["activate study mode", "study mode", "switch to study mode"]:
            with state_lock: CURRENT_VOICE_MODE = "study"
            speak("Study mode active. I will bypass wake-words and listen for document commands natively.")
            results.append("Study Mode On")
            continue
        elif cmd in ["activate movie mode", "movie mode", "switch to movie mode"]:
            with state_lock: CURRENT_VOICE_MODE = "movie"
            speak("Movie mode active. I will bypass wake-words and listen for media controls natively.")
            results.append("Movie Mode On")
            continue

        elif any(w in cmd for w in ["normal mode", "deactivate study mode", "deactivate movie mode", "exit mode", "quit mode"]):
            with state_lock: CURRENT_VOICE_MODE = "normal"
            speak("Normal mode active. I require the wake word 'Hey Tommy' to listen.")
            results.append("Normal Mode On")
            continue
            
        elif cmd in ["switch to eye control", "eye control", "use eye tracking", "enable eye control"]:
            try:
                with state_lock:
                    if os.path.exists(STATE_FILE):
                        with open(STATE_FILE, "r") as f: data = json.load(f)
                    else: data = {}
                    data["vision_mode"] = "eye"
                    with open(STATE_FILE, "w") as f: json.dump(data, f)
                speak("Optical eye tracking enabled.")
                results.append("Eye Control On")
            except: pass
            continue
        elif cmd in ["switch to hand control", "hand control", "use hand tracking", "enable hand control"]:
            try:
                with state_lock:
                    if os.path.exists(STATE_FILE):
                        with open(STATE_FILE, "r") as f: data = json.load(f)
                    else: data = {}
                    data["vision_mode"] = "hand"
                    with open(STATE_FILE, "w") as f: json.dump(data, f)
                speak("Spatial hand tracking enabled.")
                results.append("Hand Control On")
            except: pass
            continue
            


        # --- MEDIA CONTROLS (Movie Mode Enhancements) ---
        if any(w in cmd for w in ["play video", "pause video", "play song", "pause song"]) or cmd in ["play", "pause"]:
            pyautogui.press('playpause')
            results.append("Toggled Media")
            continue
        elif cmd in ["next", "next track", "next video", "skip"]:
            pyautogui.press('nexttrack')
            results.append("Next Track")
            continue
        elif cmd in ["last", "last track", "previous", "previous track", "back"]:
            pyautogui.press('prevtrack')
            results.append("Previous Track")
            continue



        # --- 🧠 PERSISTENT MEMORY ---
        elif cmd.startswith("remember that "):
            fact = cmd.replace("remember that ", "").strip()
            if " is " in fact:
                k, v = fact.split(" is ", 1)
                store_memory(k.strip(), v.strip())
                results.append(f"Memorized {k}")
                speak(f"I will remember that your {k} is {v}.")
            else:
                store_memory(fact, fact)
                results.append("Memory saved")
                speak("I have committed that to memory.")
            continue
                
        elif cmd.startswith("what is my ") or cmd.startswith("what was my "):
            k = cmd.replace("what is my ", "my ").replace("what was my ", "my ").strip()
            val = recall_memory(k)
            if val:
                speak(f"Your {k.replace('my ','')} is {val}.")
                results.append(f"Recalled {val}")
            else:
                speak("I do not have that stored in my memory banks.")
                results.append("Memory not found")
            continue



        # --- THREAD-SAFE UI & HARDWARE AUTOMATION ---
        with ui_lock:
            # 1. HARDWARE QUICK-TRIGGERS
            if any(w in cmd.split() for w in ["bright", "roshni"]): results.append(adjust_brightness("up"))
            elif any(w in cmd.split() for w in ["dark", "andhera"]): results.append(adjust_brightness("down"))
            elif "volume up" in cmd or "awaz badhao" in cmd:
                pyautogui.press('volumeup', presses=7)
                results.append("Volume Up")
            elif "volume down" in cmd or "awaz kam" in cmd:
                pyautogui.press('volumedown', presses=7)
                results.append("Volume Down")
            
            # 1.5 SYSTEM & HARDWARE CHECKS
            elif cmd.startswith("check") or "system status" in cmd or 'battery' in cmd or 'cpu' in cmd or 'ram' in cmd or 'memory' in cmd:
                import psutil
                if "cpu" in cmd:
                    results.append(f"CPU at {psutil.cpu_percent(interval=0.5)} percent")
                elif "ram" in cmd or "memory" in cmd:
                    mem = psutil.virtual_memory()
                    free_gb = round(mem.available / (1024**3), 1)
                    total_gb = round(mem.total / (1024**3), 1)
                    results.append(f"RAM {free_gb} gigabytes free")
                elif "battery" in cmd or "power" in cmd:
                    battery = psutil.sensors_battery()
                    if battery:
                        plugged = "plugged in" if battery.power_plugged else "on battery"
                        results.append(f"Battery at {battery.percent} percent, {plugged}")
                    else: 
                        results.append("No battery detected.")
                else:
                    results.append(f"CPU {psutil.cpu_percent(interval=0.2)} percent. RAM {psutil.virtual_memory().percent} percent")

            # 1.8 FILE SYSTEM MANAGEMENT
            elif cmd.startswith("create folder") or cmd.startswith("make folder"):
                folder_name = cmd.replace("create folder", "").replace("make folder", "").strip()
                target_dir = os.path.join(os.path.expanduser("~"), "Desktop")
                
                if " on desktop" in folder_name:
                    folder_name = folder_name.replace(" on desktop", "").strip()
                elif " in documents" in folder_name:
                    folder_name = folder_name.replace(" in documents", "").strip()
                    target_dir = os.path.join(os.path.expanduser("~"), "Documents")
                    
                if not folder_name: folder_name = "New Folder"
                try:
                    os.makedirs(os.path.join(target_dir, folder_name), exist_ok=True)
                    results.append(f"Created folder {folder_name}")
                except Exception as e:
                    results.append(f"Folder Error")
                    
            # 2. WINDOW & SYSTEM CONTROL
            elif cmd.startswith("close") or "band karo" in cmd:
                app_target = cmd.replace("close", "").replace("band karo", "").strip()
                if not app_target:
                    pyautogui.hotkey('alt', 'f4')
                    results.append("Closed active window")
                elif "settings" in app_target:
                    os.system("taskkill /f /im SystemSettings.exe")
                    results.append("Closed Settings")
                elif "task manager" in app_target:
                    os.system("taskkill /f /im taskmgr.exe")
                    results.append("Closed Task Manager")
                else:
                    import psutil
                    killed = False
                    for proc in psutil.process_iter(['name']):
                        if proc.info['name'] and app_target.lower() in proc.info['name'].lower():
                            try: proc.kill(); killed = True
                            except: pass
                    if killed: results.append(f"Force Closed {app_target}")
                    else: 
                        pyautogui.hotkey('alt', 'f4')
                        results.append(f"Attempted to close {app_target}")
            elif cmd.startswith("minimize") or "window minimize" in cmd:
                pyautogui.hotkey('alt', 'space')
                time.sleep(0.1)
                pyautogui.press('n')
                results.append("Minimized Window")
            elif cmd in ["maximize", "window maximize"]:
                pyautogui.hotkey('alt', 'space')
                time.sleep(0.1)
                pyautogui.press('x')
                results.append("Maximized Window")
            elif cmd in ["switch window", "change window"]:
                pyautogui.hotkey('alt', 'tab')
                time.sleep(0.5)
                results.append("Switched Window")
            elif cmd in ["take screenshot", "screenshot"]:
                pyautogui.hotkey('win', 'printscreen')
                results.append("Took Screenshot")
            elif cmd in ["lock screen", "lock computer", "lock pc"]:
                os.system("rundll32.exe user32.dll,LockWorkStation")
                results.append("Locked Screen")
            elif cmd in ["open settings"]:
                os.system("start ms-settings:")
                results.append("Opened Settings")
            elif cmd in ["open task manager", "task manager"]:
                pyautogui.hotkey('ctrl', 'shift', 'esc')
                results.append("Opened Task Manager")
            elif cmd in ["open terminal", "terminal"]:
                os.system("start wt")
                results.append("Opened Terminal")
            elif cmd in ["shutdown system", "turn off computer"]:
                os.system("shutdown /s /t 1")
                results.append("Shutting Down")
            elif cmd in ["restart system"]:
                os.system("shutdown /r /t 1")
                results.append("Restarting")
                
            # 3. MOUSE & UI INTERACTION
            elif cmd.startswith("click"):
                target = cmd.replace("click", "").strip()
                if target in ["", "here", "it", "mouse"]:
                    pyautogui.click()
                    results.append("Clicked Mouse")
                else:
                    res = find_and_click(target)
                    results.append(res)
            elif "right click" in cmd:
                pyautogui.rightClick()
                results.append("Right Clicked")
            elif "double click" in cmd:
                pyautogui.doubleClick()
                results.append("Double Clicked")
            elif "scroll down" in cmd:
                pyautogui.scroll(-500)
                results.append("Scrolled Down")
            elif "scroll up" in cmd:
                pyautogui.scroll(500)
                results.append("Scrolled Up")
    
            # 4. KEYBOARD SHORTCUTS
            elif cmd in ["copy", "copy that", "copy it"]:
                pyautogui.hotkey('ctrl', 'c')
                results.append("Copied")
            elif cmd in ["paste", "paste here", "paste it"]:
                pyautogui.hotkey('ctrl', 'v')
                results.append("Pasted")
            elif cmd in ["undo"]:
                pyautogui.hotkey('ctrl', 'z')
                results.append("Undid")
            elif cmd in ["redo"]:
                pyautogui.hotkey('ctrl', 'y')
                results.append("Redid")
            elif "select all" in cmd:
                pyautogui.hotkey('ctrl', 'a')
                results.append("Selected All")
            elif "press enter" in cmd or cmd == "enter":
                pyautogui.press('enter')
                results.append("Pressed Enter")
            elif "press space" in cmd or cmd == "space":
                pyautogui.press('space')
                results.append("Pressed Space")
            elif "press backspace" in cmd or cmd == "backspace" or "delete that" in cmd:
                pyautogui.press('backspace')
                results.append("Pressed Backspace")
            elif "press tab" in cmd or cmd == "tab":
                pyautogui.press('tab')
                results.append("Pressed Tab")
            elif "press escape" in cmd or cmd == "escape":
                pyautogui.press('escape')
                results.append("Pressed Escape")
    
            # 5. SMART OPENING & FOCUS (Universal App & Web Launcher)
            elif cmd.startswith("open"):
                raw_target = cmd.replace("open", "", 1).strip()
                
                # --- WEB ROUTER ---
                web_target = None
                clean_target = raw_target.replace(" in chrome", "").replace(" in edge", "").replace(" in browser", "").strip()
                
                if "youtube" in clean_target:
                    web_target = "youtube.com"
                elif "google" in clean_target:
                    web_target = "google.com"
                elif "chatgpt" in clean_target or "gpt" in clean_target:
                    web_target = "chatgpt.com"
                elif "." in clean_target and " " not in clean_target:
                    # e.g. "open github.com"
                    web_target = clean_target
                elif "." in clean_target and any(ext in clean_target for ext in [".com", ".org", ".net", ".in", ".xyz", ".co"]):
                    # Extracts URL e.g. "open abc.xyz please" -> "abc.xyz"
                    for word in clean_target.split():
                        if "." in word: web_target = word; break
                
                if web_target:
                    if not web_target.startswith("http"): web_target = "https://" + web_target
                    import webbrowser
                    webbrowser.open(web_target)
                    results.append(f"Opened Webpage {web_target}")
                else:
                    # --- DEEP OS KERNEL LAUNCHER (Phase 5) ---
                    import subprocess
                    try:
                        # Pure OS-level shell execution (instant and invisible background dispatch)
                        # 'start' perfectly handles registered .exe names and UWP App Aliases natively
                        res = subprocess.run(f"start {raw_target}", shell=True, capture_output=True, text=True)
                        if res.returncode == 0 and not "cannot find the file" in res.stderr.lower():
                            results.append(f"System Launched {raw_target}")
                            continue # Skip the UI macro entirely!
                    except Exception:
                        pass
                        
                    # --- FALLBACK UI MACRO LAUNCHER ---
                    pyautogui.press('win')
                    time.sleep(0.5)
                    pyautogui.write(raw_target, interval=0.03)
                    time.sleep(1.0)
                    pyautogui.press('enter')
                    results.append(f"GUI Launched {raw_target}")
    
            # 6. TYPE (Dictation)
            elif cmd.startswith("type"):
                # "type my name is chirag" -> query: "my name is chirag"
                # Since we fixed the string split above, the word "and" stays here!
                text = cmd.replace("type", "", 1).strip()
                pyautogui.write(text, interval=0.01)
                results.append("Text Typed")
            else:
                # Fallback NLP using spaCy
                if nlp:
                    doc = nlp(cmd)
                    # Basic intent extraction
                    verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
                    nouns = [token.lemma_ for token in doc if token.pos_ == "NOUN"]
                    results.append(f"Parsed Intent: Actions {verbs} on Targets {nouns}")
                else:
                    results.append("Command unhandled by strict logic")

    final_response = " and ".join(results)
    
    # LOGGING AND CONFIRMATION
    if final_response:
        if CURRENT_VOICE_MODE == "normal_ambient":
            clean_speech = final_response.replace("|", " and ")
                
            if len(clean_speech) > 250:
                speak("I have executed the long command.")
            else:
                clean_speech = f"I have executed: {clean_speech}"
                speak(clean_speech)
            
        print(f"✅ [RESPONSE]: {final_response}\n")
    else:
        print("✅ [RESPONSE]: Empty/Unknown Command\n")
        
    return final_response

# --- 🔇 STATEFUL MUTE/UNMUTE (replaces fragile volumemute toggle) ---
import comtypes
def _get_system_volume():
    """Returns the pycaw IAudioEndpointVolume interface for system audio."""
    comtypes.CoInitialize()
    devices = AudioUtilities.GetSpeakers()
    return devices.EndpointVolume

def set_system_mute(mute: bool):
    """Deterministically mute (True) or unmute (False) system audio via pycaw."""
    try:
        vol = _get_system_volume()
        vol.SetMute(int(mute), None)
    except Exception as e:
        print(f"   ⚠ Mute control error: {e}")

# --- 🎤 THE OMNI-EAR (SENSITIVE MODE) ---
def run_tommy(queue=None):
    global CURRENT_VOICE_MODE
    try:
        porcupine = pvporcupine.create(access_key=ACCESS_KEY, keyword_paths=[WAKE_WORD_PATH], sensitivities=[0.99])
        recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    except Exception as e:
        print(f"\n[🚫 PICOVOICE ERROR] Wake-word initialization failed: {e}")
        print("[ℹ️] Switching to NORMAL AMBIENT MODE (continuous listening) as fallback.")
        with state_lock:
            CURRENT_VOICE_MODE = "normal_ambient"
        porcupine = None
        recorder = None

    r = sr.Recognizer()

    # ── Listening Calibration (Phase 1 Fix) ──────────────────────
    # DISABLE dynamic threshold — it drifts upward in noisy rooms,
    # making Tommy "deaf" over time.
    r.dynamic_energy_threshold = False

    # Set a sensible baseline; adjust_for_ambient_noise will overwrite
    # this with a measured value, but we need a floor so the recognizer
    # is never *too* sensitive (picking up fan hum) or *too* deaf.
    ENERGY_FLOOR = 100          # Absolute whisper-level minimum 
    ENERGY_CEILING = 400        # Hyper-aggressive ceiling constraint (Prevents fan noise from turning Tommy deaf)
    r.energy_threshold = 100    # Reasonable default for a typical room

    # Professional commercial-grade AI pause margins (ChatGPT/Siri)
    # Allows the user 1.6 seconds of absolute silence (breathing time) before cutting them off.
    r.pause_threshold = 1.6
    r.non_speaking_duration = 0.8

    print("\n" + "="*50 + "\n 🏛️  T.O.M.M.Y: OS ARCHITECT KERNEL V2026\n" + "="*50)

    # ── Initial ambient calibration at startup (environment is quiet) ──
    print("[CALIBRATING] Measuring ambient noise — please stay quiet...")
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1.5)
            # Clamp to floor/ceiling
            r.energy_threshold = max(ENERGY_FLOOR, min(ENERGY_CEILING, r.energy_threshold))
        print(f"[CALIBRATED] energy_threshold = {r.energy_threshold:.0f}")
    except Exception as e:
        print(f"[CALIBRATION SKIPPED] {e}  — using default {r.energy_threshold}")

    speak("Tommy systems online. I am ready, Architect.")
    if recorder:
        recorder.start()

    try:
        active_attention = False
        while True:
            with state_lock:
                current_mode = CURRENT_VOICE_MODE
                
            if current_mode == "normal":
                if porcupine is None or recorder is None:
                    print("\r[WAKE-WORD ERROR] API key limit. Forcing Ambient Normal mode.", end="", flush=True)
                    with state_lock:
                        CURRENT_VOICE_MODE = "normal_ambient"
                    time.sleep(1)
                    continue

                # Ensure the background recorder is actually running!
                if not recorder.is_recording:
                    recorder.start()
                    
                if voice_ui: voice_ui.set_color("yellow")
                print("\r[WAITING] Listening for 'Hey Tommy'...", end="", flush=True)
                if porcupine.process(recorder.read()) >= 0:
                    print("\n\n[★ WAKE WORD DETECTED]")

                    # Deterministically mute system audio so calibration
                    # doesn't hear Tommy's own speakers.
                    set_system_mute(True)

                    print("   [MIC OS DRIVER YIELDED] Freeing PvRecorder...")
                    recorder.stop() # Massively critical: Drop the port so SpeechRecognition can take it!
                    
                    try:
                        with sr.Microphone() as source:
                            # 1. Re-calibrate for current ambient conditions
                            r.adjust_for_ambient_noise(source, duration=0.75)
                            r.energy_threshold = max(ENERGY_FLOOR, min(ENERGY_CEILING, r.energy_threshold))
                            print(f"   [re-calibrated] energy = {r.energy_threshold:.0f}")

                            # 2. Unmute so the user hears the "Yes?" acknowledgment
                            set_system_mute(False)
                            speak("Yes?")

                            # 3. Brief mute while listening to avoid picking up TTS tail
                            time.sleep(0.25)          # let "Yes?" finish playing
                            set_system_mute(True)

                            print("[LISTENING] Speak now...")
                            if voice_ui: voice_ui.set_color("green")
                            
                            while True:
                                try:
                                    # timeout=None guarantees Tommy waits INFINITELY for the user to speak
                                    audio = r.listen(source, timeout=None, phrase_time_limit=30)
                                    
                                    # Unmute immediately after capturing vocals
                                    set_system_mute(False)
                                    res_str = r.recognize_vosk(audio)
                                    try:
                                        command = json.loads(res_str).get("text", "")
                                    except BaseException:
                                        command = ""
                                    
                                    # If the user accidentally says "Hey Tommy" again while the box is green, 
                                    # we ignore the duplicate and keep the mic explicitly open!
                                    if command.lower() in ["hey tommy", "tommy", "hey johnny", "hey dummy"]:
                                        set_system_mute(True)
                                        continue
                                        
                                    print(f"   ↳ [HEARD (Normal)]: \"{command}\"")
                                    if voice_ui: voice_ui.set_color("yellow")
                                    
                                    # ── Background Execution ────────────────
                                    threading.Thread(target=execute_logic_chain, args=(command,), daemon=True).start()
                                    break # Exits the infinite listening loop and returns to Yellow Wake-Word hunting

                                except sr.WaitTimeoutError:
                                    continue # Ignore all timeouts natively
                                except sr.UnknownValueError:
                                    # User coughed or mumbled nonsense. Keep the box GREEN and keep waiting!
                                    set_system_mute(True)
                                    continue 
                                except Exception as e:
                                    set_system_mute(False)
                                    print(f"❌ [ERROR]: Unhandled Exception {e}.\n")
                                    if voice_ui: voice_ui.set_color("red")
                                    break
                    finally:
                        print("   [MIC OS DRIVER ACQUIRED] Restarting PvRecorder...")
                        if recorder: recorder.start()
                                
            # Phase 10 & 12: Free-Voice Native Modes
            elif current_mode in ["study", "movie", "normal_ambient"]:
                if voice_ui: voice_ui.set_color("green")
                
                # Absolutely kill the PvRecorder so it doesn't fight the OS lock
                if recorder and recorder.is_recording:
                    recorder.stop()
                
                try:
                    with sr.Microphone() as source:
                        print(f"\r[FREE VOICE] Active Mode: [{current_mode.upper()}]  <-- Ambient Array Listening...", end="", flush=True)
                        try:
                            audio = r.listen(source, timeout=None, phrase_time_limit=15)
                            res_str = r.recognize_vosk(audio)
                            try:
                                command = json.loads(res_str).get("text", "").lower()
                            except BaseException:
                                command = ""
                            print(f"\n   ↳ [AMBIENT CAUGHT]: \"{command}\"")
                            
                            # Process contextual commands without Wake Word
                            valid_command = None
                            
                            # --- Dynamic Wake Word Extraction ---
                            dyn_name = recall_memory("dynamic_wake_word")
                            wake_words = ["hey tommy", "tommy", "hey johnny", "hey dummy"]
                            if dyn_name:
                                wake_words.append(dyn_name.lower())
                                wake_words.append("hey " + dyn_name.lower())
                                
                            has_wake_word = False
                            extracted_cmd = command
                            for w in wake_words:
                                if command.startswith(w):
                                    has_wake_word = True
                                    extracted_cmd = command[len(w):].strip()
                                    break
                                    
                            if "normal mode" in command or "exit mode" in command:
                                valid_command = "switch to normal mode"
                            elif current_mode == "normal_ambient":
                                # User requested removing Wake-Word constraints altogether.
                                # Execute unconditionally. Strip the wake word ONLY if it is coincidentally present!
                                valid_command = extracted_cmd if has_wake_word else command

                            elif current_mode == "study":
                                if any(w in command for w in ["scroll down", "scroll up", "bright", "dark", "volume"]):
                                    valid_command = command
                            elif current_mode == "movie":
                                if any(w in command for w in ["play", "pause", "next", "last", "skip", "back"]):
                                    valid_command = command
                                    
                            if valid_command:
                                if voice_ui: voice_ui.set_color("yellow")
                                threading.Thread(target=execute_logic_chain, args=(valid_command,), daemon=True).start()
                                time.sleep(1.0) # Graceful thread dispatch wait
                                
                        except sr.WaitTimeoutError:
                            pass
                        except sr.UnknownValueError:
                            pass
                        except Exception as e:
                            print(f"❌ Ambient Error: {e}")
                except Exception as stream_err:
                    print(f"❌ Core Audio Stream Error: {stream_err}")
                    time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        set_system_mute(False)   # always leave audio unmuted on exit
        if recorder:
            try: recorder.stop()
            except: pass
            try: recorder.delete()
            except: pass
        if porcupine:
            try: porcupine.delete()
            except: pass

if __name__ == "__main__":
    # Force Python Dictation seamlessly into the background!
    threading.Thread(target=run_tommy, daemon=True).start()
    
    # Hand the entire Main Thread directly to Tkinter native loop!
    voice_ui = VoiceOverlay()
    try:
        voice_ui.root.mainloop()
    except KeyboardInterrupt:
        pass