# T.O.M.M.Y. OS 👁️🧠
**The Fully Hands-Free, Vision & Voice Operations Kernel for Windows.**

> 🌍 **[CLICK HERE TO VIEW OUR LIVE STREAMLIT PORTFOLIO](https://tommy-os-sye8ypzv6r4u8ufd7o8uv3.streamlit.app/)**  
> *Read the official IEEE architectural paper, view the 21-point geometric framework, and analyze the offline latency bounds on our cloud platform!*

I was sick of computers keeping us artificially tethered to our desks. Voice assistants are cool, but if you ask a commercial AI to "drag and drop" a file on your Windows desktop, it crashes helplessly. 

T.O.M.M.Y. fixes this. This isn't a wrapper for a webpage. This is a monolithic kernel script that takes over Windows completely using nothing but a regular webcam and microphone. We literally threw out machine learning controllers for raw geometric line-math to make the system process physical spatial movements in a buttery 18 milliseconds on local CPUs.

## ⚠️ The Golden Question: "Wait, does this need heavy AI to run?"
**NO.** 
The entire core operating system routing (clicking, scrolling, typing, maximizing apps, pulling volume/brightness hardware levers) runs on pure, localized, hardcoded Python natively in your memory wrapper. It uses ZERO cloud GPUs. 

The ONLY time the massive LLM neural blocks fire up is if you explicitly command Tommy to actively *read* the screen ("What am I looking at?") or to *summarize* something complex. The driving works without an IQ engine!

---

## 🛠️ HOW TO INSTALL IT

1. **Clone it.** Bring this repository down locally onto your Windows rig.
2. **Setup Script.** Double-click the `setup.bat` file. 
   - This script auto-installs every single hardcore library Tommy needs (Python 3.10+ required).
3. **The Local Neural Core (Ollama):**
   - You MUST have [Ollama](https://ollama.com/) running on your Windows machine if you want Tommy to be able to physically "see" your screen and answer intelligent questions. 
   - `setup.bat` will automatically pull down the exact neural weights we used (`moondream` for screen reading and `llama3:8b` for core logic).
4. **Wake Word Configuration:**
   - We use Picovoice Porcupine to run the "Hey Tommy" listener cleanly on your CPU without leaking memory.
   - You must go to [Picovoice Console](https://console.picovoice.ai) and sign up for a free Access Key. 
   - Open the hidden `.env` file at the root of your folder and paste your key inside: `PORCUPINE_ACCESS_KEY="paste_it_here"`

## 🚀 HOW TO DRIVE

Double click `tommy_os.py` to boot up the dual-channel processor array.

### 🖖 The Spatial Hand Tracker 
Just put your hands up! T.O.M.M.Y uses a dynamic bounding box and strict geometric Y-axis math to find you, even if you slouch.

- **Index Finger Only:** This acts as your magic wand and mouse cursor. 
- **Pinch (Thumb + Index):** Left Click.
- **Pinch (Thumb + Middle):** Copy (`Ctrl+C`).
- **Pinch (Thumb + Ring):** Paste (`Ctrl+V`).
- **Pinch (Thumb + Pinky):** Close Application.
- **Closed Fist:** Hold this to "Grab" and physically Drag-and-Drop files.
- **Peace Sign (Two Fingers):** Scroll Engine. Move your fingers apart to scroll Up, smash them together to scroll Down!
- ........and there are God-level hardware modes (Thumb/Shaka) for dragging physical brightness/volume dials natively without making UI clicks!

### 🗣️ The Voice Engine
Say `"Hey Tommy"` loudly. When you hear "Yes?", give him an order. Don't worry if people are talking or vacuuming; we injected driver-yielding locks that perfectly manage the Windows microphone so it never goes deaf.

You can say arbitrary hard commands:
- `"Open Youtube"`
- `"Close Task Manager"`
- `"Volume Up"`
- `"Type Hello World"`
- `"Scroll down"`

Or you can use the Neural Hooks:
- `"Look at my screen."` (Triggers `src/rag_vision.py` to quietly capture your Local Windows display and pipe the base64 screenshot into a localized Moondream GPU pipeline to syntactically "see" what you are working on!)
- `"Research how to build a jetpack."` (Spawns background Python agents to scrape DuckDuckGo locally).
- `"Execute ipconfig"` (Spawns a shell agent to run the terminal and summarize the output for you).

### 🕶️ Environmental "God Modes" (No Wake Words!)
Tired of saying "Hey Tommy" every 10 seconds? Switch to a context mode where Tommy burns up the local microphone and actively listens to your ambient room chatter natively:

- **"Activate Study Mode":** Drops the wake words! He will sit there and listen indefinitely to Scroll and Volume configurations natively. 
- **"Activate Superpower Mode":** (Used for complete Blind Accessibility). Triggers the system to run headless UI checks and read out your hardware status endlessly in a loop.
- **"Activate Normal Mode":** Puts the Wake Word safety breaks back on.

---
We built this because we were tired of being strapped to keyboards. Break the desk. Build things.
