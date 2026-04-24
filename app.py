import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(
    page_title="T.O.M.M.Y. OS",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================================
# GLOBAL CSS INJECTION (PRODUCT LAUNCH THEME)
# =========================================================================
st.markdown("""
    <style>
        .stApp {
            background-color: #050505;
            color: #e6e6e6;
            font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        
        header, #MainMenu, footer { visibility: hidden; }
        .block-container { padding-top: 1rem; max-width: 1400px; }
        
        /* Typography */
        h1, h2, h3 { font-family: 'Courier New', monospace; font-weight: 900; text-transform: uppercase; margin-bottom: 0; }
        .gradient-text {
            background: linear-gradient(90deg, #00ff41, #008f11);
            -webkit-background-clip: text;
            color: transparent;
        }
        
        /* Hero Button */
        .hero-btn-container { text-align: center; margin-top: 2rem; margin-bottom: 5rem; }
        .hero-btn {
            background: transparent;
            border: 2px solid #00ff41;
            color: #00ff41;
            padding: 15px 50px;
            font-size: 1.5rem;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            text-decoration: none;
            text-transform: uppercase;
            border-radius: 4px;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(0, 255, 65, 0.2);
            display: inline-block;
        }
        .hero-btn:hover {
            background: #00ff41;
            color: #000;
            box-shadow: 0 0 30px rgba(0, 255, 65, 0.6);
            transform: scale(1.05);
        }

        /* Cinematic Feature Section */
        .feature-section {
            padding: 80px 20px;
            margin: 40px 0;
            border-top: 1px solid rgba(0, 255, 65, 0.2);
            border-bottom: 1px solid rgba(0, 255, 65, 0.2);
            background: linear-gradient(180deg, rgba(0,255,65,0.02) 0%, rgba(0,0,0,0) 100%);
            display: flex;
            align-items: center;
        }
        .feature-title { font-size: 3rem; color: #fff; letter-spacing: 2px; }
        .feature-desc { font-size: 1.2rem; color: #8b949e; line-height: 1.8; margin-top: 20px; max-width: 600px; }

        /* Footer */
        .academic-footer {
            background: #0a0a0a;
            border-top: 2px solid #222;
            padding: 60px 20px;
            margin-top: 100px;
        }
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# HERO SECTION (THE HOOK)
# =========================================================================
# Glitch Title
st.markdown("""
    <style>
        .glitch-wrapper { display: flex; justify-content: center; align-items: center; margin-top: 5rem; }
        .glitch {
            font-size: 7rem; font-weight: 900; text-transform: uppercase; position: relative; color: #fff; letter-spacing: 10px; font-family: 'Courier New', monospace;
            text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.025em -0.05em 0 rgba(0,255,0,0.75), 0.025em 0.05em 0 rgba(0,0,255,0.75);
            animation: glitch 500ms infinite;
        }
        @keyframes glitch {
            0% { text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.05em -0.025em 0 rgba(0,255,0,0.75), -0.025em 0.05em 0 rgba(0,0,255,0.75); }
            20% { text-shadow: -0.05em -0.025em 0 rgba(255,0,0,0.75), 0.025em 0.025em 0 rgba(0,255,0,0.75), -0.05em -0.05em 0 rgba(0,0,255,0.75); }
            40% { text-shadow: 0.025em 0.05em 0 rgba(255,0,0,0.75), 0.05em 0 0 rgba(0,255,0,0.75), 0 -0.05em 0 rgba(0,0,255,0.75); }
            60% { text-shadow: -0.025em 0 0 rgba(255,0,0,0.75), -0.025em -0.025em 0 rgba(0,255,0,0.75), -0.025em -0.05em 0 rgba(0,0,255,0.75); }
            80% { text-shadow: 0.05em -0.05em 0 rgba(255,0,0,0.75), 0.025em 0.05em 0 rgba(0,255,0,0.75), -0.05em -0.025em 0 rgba(0,0,255,0.75); }
            100% { text-shadow: -0.025em 0.05em 0 rgba(255,0,0,0.75), -0.05em -0.05em 0 rgba(0,255,0,0.75), 0.025em 0 0 rgba(0,0,255,0.75); }
        }
        .sub-glitch { text-align: center; color: #00ff41; font-size: 1.2rem; letter-spacing: 4px; margin-bottom: 2rem; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00ff41; }
    </style>
    <div class="glitch-wrapper"><div class="glitch" data-text="T.O.M.M.Y.">T.O.M.M.Y.</div></div>
    <div class="sub-glitch">TELEMETRIC . OPTICAL & MULTIMODAL . MACHINE . YIELD</div>
""", unsafe_allow_html=True)

# Interactive Telemetric Canvas
components.html("""
    <canvas id="telemetricCanvas" style="width: 100%; height: 200px; display: block; margin-top: -30px;"></canvas>
    <script>
        const canvas = document.getElementById('telemetricCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = 200;
        
        let nodes = [];
        for (let i = 0; i < 60; i++) {
            nodes.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 1.5,
                vy: (Math.random() - 0.5) * 1.5,
                radius: Math.random() * 2 + 1
            });
        }
        
        function animate() {
            requestAnimationFrame(animate);
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.strokeStyle = "rgba(0, 255, 65, 0.2)";
            ctx.fillStyle = "#00ff41";
            
            for (let i = 0; i < nodes.length; i++) {
                let node = nodes[i];
                node.x += node.vx;
                node.y += node.vy;
                
                if (node.x < 0 || node.x > canvas.width) node.vx *= -1;
                if (node.y < 0 || node.y > canvas.height) node.vy *= -1;
                
                ctx.beginPath();
                ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
                ctx.fill();
                
                for (let j = i + 1; j < nodes.length; j++) {
                    let dx = nodes[j].x - node.x;
                    let dy = nodes[j].y - node.y;
                    let dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 100) {
                        ctx.beginPath();
                        ctx.moveTo(node.x, node.y);
                        ctx.lineTo(nodes[j].x, nodes[j].y);
                        ctx.stroke();
                    }
                }
            }
        }
        animate();
    </script>
""", height=200)

# Hero CTA & Live Metrics
st.markdown("""
    <div class="hero-btn-container">
        <a href="https://github.com/chiragphogat/tommy-os" target="_blank" class="hero-btn">>_ INITIALIZE DEPLOYMENT KERNEL</a>
    </div>
    
    <div style="display: flex; justify-content: center; gap: 40px; text-align: center; font-family: 'Courier New', monospace; margin-bottom: 50px;">
        <div><div style="color: #8b949e; font-size: 0.9rem;">VISION LATENCY</div><div style="color: #fff; font-size: 2.5rem; font-weight: 900;">18<span style="color:#00ff41; font-size:1.5rem;">ms</span></div></div>
        <div><div style="color: #8b949e; font-size: 0.9rem;">CLOUD APIs</div><div style="color: #fff; font-size: 2.5rem; font-weight: 900;">0<span style="color:#00ff41; font-size:1.5rem;">.0%</span></div></div>
        <div><div style="color: #8b949e; font-size: 0.9rem;">IPC BRIDGE</div><div style="color: #fff; font-size: 2.5rem; font-weight: 900;">60<span style="color:#00ff41; font-size:1.5rem;">FPS</span></div></div>
    </div>
""", unsafe_allow_html=True)


# =========================================================================
# PRODUCT FEATURE 1: THE TELEMETRIC ENGINE
# =========================================================================
st.markdown('<div class="feature-section">', unsafe_allow_html=True)
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="feature-title">THE <span class="gradient-text">TELEMETRIC</span> ENGINE.</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="feature-desc">
            We bypassed standard 2D tracking. T.O.M.M.Y. locks an invisible Euclidean grid directly to your facial structure. 
            By locking the mouse cursor directly to <b>FaceMesh Node 1 (The Nose)</b>, the engine entirely eradicates the biological micro-jitter found in hand-tracking.
            <br><br>
            <b>Hardware Triggers:</b><br>
            <span style="color:#00ff41;">></span> 1 Blink: Left Click<br>
            <span style="color:#00ff41;">></span> 2 Blinks: Right Click<br>
            <span style="color:#00ff41;">></span> 3 Blinks: Close Window<br>
            <span style="color:#00ff41;">></span> Jaw Drop: Physical Modifier Gate (Alt/Shift)
        </div>
    """, unsafe_allow_html=True)

