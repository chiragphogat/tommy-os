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

pyautogui.FAILSAFE = False

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

    # --- HAND STATE ---
    plocX, plocY = 0, 0
    clocX, clocY = 0, 0
    ema_x, ema_y = 0, 0
    alpha = 0.1 
    previous_pinch, previous_right_pinch = False, False
    dragging, swiping = False, False
    last_y, last_x = 0, 0
    hand_current_mode = "NAVIGATION"
    last_mode_switch_time = time.time()
    mode_colors = {"NAVIGATION": (255, 0, 255), "WINDOW": (0, 255, 0), "BROWSER": (0, 255, 255), "SYSTEM": (0, 0, 255)}

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

        # =========================================================
        # 1️⃣ HAND TRACKING SYSTEM
        # =========================================================
        if current_vision == "hand":
            results = hands.process(imgRGB)
            if results.multi_hand_landmarks:
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
                        tip_x, tip_y = int(landmarks[tip].x * cam_w), int(landmarks[tip].y * cam_h)
                        pip_x, pip_y = int(landmarks[pip].x * cam_w), int(landmarks[pip].y * cam_h)
                        fingers.append(1 if np.hypot(tip_x - wrist_x, tip_y - wrist_y) > np.hypot(pip_x - wrist_x, pip_y - wrist_y) else 0)

                    thumb_ip_x, thumb_ip_y = int(landmarks[3].x * cam_w), int(landmarks[3].y * cam_h)
                    thumb_extended = np.hypot(thumb_x - wrist_x, thumb_y - wrist_y) > np.hypot(thumb_ip_x - wrist_x, thumb_ip_y - wrist_y)
                    is_thumbs_up = (fingers == [0, 0, 0, 0] and thumb_extended)

                    if is_thumbs_up:
                        if current_time - last_mode_switch_time > 1.5:
                            modes = ["NAVIGATION", "WINDOW", "BROWSER", "SYSTEM"]
                            hand_current_mode = modes[(modes.index(hand_current_mode) + 1) % len(modes)]
                            last_mode_switch_time = current_time
                            show_mode_popup(hand_current_mode, "HAND MODE")

                    color = mode_colors.get(hand_current_mode, (255,255,255))
                    cv2.putText(img, f"HAND: {hand_current_mode}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

                    # --- Cursor Math ---
                    if fingers == [1, 0, 0, 0] and not is_thumbs_up:
                        box_margin = 150
                        cv2.rectangle(img, (box_margin, box_margin), (cam_w-box_margin, cam_h-box_margin), color, 2)
                        mapped_x = np.interp(index_x, (box_margin, cam_w-box_margin), (0, screen_w))
                        mapped_y = np.interp(index_y, (box_margin, cam_h-box_margin), (0, screen_h))
                        if ema_x == 0 and ema_y == 0: ema_x, ema_y = mapped_x, mapped_y
                        ema_x, ema_y = (alpha * mapped_x) + ((1 - alpha) * ema_x), (alpha * mapped_y) + ((1 - alpha) * ema_y)
                        clocX, clocY = ema_x, ema_y
                        try: pyautogui.moveTo(clocX, clocY)
                        except: pass
                        last_y, last_x = clocY, clocX

                    # --- Context Macros ---
                    if hand_current_mode == "NAVIGATION":
                        if np.hypot(index_x - thumb_x, index_y - thumb_y) < 30: 
                            if not previous_pinch: pyautogui.click(); previous_pinch = True
                        else: previous_pinch = False
                        if np.hypot(middle_x - thumb_x, middle_y - thumb_y) < 30 and fingers[1:] == [0,0,0]: 
                            if not previous_right_pinch: pyautogui.rightClick(); previous_right_pinch = True
                        else: previous_right_pinch = False
                        if sum(fingers) == 0 and not is_thumbs_up:
                            if not dragging: pyautogui.mouseDown(); dragging = True
                        else:
                            if dragging: pyautogui.mouseUp(); dragging = False

        # =========================================================
        # 2️⃣ EYE TRACKING SYSTEM (FaceMesh)
        # =========================================================
        elif current_vision == "eye":
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
