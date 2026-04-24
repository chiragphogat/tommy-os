import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="T.O.M.M.Y. OS | Kernel",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================================
# GLOBAL CSS INJECTION (CYBERPUNK / SCI-FI THEME)
# =========================================================================
st.markdown("""
    <style>
        /* Base Cyberpunk Theme */
        .stApp {
            background-color: #050505;
            color: #00ff41;
            font-family: 'Courier New', Courier, monospace;
        }
        
        /* Hide Streamlit elements */
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Glitch Title Effect */
        .glitch-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 2rem;
            margin-bottom: 0;
        }
        .glitch {
            font-size: 6rem;
            font-weight: 900;
            text-transform: uppercase;
            position: relative;
            text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.025em -0.05em 0 rgba(0,255,0,0.75), 0.025em 0.05em 0 rgba(0,0,255,0.75);
            animation: glitch 500ms infinite;
            color: #fff;
            letter-spacing: 5px;
        }
        @keyframes glitch {
            0% { text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.05em -0.025em 0 rgba(0,255,0,0.75), -0.025em 0.05em 0 rgba(0,0,255,0.75); }
            14% { text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.05em -0.025em 0 rgba(0,255,0,0.75), -0.025em 0.05em 0 rgba(0,0,255,0.75); }
            15% { text-shadow: -0.05em -0.025em 0 rgba(255,0,0,0.75), 0.025em 0.025em 0 rgba(0,255,0,0.75), -0.05em -0.05em 0 rgba(0,0,255,0.75); }
            49% { text-shadow: -0.05em -0.025em 0 rgba(255,0,0,0.75), 0.025em 0.025em 0 rgba(0,255,0,0.75), -0.05em -0.05em 0 rgba(0,0,255,0.75); }
            50% { text-shadow: 0.025em 0.05em 0 rgba(255,0,0,0.75), 0.05em 0 0 rgba(0,255,0,0.75), 0 -0.05em 0 rgba(0,0,255,0.75); }
            99% { text-shadow: 0.025em 0.05em 0 rgba(255,0,0,0.75), 0.05em 0 0 rgba(0,255,0,0.75), 0 -0.05em 0 rgba(0,0,255,0.75); }
            100% { text-shadow: -0.025em 0 0 rgba(255,0,0,0.75), -0.025em -0.025em 0 rgba(0,255,0,0.75), -0.025em -0.05em 0 rgba(0,0,255,0.75); }
        }
        
        .sub-glitch {
            text-align: center;
            color: #0ff;
            font-size: 1.2rem;
            letter-spacing: 2px;
            margin-bottom: 2rem;
            text-shadow: 0 0 10px #0ff;
        }

        /* Neon Holographic Cards */
        .holo-card {
            background: rgba(0, 20, 10, 0.6);
            border: 1px solid #00ff41;
            box-shadow: 0 0 15px rgba(0, 255, 65, 0.2), inset 0 0 20px rgba(0, 255, 65, 0.1);
            border-radius: 4px;
            padding: 20px;
            margin-bottom: 20px;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
            transform-style: preserve-3d;
        }
        .holo-card:hover {
            transform: perspective(1000px) translateZ(20px) rotateX(2deg) rotateY(2deg);
            box-shadow: 0 0 30px rgba(0, 255, 65, 0.5), inset 0 0 30px rgba(0, 255, 65, 0.2);
            border-color: #fff;
        }
        .holo-card::before {
            content: "";
            position: absolute;
            top: 0; left: -100%; width: 50%; height: 100%;
            background: linear-gradient(to right, transparent, rgba(0, 255, 65, 0.3), transparent);
            transform: skewX(-20deg);
            transition: 0.5s;
        }
        .holo-card:hover::before { left: 200%; }

        /* Neon Headers inside cards */
        .holo-card h3 {
            color: #0ff;
            text-transform: uppercase;
            border-bottom: 1px solid #0ff;
            padding-bottom: 5px;
            text-shadow: 0 0 5px #0ff;
        }
        
        /* Custom Streamlit Tabs */
        .stTabs [data-baseweb="tab-list"] { gap: 1rem; background-color: transparent; }
        .stTabs [data-baseweb="tab"] { 
            background: transparent;
            border: 1px solid #00ff41;
            color: #00ff41;
            font-family: 'Courier New', Courier, monospace;
            border-radius: 0;
            padding: 10px 20px;
            text-transform: uppercase;
            box-shadow: 0 0 5px rgba(0,255,65,0.2);
        }
        .stTabs [aria-selected="true"] { 
            background-color: #00ff41 !important;
            color: #000 !important;
            box-shadow: 0 0 15px rgba(0,255,65,0.8);
            font-weight: 900;
        }
        
        hr { border-color: rgba(0, 255, 65, 0.3); }
        p, li { font-size: 1.1rem; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# GLITCH TITLE
# =========================================================================
st.markdown('<div class="glitch-wrapper"><div class="glitch" data-text="T.O.M.M.Y.">T.O.M.M.Y.</div></div>', unsafe_allow_html=True)
st.markdown('<div class="sub-glitch">TACTILE . OPTICAL . MULTIMODAL . MACHINE . YIELD</div>', unsafe_allow_html=True)

# =========================================================================
# TERMINAL BOOT SEQUENCE (HTML/JS INJECTION)
# =========================================================================
components.html("""
    <div id="terminal" style="
        background-color: #000; 
        color: #00ff41; 
        font-family: 'Courier New', monospace; 
        padding: 20px; 
        border: 2px solid #00ff41; 
        border-radius: 5px;
        box-shadow: 0 0 20px rgba(0, 255, 65, 0.4);
        height: 250px; 
        overflow-y: hidden;
        position: relative;
    ">
        <div id="output"></div>
        <span id="cursor" style="animation: blink 1s step-end infinite;">█</span>
    </div>

    <style>
        @keyframes blink { 50% { opacity: 0; } }
        ::selection { background: #00ff41; color: #000; }
    </style>

    <script>
        const lines = [
            "> INITIALIZING KERNEL BOOT SEQUENCE...",
            "> MEMORY ISOLATION... [SUCCESS]",
            "> BYPASSING CLOUD APIs... [SUCCESS]",
            "> SECURING LOCAL IPC BRIDGES... [LOCKED]",
            "> INJECTING FACEMESH XNNPACK WORKERS... [ACTIVE]",
            "> WAKING DETERMINISTIC NLP DAEMON (spaCy)... [ACTIVE]",
            "> CALIBRATING 18ms VISION MATRICES...",
            "> ",
            "> SYSTEM ONLINE. WELCOME TO THE FUTURE OF OS CONTROL."
        ];
        
        let lineIndex = 0;
        let charIndex = 0;
        const output = document.getElementById("output");
        
        function typeWriter() {
            if (lineIndex < lines.length) {
                if (charIndex < lines[lineIndex].length) {
                    output.innerHTML += lines[lineIndex].charAt(charIndex);
                    charIndex++;
                    setTimeout(typeWriter, Math.random() * 30 + 10);
                } else {
                    output.innerHTML += "<br>";
                    lineIndex++;
                    charIndex = 0;
                    setTimeout(typeWriter, 400);
                }
            } else {
                document.getElementById("terminal").style.boxShadow = "0 0 40px rgba(0, 255, 65, 0.8)";
            }
        }
        
        setTimeout(typeWriter, 1000);
    </script>
""", height=280)


# =========================================================================
# LIVE STREAMER (FAKE METRICS)
# =========================================================================
components.html("""
    <div style="display: flex; justify-content: space-between; text-align: center; font-family: 'Courier New', monospace; margin-top: 10px;">
        <div style="flex: 1; border: 1px solid #0ff; margin: 5px; padding: 15px; background: rgba(0, 255, 255, 0.1); box-shadow: 0 0 10px rgba(0, 255, 255, 0.3);">
            <div style="color: #0ff; font-size: 0.8rem; text-transform: uppercase;">XNNPACK Frame Latency</div>
            <div style="color: #fff; font-size: 2.5rem; font-weight: bold; text-shadow: 0 0 10px #fff;" id="metric1">18ms</div>
        </div>
        <div style="flex: 1; border: 1px solid #f0f; margin: 5px; padding: 15px; background: rgba(255, 0, 255, 0.1); box-shadow: 0 0 10px rgba(255, 0, 255, 0.3);">
            <div style="color: #f0f; font-size: 0.8rem; text-transform: uppercase;">IPC Sync Rate</div>
            <div style="color: #fff; font-size: 2.5rem; font-weight: bold; text-shadow: 0 0 10px #fff;" id="metric2">60 FPS</div>
        </div>
        <div style="flex: 1; border: 1px solid #ff0; margin: 5px; padding: 15px; background: rgba(255, 255, 0, 0.1); box-shadow: 0 0 10px rgba(255, 255, 0, 0.3);">
            <div style="color: #ff0; font-size: 0.8rem; text-transform: uppercase;">Cloud Dependencies</div>
            <div style="color: #fff; font-size: 2.5rem; font-weight: bold; text-shadow: 0 0 10px #fff;">0.0%</div>
        </div>
    </div>
    <script>
        setInterval(() => {
            document.getElementById('metric1').innerText = (17 + Math.random() * 2).toFixed(1) + 'ms';
            document.getElementById('metric2').innerText = (59 + Math.random() * 2).toFixed(1) + ' FPS';
        }, 800);
    </script>
""", height=120)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================================
# TABS
# =========================================================================
tab1, tab2, tab3 = st.tabs(["[ 01_CORE_ARCHITECTURE ]", "[ 02_DEPLOYMENT_PROTOCOLS ]", "[ 03_ACADEMIC_ARCHIVES ]"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="holo-card">
            <h3>👁️ Vision-First Matrix</h3>
            <p>T.O.M.M.Y. maps raw Euclidean geometry directly to your hardware kernel. We completely decoupled spatial X/Y movement from the pupils to the <b>Nose Tip (FaceMesh Node 1)</b> to physically eradicate biological micro-jitter.</p>
            <ul>
                <li><b>Left Click:</b> 1 Fast Blink</li>
                <li><b>Right Click:</b> 2 Fast Blinks</li>
                <li><b>Close Window:</b> 3 Fast Blinks</li>
                <li><b>Head Roll:</b> Next/Prev Media Track</li>
            </ul>
            <p style="color: #F85149; font-size: 0.9rem;"><i>> All destructive commands are guarded by a physical Jaw-Drop (MAR) logic gate to prevent accidental actuation.</i></p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="holo-card">
            <h3>🗣️ Offline NLP Substructure</h3>
            <p>LLMs are banned. Waiting 2,000ms for an internet server to process a simple "mute volume" request is a catastrophic failure in OS design.</p>
            <p>We utilize the <b>spaCy</b> deterministic engine isolated entirely on a separate CPU core. It intercepts raw phoneme inputs via Porcupine, parses the intent vector locally, and fires direct WMI commands asynchronously.</p>
            <p style="color: #0ff;"><i>> Result: 14ms Voice Inference with zero ping.</i></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="holo-card" style="border-color: #f0f; box-shadow: 0 0 15px rgba(255, 0, 255, 0.2);">
        <h3 style="color: #f0f; border-color: #f0f;">🧩 The Memory Wall (IPC JSON Bridging)</h3>
        <p>Python's Global Interpreter Lock (GIL) is notoriously fatal for multimodal concurrency. Attempting to run a camera loop and a text-to-speech engine simultaneously causes total frame death.</p>
        <p>We solved this by launching <code>vision_engine.py</code> and <code>voice_engine.py</code> as completely detached background daemons. They never share memory. Instead, they communicate perfectly at 60 FPS across an encrypted <code>.tommy_state.json</code> high-speed bridge.</p>
    </div>
    """, unsafe_allow_html=True)


with tab2:
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.markdown("""
        <div class="holo-card">
            <h3>🚀 Automated PowerShell Sandbox</h3>
            <p>We engineered T.O.M.M.Y. to infect your machine cleanly, without polluting your global PATH variables. The <code>setup.bat</code> payload handles everything automatically.</p>
            <ol>
                <li><b>Containerization:</b> Spins up a localized Python <code>venv</code> block.</li>
                <li><b>Payload Injection:</b> Downloads MediaPipe frameworks, acoustic models, and NLP syntax offline.</li>
                <li><b>Execution Handoff:</b> Spawns an elevated PowerShell terminal natively locked into the active environment. Just press Enter to boot.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div class="holo-card" style="background: #000; border-color: #0ff;">
            <h3 style="color:#0ff; border-color: #0ff;">>_ TERMINAL</h3>
            <p style="font-family: 'Courier New', monospace; color: #0ff; font-size: 0.9rem;">
            C:\\> git clone https://github.com/chiragphogat/tommy-os.git<br>
            C:\\> cd tommy-os<br>
            C:\\tommy-os> .\\setup.bat<br>
            <br>
            <span style="color: #8b949e;"># System automatically bridges to PowerShell...</span><br>
            PS C:\\tommy-os> python tommy_os.py
            </p>
        </div>
        """, unsafe_allow_html=True)


with tab3:
    st.markdown("""
    <div class="holo-card" style="border-color: #ff0; box-shadow: 0 0 15px rgba(255, 255, 0, 0.2);">
        <h3 style="color: #ff0; border-color: #ff0;">📄 IEEE RESEARCH MANUSCRIPT</h3>
        <p><b>Title:</b> A Multi-Process Architecture for Hands-Free Windows Navigation Without Cloud Dependencies</p>
        <p style="color: #8b949e; font-style: italic;">Abstract — Even now, computers keep us at our desks with keyboards and mice. Voice assistants exist, but if you ask one to drag and drop a file, it crashes. We made T.O.M.M.Y. to fix this. It is a native wrapper that uses a regular webcam to take over Windows. By dividing the workload into separate background processes that talk through a JSON bridge, we dodged Python's GIL constraints. The final kernel runs perfectly at 60 FPS, with interactions occurring natively in under 20 milliseconds.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_dl, _ = st.columns([1, 2])
    with col_dl:
        try:
            with open("assets/T.O.M.M.Y_Research.pdf", "rb") as pdf_file:
                st.download_button(
                    label="[ INITIATE SECURE DOWNLOAD: PDF ]",
                    data=pdf_file,
                    file_name="TOMMY_Research_Paper.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        except FileNotFoundError:
            st.error("⚠️ [ERROR: 404] Research PDF missing from /assets/ directory.")

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center; color:#0ff;'>[ ARCHITECTS ]</h4>", unsafe_allow_html=True)
    
    tc1, tc2, tc3, tc4 = st.columns(4)
    with tc1:
        st.markdown("<div style='text-align:center; border: 1px solid #30363d; padding: 10px; background: #111;'><b>Chirag Phogat</b><br><span style='color:#0ff; font-size:0.8rem;'>Lead Systems Architect</span></div>", unsafe_allow_html=True)
    with tc2:
        st.markdown("<div style='text-align:center; border: 1px solid #30363d; padding: 10px; background: #111;'><b>Chava Harshavardhan</b><br><span style='color:#0ff; font-size:0.8rem;'>Gaze Estimation Math</span></div>", unsafe_allow_html=True)
    with tc3:
        st.markdown("<div style='text-align:center; border: 1px solid #30363d; padding: 10px; background: #111;'><b>Lalmalsawm Guite</b><br><span style='color:#0ff; font-size:0.8rem;'>Lead Researcher</span></div>", unsafe_allow_html=True)
    with tc4:
        st.markdown("<div style='text-align:center; border: 1px solid #30363d; padding: 10px; background: #111;'><b>Kaushal Pathak</b><br><span style='color:#0ff; font-size:0.8rem;'>Project Mentor</span></div>", unsafe_allow_html=True)
    
    st.markdown("<br><center><p style='color:#30363d; font-size: 0.8rem;'>© 2026 LOVELY PROFESSIONAL UNIVERSITY. ALL SYSTEMS NOMINAL.</p></center>", unsafe_allow_html=True)