with col2:
    # CSS Radar Scanner Animation
    components.html("""
        <style>
            .radar { position: relative; width: 300px; height: 300px; border-radius: 50%; border: 2px solid #00ff41; margin: 0 auto; overflow: hidden; box-shadow: 0 0 30px rgba(0,255,65,0.2); }
            .radar::after { content: ''; position: absolute; width: 150px; height: 150px; background: linear-gradient(45deg, rgba(0,255,65,0.8) 0%, transparent 50%); transform-origin: bottom right; top: 0; left: 0; animation: scan 2s linear infinite; }
            .radar::before { content: ''; position: absolute; width: 100%; height: 100%; background: radial-gradient(circle, transparent 40%, rgba(0,255,65,0.1) 100%); }
            .grid { position: absolute; width: 100%; height: 100%; background-image: linear-gradient(#00ff41 1px, transparent 1px), linear-gradient(90deg, #00ff41 1px, transparent 1px); background-size: 30px 30px; opacity: 0.15; }
            .target { position: absolute; width: 10px; height: 10px; background: #fff; border-radius: 50%; box-shadow: 0 0 10px #fff; top: 40%; left: 60%; animation: pulse 1s infinite; }
            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            @keyframes pulse { 0% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.5); opacity: 0.5; } 100% { transform: scale(1); opacity: 1; } }
        </style>
        <div class="radar">
            <div class="grid"></div>
            <div class="target"></div>
        </div>
    """, height=350)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# PRODUCT FEATURE 2: OFFLINE VOICE CORE
