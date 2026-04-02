import streamlit as st
import base64

# --- Must be the first Streamlit command ---
st.set_page_config(
    page_title="T.O.M.M.Y. OS",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- CSS Styling for that "Developer Log / Hacking" aesthetic ---
st.markdown("""
    <style>
        .stApp {
            background-color: #0E1117;
            color: #C9D1D9;
            font-family: 'Courier New', Courier, monospace;
        }
        h1, h2, h3 {
            color: #58A6FF;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 800;
        }
        .highlight-box {
            background-color: #161B22;
            border-left: 4px solid #58A6FF;
            padding: 1.5rem;
            border-radius: 4px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        .warning-box {
            background-color: #2D1115;
            border-left: 4px solid #F85149;
            padding: 1.5rem;
            border-radius: 4px;
            color: #FF7B72;
            margin-bottom: 2rem;
            font-family: 'Segoe UI', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.title("T.O.M.M.Y.")
st.markdown("### A Multi-Process Architecture for Hands-Free Windows Navigation Without Cloud Dependencies")

st.markdown("""
<div class="warning-box">
    <strong>⚠️ ACADEMIC ARCHITECTURE NOTICE: WHY THIS IS NOT A "WEB APP"</strong><br><br>
    Most Python projects deployed to Streamlit or HuggingFace revolve around Data Science or Web APIs. 
    T.O.M.M.Y is vastly different: It is a <em>monolithic Operating System Kernel wrapper</em>. <br><br>
    It is explicitly engineered to bypass the mouse, adjust literal hardware settings (Volume/Brightness), and directly control active local GUI window states using local Webcams and Microphones. 
    Because Streamlit Cloud operates inside remote, headless Linux containers without physical monitor displays, webcams, or speakers, <strong>T.O.M.M.Y. cannot mathematically run "in the cloud"</strong>. <br><br>
    To evaluate this project, you <strong>must</strong> clone the GitHub repository and execute it natively on a local Windows machine. 
</div>
""", unsafe_allow_html=True)

# --- GITHUB CLONE SECTION ---
st.markdown("## 📥 Core Source Code (Evaluate Here)")
st.code("git clone https://github.com/chiragphogat/tommy-os.git\ncd tommy-os\nsetup.bat", language="bash")
st.markdown("[🔗 **Open Full GitHub Repository**](https://github.com/chiragphogat/tommy-os)")

# --- ABSTRACT SECTION ---
st.markdown("---")
st.markdown("## 📄 Research Abstract")

st.markdown("""
<div class="highlight-box">
Traditional Human-Computer Interaction (HCI) is predominantly anchored to physical peripherals (keyboards, mice), inherently restricting operational mobility and accessibility. While modern Voice Assistants mitigate interaction friction, they rely heavily on cloud-hosted Large Language Models (LLMs), subjecting basic local OS execution to network latency and privacy degradation.<br><br>
This project introduces <strong>T.O.M.M.Y.</strong>, a localized, multi-process architecture engineered natively for Windows to achieve total, hands-free hardware manipulation. The architecture bifurcates environmental processing into two concurrent engines:
<ul>
    <li><strong>The Vision Engine:</strong> A geometrical spatial tracker executing Y-axis coordinate mathematics on human digits to emulate cursor manipulation, screen scrolling, and hardware dimming.</li>
    <li><strong>The Voice Engine:</strong> A zero-latency verbal parser that interfaces directly with Windows OS drivers, fortified with dynamic microphone-yielding locks to prevent IO deadlocks.</li>
</ul>
Crucially, T.O.M.M.Y. decouples OS control from neural processing. Standard commands execute natively via low-level Python scripts in ~18ms. Only highly context-dependent tasks—such as UI Vision parsing or web summarization—dispatch parallel requests to localized 4-bit neural payloads (Ollama/Moondream), proving that heavy localized HCI can function robustly without external cloud compute.
</div>
""", unsafe_allow_html=True)

# --- TECHNICAL INNOVATIONS ---
st.markdown("---")
st.markdown("## 🧠 Core Engineering Achievements")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 1. The Y-Axis Spatial Fix")
    st.markdown("""
    Standard OpenCV hand tracking uses Euclidean bounding boxes on pixel distances to detect closed fists or bent fingers. This inherently failed when users physically leaned back in their chairs (the hand shrinks on camera).
    T.O.M.M.Y utilizes sheer **Y-axis delta-math**, checking only if the absolute vertical coordinate of the fingertip sits natively *below* the vertical coordinate of the primary knuckle. It perfectly solves distance scaling.
    """)

with col2:
    st.markdown("### 2. Audio Deadlock Prevention")
    st.markdown("""
    Windows restricts the microphone driver to a single listening process. In dual-listener systems (A Wake-Word listener actively hunting for "Hey Tommy" alongside a Command Listener), traditional multi-threading causes catastrophic driver crashing.
    We engineered aggressive `recorder.stop()` pipeline hooks immediately upon wake-word detection, instantly yielding the hardware layer to the Command Listener without crashing.
    """)

st.markdown("---")
st.markdown("## 🖥️ System Requirements")
st.markdown("""
- **OS:** Windows 10/11
- **Brain:** Local installation of Ollama (`llama3:8b` & `moondream`)
- **IO:** Standard USB Webcam & Microphone
""")

st.info("Project engineered by Chirag Phogat. Deployed solely as an Architectural Summary for Evaluation.")
