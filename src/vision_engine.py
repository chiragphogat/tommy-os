#vision_engine.py
import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
import os
import json
from math import hypot
from datetime import datetime
import threading
import screen_brightness_control as sbc

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0 # DELETES PYAUTOGUI's NATIVE 100ms THREAD-BLOCKING SLEEP (Core fix for "Lag")

# --- LOAD MEDIAPIPE SOLUTIONS ONCE ---
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# --- ⚙️ EYE TRACKING CONFIG ---
EAR_THRESHOLD = 0.18         
WINK_THRESHOLD = 0.22        
MOUTH_AR_THRESHOLD = 0.45    
DOUBLE_BLINK_TIME = 0.4      
WINK_HOLD_TIME = 0.15        
GESTURE_COOLDOWN = 0.4       
SCROLL_COOLDOWN = 0.1        
SMOOTHENING = 7              
SCROLL_AMOUNT = 120

LEFT_BOUND = 0.35
RIGHT_BOUND = 0.65
TOP_BOUND = 0.30
BOTTOM_BOUND = 0.70

# --- OS STATE & IPC LOOP ---
STATE_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", ".tommy_state.json")

def read_vision_mode():
    try:
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, 'r') as f:
                return json.load(f).get("vision_mode", "hand")
    except: pass
    return "hand" # Default Fallback

# --- EYE MATH UTILS ---
def calculate_ear(eye_landmarks, frame_w: int, frame_h: int) -> float:
    p1, p2, p3, p4, p5, p6 = eye_landmarks
    def dist(p_a, p_b): return hypot((p_a.x - p_b.x) * frame_w, (p_a.y - p_b.y) * frame_h)
    v1, v2, h = dist(p2, p6), dist(p3, p5), dist(p1, p4)
    if h == 0.0: return 0.0
    return (v1 + v2) / (2.0 * h)

def calculate_mar(mouth_landmarks, frame_w: int, frame_h: int) -> float:
    p_left, p_top, p_right, p_bottom = mouth_landmarks
    def dist(p_a, p_b): return hypot((p_a.x - p_b.x) * frame_w, (p_a.y - p_b.y) * frame_h)
    v, h = dist(p_top, p_bottom), dist(p_left, p_right)
    if h == 0.0: return 0.0
    return v / h

def show_mode_popup(mode_name, title="T.O.M.M.Y. VISUAL OS"):
    def popup():
        import tkinter as tk
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes('-topmost', True)
        root.attributes('-disabled', True)
        root.attributes('-alpha', 0.85)
        sw = root.winfo_screenwidth()
        root.geometry(f"600x80+{int(sw/2)-300}+50")
        root.configure(bg='#1e1e1e')
        label = tk.Label(root, text=f"{title}: {mode_name.upper()}", font=("Segoe UI", 24, "bold"), fg="#00ffcc", bg="#1e1e1e")
        label.pack(expand=True, fill='both')
        root.after(2000, root.destroy)
        root.mainloop()
    threading.Thread(target=popup, daemon=True).start()

