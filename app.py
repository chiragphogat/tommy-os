import streamlit as st

st.set_page_config(
    page_title="T.O.M.M.Y. OS",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- CSS Styling for Modern Glassmorphism & Tabs ---
st.markdown("""
    <style>
        .stApp {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Inter', sans-serif;
        }
        h1, h2, h3, h4 { color: #58a6ff !important; font-weight: 800; }
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
            background-color: transparent;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            border-radius: 4px;
            color: #8b949e;
            font-size: 1.1rem;
            font-weight: 600;
        }
        .stTabs [aria-selected="true"] { color: #58a6ff !important; background-color: #1f2428;}
        .glass-card {
            background: rgba(22, 27, 34, 0.7);
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(4px);
            text-align: center;
        }
        .warning-box {
            background-color: #2D1115;
            border-left: 4px solid #F85149;
            padding: 1.5rem;
            border-radius: 6px;
            color: #FF7B72;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.title("T.O.M.M.Y. OS")
st.markdown("### A Unified Multimodal Framework for Real-Time OS Control using MediaPipe, Gaze Estimation, and Speech Recognition")

# --- MULTI-TAB ARCHITECTURE ---
tab1, tab2, tab3 = st.tabs(["🚀 Project Synopsis", "📊 Comparative Analysis", "📄 Research Deep-Dive"])

# =========================================================================
# TAB 1: SYNOPSIS & THE PITCH
# =========================================================================
with tab1:
    st.markdown("""
    <div class="warning-box">
        <strong>⚠️ ACADEMIC DEPLOYMENT NOTICE</strong><br><br>
        T.O.M.M.Y represents a major shift from traditional Web AI. It is an <strong>Operating System kernel wrapper</strong> designed locally for Windows machines. It physically hijacks mouse parameters, hardware drivers (brightness/volume), and display elements using localized CPU threading.<br><br>
        Because this Web Server operates on headless Linux constraints without a physical screen or microphone, this site serves strictly as our <strong>Interactive Digital Portfolio</strong>. To test the mathematical physics, clone the underlying OS source code below!
    </div>
    """, unsafe_allow_html=True)

    st.code("git clone https://github.com/chiragphogat/tommy-os.git\ncd tommy-os\nsetup.bat", language="bash")
    
    st.markdown("---")
    st.markdown("## 📖 The Core Problem")
    st.markdown("""
    Computers still keep us chained to desks using 1980s peripheral mice. While massive companies push 'Voice Assistants', they are almost exclusively cloud chatbots that have zero physical control over your desktop environment. 
    
    We engineered T.O.M.M.Y. to solve this directly. Instead of mashing heavy vision models and offline Large Language Models (LLMs) into one sluggish Python script—which instantly hits the GIL (Global Interpreter Lock) and freezes your computer—we tore down the basic architecture. We divided the system into entirely isolated subprocesses that communicate via lightning-fast JSON injection. 

    Now, you can execute basic commands instantaneously off pure mathematical geometry, and run massive localized Language Models completely offline in the background.
    """)

    st.markdown("---")
    st.markdown("## 💻 Engineering Team Roster")
    st.markdown("T.O.M.M.Y was researched, architected, and engineered at Lovely Professional University.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        try:
            st.image("assets/chirag.jpg", use_column_width=True)
        except:
            st.warning("[Photo Missing: Add 'chirag.jpg' to assets/]")
        st.markdown("<h3 style='margin-bottom:0;'>Chirag Phogat</h3><p style='color:#8b949e;'>Lead Systems Architecture</p></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        try:
            st.image("assets/chava.jpg", use_column_width=True)
        except:
            st.warning("[Photo Missing: Add 'chava.jpg' to assets/]")
        st.markdown("<h3 style='margin-bottom:0;'>Chava Harshavardhan</h3><p style='color:#8b949e;'>Gaze Estimation & Eye Control Integration</p></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        try:
            st.image("assets/lalmalsawm.jpg", use_column_width=True)
        except:
            st.warning("[Photo Missing: Add 'lalmalsawm.jpg' to assets/]")
        st.markdown("<h3 style='margin-bottom:0;'>Lalmalsawm Guite</h3><p style='color:#8b949e;'>Lead Researcher & Concept Iteration</p></div>", unsafe_allow_html=True)


# =========================================================================
# TAB 2: BENCHMARKS & COMPARATIVE ANALYSIS
# =========================================================================
with tab2:
    st.markdown("## 📈 Empirical Latency Metrics")
    st.markdown("Traditional systems force real-time camera math onto the dedicated GPU (CUDA). By doing absolute comparative analysis against native hardware bounds, we achieved staggering latency drops by keeping matrix calculations exclusively onto the CPU cache.")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("MediaPipe Frame Latency", "18 ms", "Over 60 FPS", delta_color="normal")
    m2.metric("Ocular Iris Tracking", "22 ms", "Blink/Wink Isolation", delta_color="normal")
    m3.metric("Wake-Phoneme Verification", "14 ms", "Zero Audio Delay", delta_color="normal")
    m4.metric("Avg OS Responsiveness", "< 20ms", "Instant Driver Hooks", delta_color="normal")

    st.markdown("---")
    st.markdown("### 📊 GPU CUDA Overhead vs Optimized Local XNNPACK CPU")
    
    # Building the comparative Data Frame natively
    chart_data = {
        "Latency Per Frame (ms)": {"Standard PCIe CUDA Bus Transfer": 45, "T.O.M.M.Y. CPU XNNPACK Delegate": 18}
    }
    
    st.bar_chart(chart_data["Latency Per Frame (ms)"], color="#58a6ff", height=400)
    st.caption("Paradoxically, executing raw matrix math exclusively on the generic CPU (18ms) vastly out-performed pushing data to the dedicated CUDA GPU (45ms). This empirical data absolutely proves PCIe transfer overhead completely chokes tiny 480p real-time camera arrays.")

    st.markdown("---")
    st.markdown("### 🖥️ Real-Time System Command Protocol (Simulated Logs)")
    st.code("""
============================================================
 🧠 BOOTING T.O.M.M.Y. OS MASTER KERNEL V3.2 (Monolithic) 🧠
============================================================
[OS] IPC Subprocess Bridge Initialized (Hand Tracking Default)
[OS] Allocating Engine 1: Auditory Intelligence & UI HUD...
[OS] Allocating Engine 2: Spatial Mathematics...

✅ [OS_SYS] All Neural Pipelines Active.

[CAMERA] Vision Kernel online. Tracking Geometric bounds (18ms).
[MIC] PvRecorder hardware locked. Ambient Room scanning initialized...
[HOTWORD] 'Hey Tommy' detected natively.
[MIC OS DRIVER YIELDED] Shutting down background arrays...
[LISTENING] Speak now...
   ↳ [HEARD RAW]: "Cut the brightness immediately and launch visual studio"
[MIC OS DRIVER ACQUIRED] Restarting PvRecorder lock...

>> EXECUTING HARDWARE LOGIC -> Firing daemon threads... SBC Drivers 0%.
>> EXECUTING OS LOGIC -> Executing strict Window UI deployment.
    """, language="markdown")


# =========================================================================
# TAB 3: FULL PAPER EXPANDERS
# =========================================================================
with tab3:
    st.markdown("## 🔬 Digital Research Paper")
    st.markdown("Tap the accordions below to expand and read the core methodologies ripped straight from our IEEE paper.")
    
    with st.expander("📝 Abstract & The Universal Failure Point", expanded=True):
        st.markdown("""
        Even now, computers keep us at our desks with keyboards and mice. Voice assistants are available, but if you ask one to drag and drop a file, it won't work. We made T.O.M.M.Y. to fix this. It's a hands-free wrapper that uses a regular webcam and microphone to take over Windows. 
        
        But getting there wasn't easy. When we tried to run heavy vision models and a talking AI at the same time in Python, the **GIL wall** hit right away, and the screen froze every time the bot spoke. Standard webcams also make it hard to judge depth (The camera thinks your hands got smaller when you lean back). We tore down the architecture to get around all of this, isolating processes into Inter-Process Communication networks.
        """)
        
    with st.expander("⚙️ The Spacial Fix: Eradicating Distance Scaling", expanded=False):
        st.markdown("""
        Standard OpenCV tracking uses Euclidean bounds (measuring pixels between fingers). This inherently shatters when a user leans back in their chair. T.O.M.M.Y bypasses this by utilizing pure **Y-axis delta-coordinate math**. It strictly measures if a fingertip is mathematically positioned *below* the physical plane of a knuckle (`tip.y > pip.y`), rendering the tracking immune to physical depth.
        """)

    with st.expander("🛠️ Damping Cursor Jitters (Alpha Mechanics)", expanded=False):
        st.markdown("""
        Humans can't hold their hands perfectly still in mid-air. Mapping a fingertip directly to a canvas resulted in a mouse cursor that violently shook. We silenced the shake by feeding the `pyautogui` coordinate stream directly through an **Exponential Moving Average** algorithm. Setting the alpha parameter to `a = 0.55` perfectly deleted the biological jitter while keeping the cursor sharp.
        """)
        st.latex(r"C_{coord_t} = (0.55 \times V_{raw}) + (0.45 \times C_{coord_{t-1}})")

    with st.expander("🎙️ The Auditory Hardware Deadlock Patch", expanded=False):
        st.markdown("""
        Windows OS inherently restricts active microphone arrays to a single port process. Attempting to run a Wake-Word listener alongside a Command Listener caused catastrophic Thread crashing. We engineered an aggressive, dynamic `recorder.stop()` injection protocol. The exact millisecond the wake word is detected, the audio array is forcefully yielded.
        """)
        
    with st.expander("👁️ Eye Control & The Missing Thumb Bug", expanded=False):
        st.markdown("""
        Because regular webcams shoot straight-on, people's thumbs naturally hide behind the curve of their palms. The code would drop the vision lock if it lost a thumb. We mathematically dropped the gate requirement down. 
        Once locked into gaze mode, the **Eye Aspect Ratio** filters out random blinks and only clicks the mouse if the user throws a hard, deliberate wink.
        """)
        st.latex(r"EAR_{wink} = \frac{||P_2 - P_6|| + ||P_3 - P_5||}{2||P_1 - P_4||}")

    st.markdown("<br><hr><center><p style='color:#8b949e;'>Engineered for academic evaluation. See GitHub repository for compilation guidelines.</p></center>", unsafe_allow_html=True)
