# tommy_os.py
import subprocess
import sys
import os
import time
import json

print("="*60)
print(" 🧠 BOOTING T.O.M.M.Y. OS MASTER KERNEL V3.2 (Monolithic) 🧠")
print("="*60)

# Initialize the Inter-Process Communication (IPC) State node
state_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), ".tommy_state.json")
try:
    with open(state_file, "w") as f:
        json.dump({"vision_mode": "hand"}, f)
    print("[OS] IPC Subprocess Bridge Initialized (Hand Tracking Default)")
except Exception as e:
    print(f"❌ [WARNING] IPC Bridge Failure: {e}")

# The new unified architecture dictates all core intelligence lives in `/src`
voice_script = os.path.join("src", "voice_engine.py")
gesture_script = os.path.join("src", "vision_engine.py")

# Because both voice and gesture now share the EXACT same Master Environment,
# we simply use `sys.executable` (the python currently running this script)
# to natively boot both engines synchronously without cross-environment collisions!

print("[OS] Allocating Engine 1: Auditory Intelligence & UI HUD...")
if os.path.exists(voice_script):
    p_voice = subprocess.Popen([sys.executable, voice_script])
else:
    print(f"❌ [FATAL] Monolithic failure. Could not locate {voice_script}")
    sys.exit(1)

time.sleep(3) # Give microphone hardware limits time to lock natively

print("[OS] Allocating Engine 2: Spatial Mathematics (CV2)...")
if os.path.exists(gesture_script):
    p_gesture = subprocess.Popen([sys.executable, gesture_script])
else:
    print(f"❌ [FATAL] Monolithic failure. Could not locate {gesture_script}")
    sys.exit(1)

print("\n✅ [OS_SYS] All Neural Pipelines Active.")
print("✅ T.O.M.M.Y. is functioning inside the Master Environment.")
print("You can visually track Tommy's listening state via the Top-Left Screen Box!")
print('Press (Ctrl+C) natively in this terminal to Shutdown both cores.\n')

try:
    p_voice.wait()
    p_gesture.wait()
except KeyboardInterrupt:
    print("\n[OS_SYS] Operator initiated hard shutdown. Killing processor threads...")
    p_voice.terminate()
    p_gesture.terminate()
    print("T.O.M.M.Y. OS safely unmounted.")
