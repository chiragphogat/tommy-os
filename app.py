import streamlit as st
import base64
import cv2
import numpy as np
import mediapipe as mp
import mediapipe.python.solutions.hands as mp_hands_lib
import mediapipe.python.solutions.drawing_utils as mp_drawing_lib

st.set_page_config(
    page_title="T.O.M.M.Y. OS Project Showcase",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CSS Styling ---
st.markdown("""
    <style>
        .stApp {
            background-color: #0E1117;
            color: #C9D1D9;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
        h1, h2, h3, h4 {
            color: #58A6FF;
            font-weight: 800;
        }
        .highlight-box {
            background-color: #161B22;
            border-left: 4px solid #58A6FF;
            padding: 1.5rem;
            border-radius: 6px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        .warning-box {
            background-color: #2D1115;
            border-left: 4px solid #F85149;
            padding: 1.5rem;
            border-radius: 6px;
            color: #FF7B72;
            margin-bottom: 2rem;
        }
        .team-box {
            background-color: #1a1e24;
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            border: 1px solid #30363d;
        }
        .team-name {
            color: #58A6FF;
            font-size: 1.1rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAV ---
with st.sidebar:
    st.image("https://github.com/fluidicon.png", width=50) # Generic dark-mode icon setup
    st.markdown("## Navigation")
    st.markdown("- [Home](#t-o-m-m-y-os)")
    st.markdown("- [Deployment Limitations](#warning-academic-architecture-notice)")
    st.markdown("- [Live System Demo](#-interactive-system-demonstration)")
    st.markdown("- [Architecture Deep Dive](#-core-engineering-achievements)")
    st.markdown("- [The Engineering Team](#-the-engineering-team)")

# --- HERO SECTION ---
st.title("T.O.M.M.Y. OS")
st.markdown("### A Multi-Process Architecture for Hands-Free Windows Navigation Without Cloud Dependencies")

st.markdown("""
<div class="warning-box">
    <strong>⚠️ ACADEMIC ARCHITECTURE NOTICE: CLOUD DEPLOYMENT LIMITATIONS</strong><br><br>
    Most standard Python projects deployed to the cloud are web apps or data parsers. T.O.M.M.Y is drastically different: It is a <em>monolithic Operating System Kernel wrapper</em> designed natively for local Windows execution.<br><br>
    The script explicitly bypasses the standard mouse, alters hardware constraints (like screen brightness), and analyzes active GUI windows utilizing a localized USB Webcam and Microphone. Because Streamlit Cloud runs inside headless Linux Docker containers that completely lack physical screens, hardware microphones, and speakers, <strong>the actual OS engine cannot be live-executed from this server</strong>. <br><br>
    This website serves as our Comprehensive Project Portfolio. To physically test the OS, the source code must be compiled natively on a local Windows machine.
</div>
""", unsafe_allow_html=True)

# --- GITHUB URL ENTRY ---
st.markdown("## 📥 Source Code Registry")
st.markdown("To evaluate this project locally, execute the following within a Windows environment:")
st.code("git clone https://github.com/chiragphogat/tommy-os.git\ncd tommy-os\nsetup.bat", language="bash")
st.markdown("""[🚀 **Launch Full GitHub Repository Here**](https://github.com/chiragphogat/tommy-os)""")

st.divider()

# --- DEMO TERMINAL SECTION ---
st.markdown("## 🎮 Interactive Vision Demonstration")
st.markdown("While this server cannot physically move your mouse, we can demonstrate the exact **Neural Hand-Tracking mathematics** Tommy utilizes to process spatial geometry!")

demo_expander = st.expander("👁️ Try the Vision Engine Architecture (Requires Camera)", expanded=True)
with demo_expander:
    st.markdown("**Hold your hand up to the camera and take a snapshot to test the MediaPipe geometric mapping framework:**")
    picture = st.camera_input("Vision Engine Input Stream")
    
    if picture:
        # Load the image array natively
        bytes_data = picture.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        
        # Initiate MediaPipe Native Geometry Parsing
        mp_hands = mp_hands_lib
        mp_drawing = mp_drawing_lib
        
        with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
            results = hands.process(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))
            
            if results.multi_hand_landmarks:
                st.success("✅ **Spatial Hit!** Tommy successfully mapped your geometrical skeleton structure.")
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        cv2_img, 
                        hand_landmarks, 
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(88, 166, 255), thickness=2, circle_radius=4), # Blue
                        mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2)  # White
                    )
                    
                    # Core Y-Axis Math Simulation
                    tip_y = hand_landmarks.landmark[8].y  # Index Finger Tip
                    pip_y = hand_landmarks.landmark[6].y  # Index Finger Knuckle
                    
                    st.code(f">>> Processing Y-Axis Delta...\nIndex Tip Y: {tip_y:.4f}\nIndex Knuckle Y: {pip_y:.4f}\nGeometry Result: {'Wand Active (Tip above Knuckle)' if tip_y < pip_y else 'Wand Disabled'}")
            else:
                st.warning("❌ No spatial hand structures detected. Make sure your hand is fully in the frame!")
                
        # Return processed image to browser natively
        st.image(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB), channels="RGB")

