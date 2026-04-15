# T.O.M.M.Y. OS 👁️🧠
**The Vision-First, Hands-Free Operations Kernel for Windows.**

> 🌍 **[CLICK HERE TO VIEW OUR LIVE STREAMLIT PORTFOLIO](https://tommy-os-sye8ypzv6r4u8ufd7o8uv3.streamlit.app/)**  
> *Read the official IEEE architectural paper, view the 21-point geometric framework, and analyze the offline latency bounds on our cloud platform!*

I was sick of computers keeping us artificially tethered to our desks. Voice assistants are cool, but if you ask a commercial AI to "drag and drop" a file on your Windows desktop, it crashes helplessly. 

T.O.M.M.Y. fixes this. This isn't a wrapper for a webpage. This is a monolithic kernel script that takes over Windows completely using nothing but a regular webcam and microphone. We literally threw out machine learning controllers for raw geometric line-math to make the system process physical spatial movements in a buttery 18 milliseconds on local CPUs.

## ⚠️ Vision-Primary / Offline Deterministic NLP
**NO LLMs. Voice is merely a Fallback.** 
For smooth, continuous day-to-day use, T.O.M.M.Y. prioritizes high-speed spatial vision inputs (Hands and Nose Tracking). Voice acts strictly as a secondary fallback. The entire core operating system routing runs natively in your memory wrapper. It uses ZERO cloud GPUs and ZERO LLM inference. All natural language processing is securely handled by lightweight spaCy models offline.

---

## 🛠️ HOW TO INSTALL IT

1. **Clone it.** Bring this repository down locally onto your Windows rig.
2. **Setup Script.** Double-click the `setup.bat` file. 
   - This script auto-installs every single hardcore library Tommy needs (Python 3.10+ required).
3. **The Local Deterministic Core (spaCy):**
   - Tommy processes language using `spaCy`. `setup.bat` will automatically download the required English grammar models.
4. **Wake Word Configuration:**
   - We use Picovoice Porcupine to run the "Hey Tommy" listener cleanly on your CPU without leaking memory.
   - You must go to [Picovoice Console](https://console.picovoice.ai) and sign up for a free Access Key. 
   - Open the hidden `.env` file at the root of your folder and paste your key inside: `PORCUPINE_ACCESS_KEY="paste_it_here"`

## 🚀 HOW TO DRIVE

Double click `tommy_os.py` to boot up the dual-channel processor array.

### 🖖 The Spatial Hand Tracker 
Just put your hands up! T.O.M.M.Y uses a dynamic bounding box and strict geometric Y-axis math to find you, even if you slouch. We've also heavily implemented a **Magnetic Cursor Lock** which mathematically freezes the cursor when your fingers pinch, instantly stopping organic hand jitter!

- **Index Finger Only:** This acts as your magic wand and mouse cursor. 
- **Pinch (Thumb + Index):** Left Click.
- **Pinch (Thumb + Middle):** Copy (`Ctrl+C`).
- **Pinch (Thumb + Ring):** Paste (`Ctrl+V`).
- **Pinch (Thumb + Pinky):** Close Application.
- **Closed Fist:** Hold this to "Grab" and physically Drag-and-Drop files.
- **Peace Sign (Two Fingers):** Scroll Engine. Move your fingers apart to scroll Up, smash them together to scroll Down!
- ........and there are God-level hardware modes (Thumb/Shaka) for dragging physical brightness/volume dials natively without making UI clicks!

### 👃 Nose-Pointing & Ocular Clicks
Sometimes standard eye pupils jitter terribly on standard webcams, making pixel-perfect clicks impossible. We decoupled the X/Y cursor tracking from the eyes entirely and tied it to the tip of your nose, allowing your head and facial expressions to control the entire OS smoothly without modes:

- **Nose Joystick:** Tilt your head slightly to steer the mouse pointer flawlessly.
- **Scroll Engine:** Move your nose to the absolute top/bottom 20% of your screen to scroll seamlessly.
- **Left Click:** 1 Fast Blink.
- **Right Click:** 2 Fast Blinks.
- **Close Tab (`Ctrl+W`):** 3 Fast Blinks.
- **Double-Click:** 4 Fast Blinks.
- **Copy / Paste:** Left Eye Wink = Copy, Right Eye Wink = Paste.
- **Play / Pause Media:** Medium Blink Hold (Close your eyes for half a second).
- **Previous / Next Track:** Tilt your head (ear to shoulder) Left or Right.

**The "Mouth" Modifier Key:**
Opening your jaw wide (Yawn state) acts like holding down `Shift` or `Alt` on a keyboard to modify actions!
- **Open Mouth (Static):** Toggles Drag-And-Drop mode.
- **Open Mouth + 2 Fast Blinks:** Undo (`Ctrl+Z`).
- **Open Mouth + Left Wink:** Alt-Tab (Cycle Windows).
- **Open Mouth + Right Wink:** Select All (`Ctrl+A`).
- **Open Mouth + Nose Scroll:** Volume Up / Volume Down natively.

- **Deep Squeeze Hold (> 3.0s):** Instantly shuts down the webcam face math and routes OS computing power safely back to Hand Tracking natively.

### 🗣️ The Voice Fallback
If you can't use vision, say `"Hey Tommy"` loudly. When you hear "Yes?", give him an order. Don't worry if people are talking or vacuuming; we injected driver-yielding locks that perfectly manage the Windows microphone so it never goes deaf.

You can say arbitrary hard commands:
- `"Open Youtube"`
- `"Close Task Manager"`
- `"Volume Up"`
- `"Type Hello World"`
- `"Scroll down"`

> **Dynamic Wake Words:** You can also dynamically tell Tommy to respond to a new name purely via voice! Say: *"change model name to JARVIS"*. 
> **Offline Fail-Safe:** If your free Picovoice token ever expires, the system dynamically catches the API error and automatically shifts into "Normal Ambient Mode", falling back natively onto your local microphone array.

### 🕶️ Environmental "God Modes" (No Wake Words!)
Tired of saying "Hey Tommy" every 10 seconds? Switch to a context mode where Tommy burns up the local microphone and actively listens to your ambient room chatter natively:

- **"Activate Study Mode":** Drops the wake words! He will sit there and listen indefinitely to Scroll and Volume configurations natively. 
- **"Activate Normal Mode":** Puts the Wake Word safety breaks back on.

---
We built this because we were tired of being strapped to keyboards. Break the desk. Build things.