# =========================================================================
st.markdown('<div class="feature-section" style="background: #020202;">', unsafe_allow_html=True)
col3, col4 = st.columns([1, 1.2])

with col3:
    # CSS Soundwave Animation
    components.html("""
        <style>
            .wave-container { display: flex; align-items: center; justify-content: center; height: 300px; gap: 5px; }
            .bar { width: 15px; background: #00ff41; border-radius: 10px; animation: sound 0ms -800ms linear infinite alternate; box-shadow: 0 0 15px #00ff41; }
            @keyframes sound { 0% { height: 10px; opacity: 0.3; } 100% { height: 150px; opacity: 1; } }
            .bar:nth-child(1)  { animation-duration: 474ms; }
            .bar:nth-child(2)  { animation-duration: 433ms; }
            .bar:nth-child(3)  { animation-duration: 407ms; }
            .bar:nth-child(4)  { animation-duration: 458ms; }
            .bar:nth-child(5)  { animation-duration: 400ms; }
            .bar:nth-child(6)  { animation-duration: 427ms; }
            .bar:nth-child(7)  { animation-duration: 441ms; }
            .bar:nth-child(8)  { animation-duration: 419ms; }
            .bar:nth-child(9)  { animation-duration: 487ms; }
            .bar:nth-child(10) { animation-duration: 442ms; }
        </style>
        <div class="wave-container">
            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
        </div>
    """, height=350)

