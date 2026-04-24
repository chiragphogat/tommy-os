import streamlit as st
import base64

st.set_page_config(
    page_title="T.O.M.M.Y. OS Command Center",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for glassmorphism, glowing text, and modern tech aesthetic
st.markdown("""
    <style>
        .stApp {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Inter', sans-serif;
        }
        .css-1d391kg { background-color: #161b22; } /* Sidebar */
        h1, h2, h3 { 
            color: transparent;
            background: linear-gradient(90deg, #58a6ff, #3fb950);
            -webkit-background-clip: text;
            font-weight: 900;
        }
        h4, h5, h6 { color: #8b949e; font-weight: 700; }
        
        .metric-card {
            background: rgba(22, 27, 34, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease-in-out;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            border-color: #58a6ff;
            box-shadow: 0 8px 30px rgba(88, 166, 255, 0.2);
        }
        .metric-value {
            font-size: 2.5rem;
            font-weight: 800;
            color: #58a6ff;
            margin: 10px 0;
        }
        .metric-label {
            font-size: 0.9rem;
            color: #8b949e;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .feature-box {
            background: linear-gradient(145deg, #161b22, #0d1117);
            border-left: 4px solid #3fb950;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-right: 1px solid #30363d;
            border-top: 1px solid #30363d;
            border-bottom: 1px solid #30363d;
        }
        
        .terminal-box {
            background-color: #010409;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 15px;
            font-family: 'Courier New', Courier, monospace;
            color: #3fb950;
        }
        
        .stTabs [data-baseweb="tab-list"] { gap: 1rem; }
        .stTabs [data-baseweb="tab"] { 
            height: 50px; 
            white-space: pre-wrap; 
            border-radius: 6px; 
            color: #8b949e; 
            font-weight: 600;
            background-color: #161b22;
            border: 1px solid #30363d;
            padding: 0 20px;
        }
        .stTabs [aria-selected="true"] { 
            color: #ffffff !important; 
            background-color: #238636 !important;
            border-color: #2ea043 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## T.O.M.M.Y. OS")
    st.markdown("v3.0 - Vision-First Architecture")
    st.markdown("---")
    st.markdown("**Status:** `NATIVE KERNEL MODE`")
    st.markdown("**Cloud Dependency:** `0%`")
    st.markdown("**LLM Engine:** `BYPASSED`")
    st.markdown("---")
    st.markdown("### Engineering Team")
    st.markdown("- Chirag Phogat\n- Chava Harshavardhan\n- Lalmalsawm Guite\n- Kaushal Pathak")

st.markdown("<h1 style='text-align: center; font-size: 4rem; margin-bottom: 0;'>T.O.M.M.Y.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; font-size: 1.2rem; margin-top: 0;'>Tactile, Optical, and Multimodal Machine Yield</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🎛️ Command Center", "⚙️ Core Architecture", "📄 Academic Portal"])

# --- TAB 1: COMMAND CENTER ---
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Vision Latency</div>
            <div class="metric-value">18<span style="font-size:1rem;">ms</span></div>
            <div style="color:#3fb950; font-size:0.8rem;">▲ XNNPACK CPU Local</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Voice Pipeline</div>
            <div class="metric-value">14<span style="font-size:1rem;">ms</span></div>
            <div style="color:#3fb950; font-size:0.8rem;">▲ Porcupine Offline</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">NLP Resolution</div>
            <div class="metric-value">0<span style="font-size:1rem;">ping</span></div>
            <div style="color:#3fb950; font-size:0.8rem;">▲ Deterministic spaCy</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Cloud Hooks</div>
            <div class="metric-value" style="color:#F85149;">Zero</div>
            <div style="color:#8b949e; font-size:0.8rem;">Fully Air-Gapped</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><hr style='border-color:#30363d;'><br>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1.5, 1])
    with col_a:
        st.markdown("### 🚀 Automated Deployment Pipeline")
        st.markdown("We engineered T.O.M.M.Y. to deploy instantly without cluttering your system's global variables. Using our completely overhauled `setup.bat`, the system natively sandboxes itself.")
        
        st.markdown("""
        <div class="feature-box">
            <h4>1. Virtual Containerization</h4>
            <p style="color:#8b949e;">Automatically spins up an isolated `venv` environment. No conflicting packages.</p>
            <h4>2. Driver Injections</h4>
            <p style="color:#8b949e;">Downloads Physics Trackers (MediaPipe), Hardware Audio limits, and spaCy grammar models directly into the sandbox.</p>
            <h4>3. PowerShell Handoff</h4>
            <p style="color:#8b949e;">Spawns an elevated green PowerShell, pre-fills the boot command, and waits for a single Enter keystroke to seize OS control.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("### 💻 Quick Start Terminal")
        st.markdown("""
        <div class="terminal-box">
            > git clone https://github.com/chiragphogat/tommy-os.git<br>
            > cd tommy-os<br>
            > .\setup.bat<br>
            <br>
            <span style="color:#8b949e;"># Wait for PowerShell handoff...</span><br>
            > python tommy_os.py
        </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 Make sure to inject your free `PORCUPINE_ACCESS_KEY` into the hidden `.env` file first!")

# --- TAB 2: CORE ARCHITECTURE ---
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🧠 The 12-Module Substructure")
    st.markdown("T.O.M.M.Y. isn't a web wrapper. It's a decoupled Inter-Process Communication (IPC) operating system that hijacks Windows. By forcing audio and video execution onto physically distinct CPU cores via JSON states, we eradicated GIL bottlenecks entirely.")
    
    c1, c2 = st.columns(2)
    with c1:
        with st.expander("👁️ Vision-First Hardware Tracking", expanded=True):
            st.markdown("""
            **Mode-less Ocular Command Mapping:**
            Instead of standard hand tracking alone, the system decouples spatial X/Y movement to your **Nose Tip (FaceMesh Node 1)** to completely eliminate micro-jitter.
            
            - **1 Blink:** Left Click
            - **2 Blinks:** Right Click
            - **3 Blinks:** Close Tab (`Ctrl+W`)
            - **Head Roll:** Media Next/Prev Track
            
            *Complex macros are securely guarded behind a physical Jaw-Drop (MAR) modifier, ensuring zero accidental actuations.*
            """)
            
        with st.expander("⚡ Latency & Execution Mathematics", expanded=False):
            st.markdown("""
            We deliberately abandoned CUDA GPU acceleration. Shoving tiny 480p matrix arrays across the physical PCIe motherboard bus was too slow (45ms).
            By keeping execution strictly inside the CPU's local XNNPACK cache, we achieve continuous 18ms bounding box mathematics.
            """)
            st.bar_chart({"Latency (ms)": {"PCIe CUDA Transfer": 45, "Local CPU XNNPACK": 18}}, color="#58a6ff")

    with c2:
        with st.expander("🗣️ Deterministic NLP Engine", expanded=True):
            st.markdown("""
            **LLMs Are Banned.**
            A desktop OS cannot wait 2000ms for a cloud server to "generate" an API response just to mute the volume. 
            
            We ripped out heavy Generative AI and replaced it with strict, deterministic syntactic parsing using **spaCy**. It identifies hard Intent logic offline and fires WMI kernel requests natively. Voice is purely a fallback when vision is disabled.
            """)
            
        with st.expander("🧩 IPC Memory Isolation", expanded=False):
            st.markdown("""
            Python's Global Interpreter Lock (GIL) freezes the camera feed if a microphone text-to-speech module starts executing.
            
            T.O.M.M.Y. bypasses this by launching `vision_engine.py` and `voice_engine.py` as fully detached `subprocess` daemons. They never share memory, communicating securely across a `.tommy_state.json` bridge at 60 FPS.
            """)

# --- TAB 3: ACADEMIC PORTAL ---
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📄 Research & Documentation")
    
    st.markdown("""
    <div class="feature-box" style="border-left-color: #58a6ff;">
        <h4>T.O.M.M.Y.: A Multi-Process Architecture for Hands-Free Windows Navigation</h4>
        <p style="color:#8b949e; font-style: italic;">Abstract — Even now, computers keep us at our desks with keyboards and mice. Voice assistants are available, but if you ask one to drag and drop a file, it will not work. We made T.O.M.M.Y. to fix this. It is a hands-free wrapper that uses a regular webcam and microphone to take over Windows. We divided everything into separate background processes that talked to each other through a JSON bridge, dodging Python's GIL. The final build runs perfectly at 60 FPS, with interactions occurring natively in under 20 milliseconds.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # PDF Download
    col_dl, col_blank = st.columns([1, 2])
    with col_dl:
        try:
            with open("assets/T.O.M.M.Y_Research.pdf", "rb") as pdf_file:
                st.download_button(
                    label="📥 Download Official IEEE Paper (PDF)",
                    data=pdf_file,
                    file_name="TOMMY_Research_Paper.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        except FileNotFoundError:
            st.error("⚠️ `T.O.M.M.Y_Research.pdf` not found in `assets/`. Please compile the LaTeX to deploy.")

    st.markdown("<br><hr style='border-color:#30363d;'><br>", unsafe_allow_html=True)
    st.markdown("#### The Engineering Team")
    st.markdown("<p style='color:#8b949e;'>Engineered at Lovely Professional University</p>", unsafe_allow_html=True)
    
    tc1, tc2, tc3, tc4 = st.columns(4)
    with tc1:
        st.markdown("**Chirag Phogat**<br><span style='color:#8b949e; font-size:0.9rem;'>Lead Systems Architecture</span>", unsafe_allow_html=True)
    with tc2:
        st.markdown("**Chava Harshavardhan**<br><span style='color:#8b949e; font-size:0.9rem;'>Gaze Estimation</span>", unsafe_allow_html=True)
    with tc3:
        st.markdown("**Lalmalsawm Guite**<br><span style='color:#8b949e; font-size:0.9rem;'>Lead Researcher</span>", unsafe_allow_html=True)
    with tc4:
        st.markdown("**Kaushal Pathak**<br><span style='color:#8b949e; font-size:0.9rem;'>Project Guide & Mentor</span>", unsafe_allow_html=True)