st.divider()

# --- ARCHITECTURE SECTION ---
st.markdown("## 🧠 Core Engineering Achievements")

st.markdown("""
<div class="highlight-box">
Our research completely tears down traditional Human-Computer Interaction (HCI). While modern Voice Assistants exist, they rely heavily on cloud-hosted Large Language Models (LLMs), subjecting local OS execution to tremendous network latency. We successfully decoupled OS control from heavy neural processing. Standard commands execute natively using local geometry loops in under 20ms, proving that intensive visual and audial computing can function flawlessly on lightweight Windows hardware without cloud reliance.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 1. Y-Axis Spatial Mathematics")
    st.markdown("""
    Standard OpenCV hand tracking uses Euclidean bounding distance boxes (measuring pixels between fingers). This inherently shatters when a user leans back in their chair, as the camera scale shrinks.
    T.O.M.M.Y bypasses this by utilizing pure **Y-axis delta-coordinate math**. It strictly measures if a fingertip is mathematically positioned *below* the physical plane of a knuckle (`tip.y > pip.y`), rendering the tracking immune to physical depth scaling.
    """)
    st.markdown("### 3. Asymmetric Neural Invocation")
    st.markdown("""
    The system isolates basic tasks (like Volume adjustment and UI clicks) into raw Python OS routines that fire instantly. We only trigger massive LLMs (`llama3` and `moondream` using Ollama) when complex context is required, such as commanding the assistant to "Read my screen".
    """)

with col2:
    st.markdown("### 2. Hardware Driver Lock Patches")
    st.markdown("""
    Windows OS inherently restricts active microphone arrays to a single port process. Attempting to run a Wake-Word listener (`pvporcupine`) alongside a Command Listener (`speech_recognition`) caused immediate Thread crashing.
    We engineered an aggressive, dynamic `recorder.stop()` injection protocol. The exact millisecond the wake word is detected, the audio array is forcefully yielded, instantly unlocking the hardware port for the Command Engine without memory leaking.
    """)
    st.markdown("### 4. IPC State Bridging")
    st.markdown("""
    Because multi-threading a GPU vision process alongside a vocal LLM triggers the Global Interpreter Lock (GIL) and crashes Python, we bifurcated the architecture into dual subprocesses that communicate via a localized `.tommy_state.json` bridge pipeline.
    """)

st.divider()

# --- TEAM COMPOSITION ---
st.markdown("## 🤝 The Engineering Team")
st.markdown("T.O.M.M.Y. was heavily developed and architected in conjunction by the following core members from the Department of Computer Science at Lovely Professional University:")

t1, t2, t3 = st.columns(3)

with t1:
    st.markdown("""
    <div class="team-box">
        <div class="team-name">Chirag Phogat</div>
        <p style="color:#8b949e; font-size: 0.9rem;">Lead Systems Architecture</p>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
    <div class="team-box">
        <div class="team-name">Chava Harshavardhan</div>
        <p style="color:#8b949e; font-size: 0.9rem;">Gaze Estimation & Eye Control</p>
    </div>
    """, unsafe_allow_html=True)

with t3:
    st.markdown("""
    <div class="team-box">
        <div class="team-name">Lalmalsawm Guite</div>
        <p style="color:#8b949e; font-size: 0.9rem;">Lead Researcher & Concept Ideation</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Powered by Streamlit | Engineered strictly for Offline Deployment.")