with col4:
    st.markdown('<div class="feature-title">DETERMINISTIC <span class="gradient-text">VOICE</span> ISOLATION.</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="feature-desc">
            LLMs are banned from the logic loop. Waiting 2,000ms for a cloud server to "generate" an API response just to mute your volume is a catastrophic failure in OS design.
            <br><br>
            T.O.M.M.Y. rips out heavy Generative AI and replaces it with strict, deterministic syntactic parsing using the <b>spaCy</b> grammar engine. It runs locally, offline, parsing human intent instantly and firing native WMI kernel commands at lightning speeds.
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# PRODUCT FEATURE 3: DEPLOYMENT TERMINAL
# =========================================================================
st.markdown('<div style="text-align:center; margin-top: 80px;"><h2 style="font-size: 2.5rem;">>_ INJECTING THE SANDBOX</h2></div>', unsafe_allow_html=True)
st.markdown("""
    <p style="text-align:center; color:#8b949e; max-width:800px; margin: 0 auto 40px auto; font-size:1.1rem;">
        Engineered to deploy cleanly without polluting your Windows PATH. 
        The <code>setup.bat</code> payload spins up an isolated <code>venv</code>, downloads all visual MediaPipe models, and hands execution off to an elevated PowerShell terminal natively.
    </p>
""", unsafe_allow_html=True)

# Fake Terminal Block
components.html("""
    <div style="background: #010409; border: 1px solid #30363d; border-radius: 8px; width: 60%; margin: 0 auto; font-family: 'Courier New', monospace; box-shadow: 0 10px 30px rgba(0,0,0,0.5); overflow: hidden;">
        <div style="background: #161b22; padding: 10px; border-bottom: 1px solid #30363d; display: flex; gap: 8px;">
            <div style="width: 12px; height: 12px; border-radius: 50%; background: #ff5f56;"></div>
            <div style="width: 12px; height: 12px; border-radius: 50%; background: #ffbd2e;"></div>
            <div style="width: 12px; height: 12px; border-radius: 50%; background: #27c93f;"></div>
        </div>
        <div style="padding: 20px; color: #fff; font-size: 1.1rem; line-height: 1.6;">
            <span style="color:#00ff41;">C:\\Windows\\System32></span> git clone https://github.com/chiragphogat/tommy-os.git<br>
            <span style="color:#00ff41;">C:\\Windows\\System32></span> cd tommy-os<br>
            <span style="color:#00ff41;">C:\\tommy-os></span> .\\setup.bat<br>
            <span style="color:#8b949e;">[+] Building Virtual Sandbox... DONE</span><br>
            <span style="color:#8b949e;">[+] Initializing spaCy Models... DONE</span><br>
            <span style="color:#8b949e;">[+] Bypassing Execution Policies... DONE</span><br>
            <span style="color:#3fb950; font-weight:bold;">PS C:\\tommy-os></span> python tommy_os.py<span style="animation: blink 1s infinite;">_</span>
        </div>
    </div>
    <style>@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }</style>
""", height=350)


# =========================================================================
# ACADEMIC FOOTER
# =========================================================================
st.markdown('<div class="academic-footer">', unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#58a6ff;'>// ACADEMIC RESOURCES</h3>", unsafe_allow_html=True)

col_f1, col_f2 = st.columns([1, 1])
with col_f1:
    st.markdown("""
        <div style="background: #161b22; border: 1px solid #30363d; padding: 30px; border-radius: 8px;">
            <h4 style="color:#fff;">A Multi-Process Architecture for Hands-Free Windows Navigation</h4>
            <p style="color:#8b949e; font-size: 0.9rem;">
                Even now, computers keep us at our desks. We made T.O.M.M.Y. to fix this. It is a native wrapper that uses a regular webcam to take over Windows. 
                By dividing the workload into separate background processes that talk through a JSON bridge, we dodged Python's GIL constraints completely.
            </p>
    """, unsafe_allow_html=True)
    try:
        with open("assets/T.O.M.M.Y_Research.pdf", "rb") as pdf_file:
            st.download_button(
                label="📥 DOWNLOAD IEEE RESEARCH MANUSCRIPT",
                data=pdf_file,
                file_name="TOMMY_Research_Paper.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except FileNotFoundError:
        st.error("⚠️ PDF Not Compiled in /assets/")
    st.markdown("</div>", unsafe_allow_html=True)

with col_f2:
    st.markdown("""
        <div style="background: #161b22; border: 1px solid #30363d; padding: 30px; border-radius: 8px; height: 100%;">
            <h4 style="color:#fff;">SYSTEM ARCHITECTS</h4>
            <p style="color:#8b949e; font-size: 0.9rem;">Engineered at Lovely Professional University.</p>
            <ul style="color:#c9d1d9; list-style-type: none; padding-left: 0;">
                <li style="margin-bottom: 10px;"><b>Chirag Phogat</b> - Lead Systems Architecture</li>
                <li style="margin-bottom: 10px;"><b>Chava Harshavardhan</b> - Gaze Estimation Math</li>
                <li style="margin-bottom: 10px;"><b>Lalmalsawm Guite</b> - Lead Researcher</li>
                <li style="margin-bottom: 10px;"><b>Kaushal Pathak</b> - Project Mentor</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; margin-top: 50px; color: #484f58; font-family: 'Courier New', monospace; font-size: 0.8rem;">
        © 2026 T.O.M.M.Y. OS PLATFORM. ALL SYSTEMS NOMINAL.
    </div>
</div>
""", unsafe_allow_html=True)