def run_vision_engine():
    screen_w, screen_h = pyautogui.size()
    cap = cv2.VideoCapture(0)
    cam_w, cam_h = 1280, 720
    cap.set(3, cam_w)
    cap.set(4, cam_h)
    
    # --- PHYSICAL WORLD SNAPSHOT TIMER ---
    last_snapshot_time = 0.0

    # --- HAND STATE ---
    plocX, plocY = 0, 0
    clocX, clocY = 0, 0
    ema_x, ema_y = 0, 0
    alpha = 0.55 # Phase 24: Doubled Cursor Velocity (Lighting Fast smoothing)
    previous_pinch, previous_right_pinch = False, False
    dragging, swiping = False, False
    last_y, last_x = 0, 0
    hands_open_time = 0.0 # Phase 20: Restored Ignition Timer
    last_hand_check_time, last_macro_time = 0.0, 0.0 # Phase 21: Dual-Core Hand Spooling & Macro Cooldowns

    # --- EYE STATE ---
    prev_x, prev_y = 0.0, 0.0
    curr_x, curr_y = 0.0, 0.0
    left_EAR, right_EAR, mouth_MAR = 0.30, 0.30, 0.0
    blink_count = 0
    eyes_closed = False
    last_blink_time, last_gesture_time, last_scroll_time = 0.0, 0.0, 0.0
    left_wink_time, right_wink_time = 0.0, 0.0
    left_winking, right_winking = False, False
    eye_drag_mode, mouth_was_open = False, False

    print("="*50)
    print(" 👁️ T.O.M.M.Y. VISION KERNEL V3.2 ONLINE 👁️")
    print("="*50)

    last_active_vision = ""

    while cap.isOpened():
        current_vision = read_vision_mode()
        if current_vision != last_active_vision:
            show_mode_popup(f"Tracking: {current_vision}")
            last_active_vision = current_vision

        success, img = cap.read()
        if not success: break
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        current_time = time.time()
        
        # --- PHASE 11: Omni-Sensory Superpower Cache ---
        # Quietly drop a single high-quality frame of the Physical World to disk every 1.5s
        # This allows the Voice LLM to 'look' through the blocked Vision Camera.
        if current_time - last_snapshot_time > 1.5:
            snapshot_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "assets", ".latest_realworld.jpg")
            try: cv2.imwrite(snapshot_path, img)
            except: pass
            last_snapshot_time = current_time

        # =========================================================
        # 1️⃣ HAND TRACKING SYSTEM
        # =========================================================
        if current_vision == "hand":
            results = hands.process(imgRGB)
            if results.multi_hand_landmarks:
                hand_count = len(results.multi_hand_landmarks)
                total_active_fingers = 0
                
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    landmarks = hand_landmarks.landmark
                    index_x, index_y = int(landmarks[8].x * cam_w), int(landmarks[8].y * cam_h)
                    middle_x, middle_y = int(landmarks[12].x * cam_w), int(landmarks[12].y * cam_h)
                    thumb_x, thumb_y = int(landmarks[4].x * cam_w), int(landmarks[4].y * cam_h)
                    wrist_x, wrist_y = int(landmarks[0].x * cam_w), int(landmarks[0].y * cam_h)

                    fingers = []
                    finger_joints = [(8, 6), (12, 10), (16, 14), (20, 18)]
                    for tip, pip in finger_joints:
                        # Use pure geometric Y-axis math defined in the IEEE paper. 
                        # This ignores depth-scaling shrinkage completely!
                        fingers.append(1 if landmarks[tip].y < landmarks[pip].y else 0)

                    # Thumb check using horizontal X-axis mapping against the opposite side of the hand (Pinky MCP).
                    # Makes the thumb extension detection wildly stable regardless of camera angles.
                    thumb_extended = abs(landmarks[4].x - landmarks[17].x) > abs(landmarks[3].x - landmarks[17].x)
                    
                    dist_index = np.hypot(index_x - thumb_x, index_y - thumb_y)
                    dist_middle = np.hypot(middle_x - thumb_x, middle_y - thumb_y)
                    ring_x, ring_y = int(landmarks[16].x * cam_w), int(landmarks[16].y * cam_h)
                    dist_ring = np.hypot(ring_x - thumb_x, ring_y - thumb_y)
                    pinky_x, pinky_y = int(landmarks[20].x * cam_w), int(landmarks[20].y * cam_h)
                    dist_pinky = np.hypot(pinky_x - thumb_x, pinky_y - thumb_y) # Phase 24: Fixed dropped pinky bounds
                    
                    # Accumulate fingers for the Phase 20 global trigger
                    total_active_fingers += sum(fingers) + (1 if thumb_extended else 0)

                    # --- PHASE 23: GEOMETRIC CLASSIFIERS ---
                    is_index_only = fingers == [1, 0, 0, 0] and not thumb_extended
                    is_dragging_text = dist_index < 55 and sum(fingers[1:]) == 0
                    is_fist = fingers == [0, 0, 0, 0] and not thumb_extended
                    is_peace = fingers == [1, 1, 0, 0] and not thumb_extended
                    is_palm = fingers == [1, 1, 1, 1]
                    is_rock = fingers == [1, 0, 0, 1] and not thumb_extended
                    is_thumb_up = fingers == [0, 0, 0, 0] and thumb_extended
                    is_shaka = fingers == [0, 0, 0, 1] and thumb_extended

                    # --- ACTIVE SPATIAL MATHEMATICS ---
                    box_margin = 150
                    cv2.rectangle(img, (box_margin, box_margin), (cam_w-box_margin, cam_h-box_margin), (255, 255, 255), 1)
                    mapped_x = np.interp(index_x, (box_margin, cam_w-box_margin), (0, screen_w))
                    mapped_y = np.interp(index_y, (box_margin, cam_h-box_margin), (0, screen_h))
                    if ema_x == 0 and ema_y == 0: ema_x, ema_y = mapped_x, mapped_y
                    ema_x, ema_y = (alpha * mapped_x) + ((1 - alpha) * ema_x), (alpha * mapped_y) + ((1 - alpha) * ema_y)
                    
                    # Track relative movement distance unconditionally for Swiping Macros
                    clocX, clocY = ema_x, ema_y

                    # 1️⃣ THE NAVIGATION WAND (Cursor & Editing)
                    if is_index_only or is_dragging_text or is_fist:
                        cv2.putText(img, "WAND / EDITING", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 3)
                        try: pyautogui.moveTo(clocX, clocY)
                        except: pass
                        
                        # Selection / Left Click 
                        if dist_index < 55: 
                            if not previous_pinch: pyautogui.mouseDown(); previous_pinch = True
                        else: 
                            if previous_pinch: pyautogui.mouseUp(); previous_pinch = False
                            
                        # Dedicated Copy
                        if dist_middle < 55: 
                            if not previous_right_pinch: pyautogui.hotkey('ctrl', 'c'); previous_right_pinch = True
                        else: previous_right_pinch = False
                        
                        # Dedicated Paste
                        if dist_ring < 55: 
                            if not dragging: pyautogui.hotkey('ctrl', 'v'); dragging = True 
                        else: dragging = False
                        
                        # Dedicated Close Tab / App (`Ctrl+W`)
                        if dist_pinky < 55:
                            if current_time - last_macro_time > 0.8: # Cooldown to prevent closing multiple tabs instantly
                                pyautogui.hotkey('ctrl', 'w')
                                last_macro_time = current_time
                        
                        # Sledgehammer Drag-Drop
                        if is_fist:
                            if not swiping: pyautogui.mouseDown(); swiping = True
                        elif not is_fist and swiping:
                            pyautogui.mouseUp(); swiping = False

                    # 2️⃣ THE SCISSORS (Scroll)
                    elif is_peace:
                        cv2.putText(img, "SCROLL ENGINE", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)
                        if current_time - last_macro_time > 0.05:
                            dist_scissor = np.hypot(index_x - middle_x, index_y - middle_y)
                            if dist_scissor < 40: pyautogui.scroll(100); last_macro_time = current_time
                            elif dist_scissor > 85: pyautogui.scroll(-100); last_macro_time = current_time

                    # 3️⃣ THE WINDOW MANAGER (Palm)
                    elif is_palm:
                        cv2.putText(img, "WINDOW SNAP", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                        if current_time - last_macro_time > 0.6:
                            if clocX - last_x > 300: pyautogui.hotkey('alt', 'tab'); last_macro_time = current_time
                            elif clocX - last_x < -300: pyautogui.hotkey('alt', 'shift', 'tab'); last_macro_time = current_time
                            elif clocY - last_y < -200: pyautogui.hotkey('win', 'up'); last_macro_time = current_time
                            elif clocY - last_y > 200: pyautogui.hotkey('win', 'down'); last_macro_time = current_time

                    # 4️⃣ THE MEDIA CONTROLLER (Rock On)
                    elif is_rock:
                        cv2.putText(img, "MEDIA / TABS", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)
                        if current_time - last_macro_time > 0.8:
                            if clocX - last_x > 300: pyautogui.press('nexttrack'); last_macro_time = current_time
                            elif clocX - last_x < -300: pyautogui.press('prevtrack'); last_macro_time = current_time
                        if dist_index < 55:
                            if not previous_pinch: pyautogui.press('playpause'); previous_pinch = True
                        else: previous_pinch = False

                    # 5️⃣ THE HARDWARE OVERLORD (Thumb/Shaka)
                    elif is_thumb_up or is_shaka:
                        cv2.putText(img, "HARDWARE LEVEL", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        if current_time - last_macro_time > 0.10:
                            if hand_count == 1: # BRIGHTNESS
                                try:
                                    if is_thumb_up: threading.Thread(target=sbc.set_brightness, args=('-5',)).start()
                                    if is_shaka: threading.Thread(target=sbc.set_brightness, args=('+5',)).start()
                                except: pass
                            else: # VOLUME
                                if is_thumb_up: pyautogui.press('volumedown')
                                if is_shaka: pyautogui.press('volumeup')
                            last_macro_time = current_time

                    # Anchor final comparative coordinates unconditionally
                    last_y, last_x = clocY, clocX

                # --- Phase 20: 10-Finger Eye Mode Ignition Sequence ---
                # Check AFTER both hands have been independently mapped in the loop
                if hand_count == 2:
                    if total_active_fingers >= 8: # Phase 24: Lowered threshold from 10 to bypass Thumb depth-of-field failures!
                        hands_open_time = current_time
                    elif total_active_fingers == 0 and hands_open_time > 0:
                        if current_time - hands_open_time < 2.0: # Bumped window slightly
                            print("\n[⚡ BIO-GESTURE DETECTED] Both hands closed from Full Extension. Routing OS Power to Eye Engine...")
                            try:
                                with open(STATE_FILE, "r") as f: state_data = json.load(f)
                            except: state_data = {}
                            
                            state_data["vision_mode"] = "eye"
                            with open(STATE_FILE, "w") as f: json.dump(state_data, f)
                            
                            hands_open_time = 0.0 # Reset Trigger Data
                            current_vision = "eye"
                            last_active_vision = "" # Defeat the cached state immediately to force UI Pop-up render

        # =========================================================
        # 2️⃣ EYE TRACKING SYSTEM (FaceMesh)
        # =========================================================
        elif current_vision == "eye":
            
            # --- Phase 21: 2Hz Nano-Scale Hand Interceptor ---
            if current_time - last_hand_check_time > 0.5:
                small_img = cv2.resize(imgRGB, (256, 144)) # Shrink 96% of pixels away
                hand_ping = hands.process(small_img)
                if hand_ping.multi_hand_landmarks:
                    print("\n[⚡ HAND DETECTED] Intercepted Physical Hand Movement. Snapping OS back to Hand Engine...")
                    try:
                        with open(STATE_FILE, "r") as f: d = json.load(f)
                    except: d = {}
                    d["vision_mode"] = "hand"
                    with open(STATE_FILE, "w") as f: json.dump(d, f)
                    
                    last_hand_check_time = current_time
                    current_vision = "hand"
                    last_active_vision = "" # Forces immediate UI Notification
                    continue # Sever FaceMesh logic for this frame to boost hand-off speed
                last_hand_check_time = current_time

            results = face_mesh.process(imgRGB)
            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0].landmark
                left_iris, right_iris = landmarks[468], landmarks[473]

                # --- Cursor Control ---
                iris_x, iris_y = (left_iris.x + right_iris.x) / 2.0, (left_iris.y + right_iris.y) / 2.0
                norm_x, norm_y = (iris_x - LEFT_BOUND) / (RIGHT_BOUND - LEFT_BOUND), (iris_y - TOP_BOUND) / (BOTTOM_BOUND - TOP_BOUND)
                norm_x, norm_y = max(0.0, min(1.0, norm_x)), max(0.0, min(1.0, norm_y))
                screen_x, screen_y = norm_x * screen_w, norm_y * screen_h
                
                dist = hypot(screen_x - prev_x, screen_y - prev_y)
                if dist < 2.5: curr_x, curr_y = prev_x, prev_y # Deadzone filter
                else:
                    smooth_factor = max(2.0, SMOOTHENING / 1.5) if dist > 60.0 else SMOOTHENING
                    curr_x, curr_y = prev_x + (screen_x - prev_x) / smooth_factor, prev_y + (screen_y - prev_y) / smooth_factor

                mx, my = max(0, min(screen_w - 1, int(curr_x))), max(0, min(screen_h - 1, int(curr_y)))
                try: pyautogui.moveTo(mx, my)
                except: pass
                prev_x, prev_y = curr_x, curr_y

                # --- Optics Calculations ---
                l_eye = [landmarks[33], landmarks[160], landmarks[158], landmarks[133], landmarks[153], landmarks[144]]
                r_eye = [landmarks[362], landmarks[385], landmarks[387], landmarks[263], landmarks[373], landmarks[380]]
                mouth = [landmarks[78], landmarks[13], landmarks[308], landmarks[14]]

                left_EAR, right_EAR = (left_EAR * 0.6) + (calculate_ear(l_eye, cam_w, cam_h) * 0.4), (right_EAR * 0.6) + (calculate_ear(r_eye, cam_w, cam_h) * 0.4)
                mouth_MAR = (mouth_MAR * 0.6) + (calculate_mar(mouth, cam_w, cam_h) * 0.4)

                # MOUTH OPEN (Toggle Drag Mode)
                if mouth_MAR > MOUTH_AR_THRESHOLD:
                    if not mouth_was_open and current_time - last_gesture_time > GESTURE_COOLDOWN:
                        eye_drag_mode = not eye_drag_mode
                        if eye_drag_mode: pyautogui.mouseDown()
                        else: pyautogui.mouseUp()
                        last_gesture_time = current_time
                        mouth_was_open = True
                else: mouth_was_open = False

                # WINK DETECTION (L/R Clicks)
                is_left_wink = left_EAR < WINK_THRESHOLD and right_EAR > left_EAR + 0.05
                is_right_wink = right_EAR < WINK_THRESHOLD and left_EAR > right_EAR + 0.05
                both_closed = left_EAR < EAR_THRESHOLD and right_EAR < EAR_THRESHOLD

                if is_left_wink and not both_closed and not right_winking:
                    if not left_winking: left_wink_time = current_time; left_winking = True
                    elif current_time - left_wink_time > WINK_HOLD_TIME and current_time - last_gesture_time > GESTURE_COOLDOWN:
                        pyautogui.click(); last_gesture_time = current_time; left_winking = False
                else: left_winking = False

                if is_right_wink and not both_closed and not left_winking:
                    if not right_winking: right_wink_time = current_time; right_winking = True
                    elif current_time - right_wink_time > WINK_HOLD_TIME and current_time - last_gesture_time > GESTURE_COOLDOWN:
                        pyautogui.rightClick(); last_gesture_time = current_time; right_winking = False
                else: right_winking = False

                # BLINKS & SCROLLING
                if both_closed and not eyes_closed and current_time - last_gesture_time > 0.1: eyes_closed = True
                elif not both_closed and eyes_closed:
                    blink_count = 1 if current_time - last_blink_time > DOUBLE_BLINK_TIME else int(blink_count) + 1
                    last_blink_time, eyes_closed = current_time, False
                    if blink_count == 1: pyautogui.click()
                    elif blink_count == 2: pyautogui.doubleClick()
                    elif blink_count >= 3: pyautogui.hotkey('win', 'printscreen'); blink_count = 0
                    last_gesture_time = current_time
                
                if left_EAR > EAR_THRESHOLD and right_EAR > EAR_THRESHOLD and not eye_drag_mode:
                    if current_time - last_scroll_time > SCROLL_COOLDOWN:
                        if norm_y < 0.20: pyautogui.scroll(SCROLL_AMOUNT); last_scroll_time = current_time
                        elif norm_y > 0.80: pyautogui.scroll(-SCROLL_AMOUNT); last_scroll_time = current_time

                cv2.putText(img, "EYE TRACKING ACTIVE", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                if eye_drag_mode: cv2.putText(img, "[DRAGGING]", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        cv2.imshow("T.O.M.M.Y. Unified Vision Engine", img)
        if cv2.waitKey(1) & 0xFF == 27: break # ESC to quit

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_vision_engine()
