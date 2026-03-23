import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

pyautogui.FAILSAFE = False

import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_draw

def run_gesture_engine(cmd_queue=None):
    global clocX, clocY, plocX, plocY
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )

    screen_w, screen_h = pyautogui.size()

    cap = cv2.VideoCapture(0)
    cam_w, cam_h = 1280, 720
    cap.set(3, cam_w)
    cap.set(4, cam_h)

    plocX, plocY = 0, 0
    clocX, clocY = 0, 0
    ema_x, ema_y = 0, 0
    alpha = 0.1 # Ultra smooth, high physical weight (no jitter)
    previous_pinch, previous_right_pinch = False, False
    dragging, swiping = False, False
    last_y, last_x = 0, 0

    current_mode = "NAVIGATION"
    last_mode_switch_time = time.time()
    mode_colors = {
        "NAVIGATION": (255, 0, 255),
        "WINDOW": (0, 255, 0),
        "BROWSER": (0, 255, 255),
        "SYSTEM": (0, 0, 255)
    }

    # --- NON-BLOCKING TOP SCREEN POPUP ---
    import threading
    def show_mode_popup(mode_name):
        def popup():
            import tkinter as tk
            root = tk.Tk()
            root.overrideredirect(True) # Remove windows borders
            root.attributes('-topmost', True) # Keep on top
            root.attributes('-disabled', True) # Cannot steal typing focus
            root.attributes('-alpha', 0.85)
            root.geometry(f"600x80+{int(screen_w/2)-300}+50")
            root.configure(bg='#1e1e1e')
            label = tk.Label(root, text=f"T.O.M.M.Y.G MODE: {mode_name}", font=("Segoe UI", 24, "bold"), fg="#00ffcc", bg="#1e1e1e")
            label.pack(expand=True, fill='both')
            root.after(1500, root.destroy)
            root.mainloop()
        threading.Thread(target=popup, daemon=True).start()

    print("="*50)
    print(" ? T.O.M.M.Y.G V1.0 - GESTURE CONTROL ONLINE ?")
    print("="*50)
    print("Raise your Index finger to move the mouse.")
    print("Pinch your Index and Thumb together to Left-Click.")
    print("Press 'Q' on the physical keyboard to quit.")

    while cap.isOpened():
        
        # --- OS MULTI-CORE COMMAND QUEUE ---
        if cmd_queue is not None and not cmd_queue.empty():
            cmd = cmd_queue.get()
            if str(cmd).startswith("MODE:"):
                current_mode = str(cmd).split(":")[1]
                show_mode_popup(current_mode)
                
        success, img = cap.read()
        if not success: break

        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                landmarks = hand_landmarks.landmark
                index_x, index_y = int(landmarks[8].x * cam_w), int(landmarks[8].y * cam_h)
                middle_x, middle_y = int(landmarks[12].x * cam_w), int(landmarks[12].y * cam_h)
                thumb_x, thumb_y = int(landmarks[4].x * cam_w), int(landmarks[4].y * cam_h)

                # --- 360-DEGREE OMNIDIRECTIONAL FINGER EXTRACTION ---
                wrist_x, wrist_y = int(landmarks[0].x * cam_w), int(landmarks[0].y * cam_h)
                fingers = []

                # Index, Middle, Ring, Pinky Euclidean Bounds
                # Finger is "out" if the Tip is further from the Wrist than the PIP joint
                finger_joints = [(8, 6), (12, 10), (16, 14), (20, 18)]
                for tip, pip in finger_joints:
                    tip_x, tip_y = int(landmarks[tip].x * cam_w), int(landmarks[tip].y * cam_h)
                    pip_x, pip_y = int(landmarks[pip].x * cam_w), int(landmarks[pip].y * cam_h)

                    dist_tip = np.hypot(tip_x - wrist_x, tip_y - wrist_y)
                    dist_pip = np.hypot(pip_x - wrist_x, pip_y - wrist_y)
                    fingers.append(1 if dist_tip > dist_pip else 0)

                # Thumb Euclidean
                thumb_ip_x, thumb_ip_y = int(landmarks[3].x * cam_w), int(landmarks[3].y * cam_h)
                dist_thumb_tip = np.hypot(thumb_x - wrist_x, thumb_y - wrist_y)
                dist_thumb_ip = np.hypot(thumb_ip_x - wrist_x, thumb_ip_y - wrist_y)
                thumb_extended = dist_thumb_tip > dist_thumb_ip

                # --- MODE SWITCHING (Hold Thumbs Up [1,0,0,0] for 1.5 seconds) ---
                current_time = time.time()
                # 360-Degree Thumbs Up: Thumb is geometrically extended, all 4 fingers are folded into the palm
                is_thumbs_up = (fingers == [0, 0, 0, 0] and thumb_extended)

                if is_thumbs_up:
                    if current_time - last_mode_switch_time > 1.5:
                        modes = ["NAVIGATION", "WINDOW", "BROWSER", "SYSTEM"]
                        current_mode = modes[(modes.index(current_mode) + 1) % len(modes)]
                        last_mode_switch_time = current_time
                        cv2.putText(img, "MODE SWITCHED!", (400, 360), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
                        show_mode_popup(current_mode) # Trigger Windows top-screen UI

                # Display Current Mode on Camera Feed
                color = mode_colors.get(current_mode, (255,255,255))
                cv2.putText(img, f"MODE: {current_mode}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

                # --- 1. MOVEMENT MAPPING & EMA ---
                if fingers == [1, 0, 0, 0] and not is_thumbs_up:
                    box_margin = 150
                    cv2.rectangle(img, (box_margin, box_margin), (cam_w-box_margin, cam_h-box_margin), color, 2)
                    mapped_x = np.interp(index_x, (box_margin, cam_w-box_margin), (0, screen_w))
                    mapped_y = np.interp(index_y, (box_margin, cam_h-box_margin), (0, screen_h))

                    if ema_x == 0 and ema_y == 0: ema_x, ema_y = mapped_x, mapped_y
                    ema_x = (alpha * mapped_x) + ((1 - alpha) * ema_x)
                    ema_y = (alpha * mapped_y) + ((1 - alpha) * ema_y)

                    clocX, clocY = ema_x, ema_y
                    try: pyautogui.moveTo(clocX, clocY); plocX, plocY = clocX, clocY
                    except: pass
                    last_y, last_x = clocY, clocX

                # --- CONTEXTUAL ACTIONS ---
                if current_mode == "NAVIGATION":
                    distance_l = np.hypot(index_x - thumb_x, index_y - thumb_y)
                    if distance_l < 30: 
                        cv2.circle(img, ((index_x + thumb_x)//2, (index_y + thumb_y)//2), 15, (0, 255, 0), cv2.FILLED)
                        if not previous_pinch: pyautogui.click(); previous_pinch = True
                    else: previous_pinch = False

                    distance_r = np.hypot(middle_x - thumb_x, middle_y - thumb_y)
                    if distance_r < 30 and fingers[1:] == [0,0,0]: 
                        cv2.circle(img, ((middle_x + thumb_x)//2, (middle_y + thumb_y)//2), 15, (255, 0, 0), cv2.FILLED)
                        if not previous_right_pinch: pyautogui.rightClick(); previous_right_pinch = True
                    else: previous_right_pinch = False

                    if fingers == [1, 1, 0, 0]:
                        if last_y != 0: pyautogui.scroll(int((last_y - index_y) * 2))
                        last_y = index_y
                        cv2.putText(img, 'SCROLLING', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

                    if sum(fingers) == 0 and not is_thumbs_up:
                        if not dragging: pyautogui.mouseDown(); dragging = True
                        cv2.putText(img, 'DRAGGING', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                    else:
                        if dragging: pyautogui.mouseUp(); dragging = False

                elif current_mode == "WINDOW":
                    if sum(fingers) == 4:
                        cv2.putText(img, 'WINDOW SWIPE', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                        if last_x != 0:
                            # Massive 150 pixel threshold to stop false-positive jumping
                            if (index_x - last_x) > 150: pyautogui.hotkey('win', 'right'); time.sleep(0.5)
                            elif (index_x - last_x) < -150: pyautogui.hotkey('win', 'left'); time.sleep(0.5)
                            elif (last_y - index_y) > 150: pyautogui.hotkey('win', 'up'); time.sleep(0.5)
                            elif (last_y - index_y) < -150: pyautogui.hotkey('win', 'down'); time.sleep(0.5)
                        last_x, last_y = index_x, index_y

                    distance_l = np.hypot(index_x - thumb_x, index_y - thumb_y)
                    if distance_l < 30:
                        if not previous_pinch: pyautogui.hotkey('alt', 'f4'); previous_pinch = True
                    else: previous_pinch = False

                    if fingers == [1, 1, 0, 0]:
                        cv2.putText(img, 'VIRTUAL DESKTOP', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                        if last_x != 0:
                            # Massive 150 threshold
                            if (index_x - last_x) > 150: pyautogui.hotkey('ctrl', 'win', 'right'); time.sleep(0.5)
                            elif (index_x - last_x) < -150: pyautogui.hotkey('ctrl', 'win', 'left'); time.sleep(0.5)
                        last_x = index_x

                elif current_mode == "BROWSER":
                    if sum(fingers) == 4:
                        cv2.putText(img, 'BROWSER SWIPE', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                        if last_x != 0:
                            # Massive 150 threshold
                            if (index_x - last_x) > 150: pyautogui.hotkey('browserforward'); time.sleep(0.5)
                            elif (index_x - last_x) < -150: pyautogui.hotkey('browserback'); time.sleep(0.5)
                        last_x = index_x

                    distance_l = np.hypot(index_x - thumb_x, index_y - thumb_y)
                    if distance_l < 30:
                        if not previous_pinch: pyautogui.hotkey('ctrl', 't'); previous_pinch = True
                    else: previous_pinch = False

                    distance_r = np.hypot(middle_x - thumb_x, middle_y - thumb_y)
                    if distance_r < 30 and fingers[1:] == [0,0,0]:
                        if not previous_right_pinch: pyautogui.hotkey('ctrl', 'w'); previous_right_pinch = True
                    else: previous_right_pinch = False

                elif current_mode == "SYSTEM":
                    if fingers == [0, 0, 0, 1]:
                        cv2.putText(img, 'VOLUME', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                        if last_y != 0:
                            if (last_y - index_y) > 5: pyautogui.press('volumeup')
                            elif (last_y - index_y) < -5: pyautogui.press('volumedown')
                        last_y = index_y

                    if sum(fingers) == 0 and not is_thumbs_up:
                        cv2.putText(img, 'LOCKING SYSTEM', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                        if not previous_pinch:
                            time.sleep(2) # Fail-safe delay
                            # pyautogui.hotkey('win', 'l') 
                            print("System locked placeholder.")
                            previous_pinch = True
                    else: previous_pinch = False

        cv2.imshow("T.O.M.M.Y.G Camera Feed", img)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_gesture_engine()
