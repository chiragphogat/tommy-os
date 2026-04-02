import os
import sys
import time
from unittest.mock import MagicMock

# --- MOCK HEAVY HARDWARE DEPENDENCIES ---
sys.modules['pyautogui'] = MagicMock()
sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['pycaw'] = MagicMock()
sys.modules['pycaw.pycaw'] = MagicMock()
sys.modules['comtypes'] = MagicMock()
sys.modules['speech_recognition'] = MagicMock()
sys.modules['pvporcupine'] = MagicMock()
sys.modules['easyocr'] = MagicMock()
sys.modules['uiautomation'] = MagicMock()
sys.modules['screen_brightness_control'] = MagicMock()
sys.modules['requests'] = MagicMock()
sys.modules['bs4'] = MagicMock()
sys.modules['dotenv'] = MagicMock()
sys.modules['openai'] = MagicMock()
sys.modules['edge_tts'] = MagicMock()
sys.modules['psutil'] = MagicMock()
sys.modules['pvrecorder'] = MagicMock()
sys.modules['keyboard'] = MagicMock()

# Append root to path so we can import src modules
sys.path.append(os.path.abspath("C:\\tommyv"))

from src import voice_engine

# --- Mocking Speak to intercept TTS output ---
intercepted_speech = []
def mock_speak(text):
    print(f"[MOCK TTS OUTPUT]: {text}")
    intercepted_speech.append(text)

voice_engine.speak = mock_speak

def test_superpower_mode():
    print("--- [TEST 1] ACTIVATING SUPERPOWER MODE ---")
    voice_engine.execute_logic_chain("activate superpower mode")
    time.sleep(1)
    
    assert "superpower" in voice_engine.CURRENT_VOICE_MODE, "Voice Mode did not update to 'superpower'"
    print("✅ Mode switch successful.")
    
    print("\n--- [TEST 2] WINDOW AWARENESS ---")
    intercepted_speech.clear()
    voice_engine.execute_logic_chain("what window am i in")
    time.sleep(2)
    
    found_window = any("You are currently looking at" in speech for speech in intercepted_speech)
    print("✅ Window awareness successful." if found_window else "❌ Window announcer failed.")

    print("\n--- [TEST 3] OCR SCREEN READER ---")
    intercepted_speech.clear()
    voice_engine.execute_logic_chain("read the screen")
    
    # Wait for the background OCR thread to finish (max 15 seconds)
    print("Waiting for OCR Engine...")
    timeout = 15
    while timeout > 0:
        if any("The screen says:" in speech or "I do not see any" in speech for speech in intercepted_speech):
            break
        time.sleep(1)
        timeout -= 1
        
    found_ocr = any("The screen says:" in speech for speech in intercepted_speech)
    print("✅ OCR successful." if found_ocr else "⚠️ OCR returned no text or timed out (expected if headless/blank screen).")
    
    
    print("\n=== SYSTEMATIC SUPERPOWER CAPABILITY AUDIT ===")
    
    commands_to_test = [
        ("scroll down", "I have executed: Scroll Down"),
        ("volume up", "I have executed: Volume Increased"),
        ("brightness up", "I have executed: Brightness Increased"),
        ("minimize", "I have executed: Minimized Window"),
        ("copy", "I have executed: Copied"),
        ("type unit tests are passing", "I have executed: Text Typed"),
        ("open notepad", "Launched notepad"), 
        ("play music", "I have executed: Toggled Media"),
        ("next track", "I have executed: Next Track"),
        ("switch application", "I have executed: Switched Application"),
        ("desktop", "I have executed: Showed Desktop"),
        ("switch to eye control", "Optical eye tracking enabled")
    ]
    
    passed_tests = 0
    for cmd, expected_response_snippet in commands_to_test:
        intercepted_speech.clear()
        print(f"\n[EVALUATING]: '{cmd}'")
        voice_engine.execute_logic_chain(cmd)
        
        # Check if the expected string physically reached Swara's vocal engine
        found = any(expected_response_snippet.lower() in speech.lower() for speech in intercepted_speech)
        if found:
            print(f"✅ Success: Uttered confirmation -> {intercepted_speech[0] if intercepted_speech else expected_response_snippet}")
            passed_tests += 1
        else:
            print(f"❌ Failed: TTS Engine did not articulate the confirmation for '{cmd}'")
            print(f"   ↳ Captured TTS: {intercepted_speech}")
            
    print(f"\n=======================================================")
    print(f"🎯 Exhaustive Superpower Audit Complete | {passed_tests}/{len(commands_to_test)} Functions Passed")
    print(f"=======================================================\n")

if __name__ == "__main__":
    test_superpower_mode()
