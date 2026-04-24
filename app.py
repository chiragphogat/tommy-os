import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="T.O.M.M.Y. OS",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================================
# GLOBAL CSS INJECTION (CINEMATIC SCROLL)
# =========================================================================
st.markdown("""
    <style>
        /* Base Cyberpunk Theme */
        .stApp {
            background-color: #020202;
            color: #e6e6e6;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        
        header, #MainMenu, footer { visibility: hidden; }
        .block-container { padding-top: 0rem; max-width: 1600px; padding-left: 0; padding-right: 0; }
        
        /* Typography */
        h1, h2, h3 { font-family: 'Courier New', monospace; font-weight: 900; text-transform: uppercase; margin-bottom: 0; }
        .gradient-text { background: linear-gradient(90deg, #00ff41, #008f11); -webkit-background-clip: text; color: transparent; }
        
        /* Full Viewport Sections */
        .cinematic-section {
            min-height: 90vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 50px 20px;
            border-bottom: 1px solid rgba(0, 255, 65, 0.1);
            position: relative;
        }
        
        /* Hero Styling */
        .glitch-wrapper { display: flex; justify-content: center; align-items: center; margin-top: 5vh; }
        .glitch {
            font-size: 8rem; font-weight: 900; text-transform: uppercase; position: relative; color: #fff; letter-spacing: 12px; font-family: 'Courier New', monospace;
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
        .sub-glitch { text-align: center; color: #00ff41; font-size: 1.5rem; letter-spacing: 5px; margin-bottom: 5vh; font-family: 'Courier New', monospace; text-shadow: 0 0 15px #00ff41; }
        
        .scroll-down { margin-top: 10vh; color: #8b949e; font-family: 'Courier New', monospace; animation: bounce 2s infinite; letter-spacing: 2px;}
        @keyframes bounce { 0%, 20%, 50%, 80%, 100% {transform: translateY(0);} 40% {transform: translateY(-20px);} 60% {transform: translateY(-10px);} }

    </style>
""", unsafe_allow_html=True)


# =========================================================================
# SECTION 1: HERO
# =========================================================================
st.markdown("""
<div class="cinematic-section">
    <div class="glitch-wrapper"><div class="glitch" data-text="T.O.M.M.Y.">T.O.M.M.Y.</div></div>
    <div class="sub-glitch">TELEMETRIC . OPTICAL & MULTIMODAL . MACHINE . YIELD</div>
    
    <div style="display: flex; justify-content: center; gap: 80px; text-align: center; font-family: 'Courier New', monospace; margin-top: 5vh;">
        <div><div style="color: #8b949e; font-size: 1rem;">VISION LATENCY</div><div style="color: #fff; font-size: 3.5rem; font-weight: 900;">18<span style="color:#00ff41; font-size:1.5rem;">ms</span></div></div>
        <div><div style="color: #8b949e; font-size: 1rem;">CLOUD APIs</div><div style="color: #fff; font-size: 3.5rem; font-weight: 900;">0<span style="color:#00ff41; font-size:1.5rem;">.0%</span></div></div>
        <div><div style="color: #8b949e; font-size: 1rem;">IPC SYNCHRONIZATION</div><div style="color: #fff; font-size: 3.5rem; font-weight: 900;">60<span style="color:#00ff41; font-size:1.5rem;">FPS</span></div></div>
    </div>
    
    <div class="scroll-down">v INITIATE DEPLOYMENT SEQUENCE v</div>
</div>
""", unsafe_allow_html=True)


# =========================================================================
# SECTION 2: INTERACTIVE SIMULATOR (THE FEEL)
# =========================================================================
st.markdown('<div class="cinematic-section" style="background: radial-gradient(circle, #0a110a 0%, #020202 100%);">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 3rem; text-align:center;">LIVE <span class="gradient-text">TELEMETRIC</span> SIMULATOR</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#8b949e; font-size:1.2rem; max-width:800px; margin: 20px auto;">T.O.M.M.Y. uses your nose as a mouse pointer. We use a 55-pixel Euclidean collision boundary to ensure jitter-free clicks. <b>Test the engine below: Use your mouse to chase the target. Stay inside the green boundary to lock on!</b></p>', unsafe_allow_html=True)

# HTML5 Canvas Game
components.html("""
    <div style="display:flex; justify-content:center; align-items:center; flex-direction:column;">
        <canvas id="simCanvas" style="border: 2px solid #30363d; border-radius: 8px; cursor: crosshair; box-shadow: 0 0 30px rgba(0,255,65,0.1);"></canvas>
        <div style="margin-top: 15px; width: 800px; height: 10px; background: #111; border-radius: 5px; overflow: hidden;">
            <div id="lockBar" style="width: 0%; height: 100%; background: #00ff41; transition: width 0.1s;"></div>
        </div>
        <p id="simStatus" style="color:#8b949e; font-family:'Courier New', monospace; margin-top: 10px; font-weight: bold;">STATUS: AWAITING TARGET ACQUISITION</p>
    </div>
    <script>
        const canvas = document.getElementById('simCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = 800; canvas.height = 400;
        
        let mouseX = canvas.width / 2; let mouseY = canvas.height / 2;
        let targetX = canvas.width / 2; let targetY = canvas.height / 2;
        let tVx = 3; let tVy = 3;
        let lockScore = 0;
        
        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            mouseX = e.clientX - rect.left;
            mouseY = e.clientY - rect.top;
        });

        function animate() {
            requestAnimationFrame(animate);
            ctx.fillStyle = '#050505';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Move Target
            targetX += tVx; targetY += tVy;
            if(targetX < 20 || targetX > canvas.width - 20) { tVx *= -1; tVx += (Math.random() - 0.5); }
            if(targetY < 20 || targetY > canvas.height - 20) { tVy *= -1; tVy += (Math.random() - 0.5); }
            
            // Clamp speed
            tVx = Math.max(-5, Math.min(5, tVx));
            tVy = Math.max(-5, Math.min(5, tVy));

            // Draw Target
            ctx.beginPath();
            ctx.arc(targetX, targetY, 15, 0, Math.PI * 2);
            ctx.fillStyle = '#F85149';
            ctx.fill();
            
            // Calculate Euclidean Distance
            let dx = mouseX - targetX;
            let dy = mouseY - targetY;
            let distance = Math.sqrt(dx * dx + dy * dy);
            
            // The 55-pixel rule
            if (distance < 55) {
                ctx.strokeStyle = '#00ff41';
                ctx.lineWidth = 3;
                lockScore = Math.min(100, lockScore + 1);
                document.getElementById('simStatus').innerText = "STATUS: TELEMETRIC LOCK ENGAGED";
                document.getElementById('simStatus').style.color = "#00ff41";
            } else {
                ctx.strokeStyle = '#8b949e';
                ctx.lineWidth = 1;
                lockScore = Math.max(0, lockScore - 2);
                document.getElementById('simStatus').innerText = "STATUS: TRACKING TARGET...";
                document.getElementById('simStatus').style.color = "#8b949e";
            }
            document.getElementById('lockBar').style.width = lockScore + "%";
            
            // Draw Collision Boundary around mouse
            ctx.beginPath();
            ctx.arc(mouseX, mouseY, 55, 0, Math.PI * 2);
            ctx.stroke();
            
            // Draw Line
            ctx.beginPath();
            ctx.moveTo(mouseX, mouseY);
            ctx.lineTo(targetX, targetY);
            ctx.stroke();
        }
        animate();
    </script>
""", height=500)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 3: THE VISION ENGINE
# =========================================================================
st.markdown('<div class="cinematic-section">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    components.html("""
        <style>
            .radar { width: 400px; height: 400px; border-radius: 50%; border: 2px solid #00ff41; margin: 0 auto; overflow: hidden; position: relative; box-shadow: 0 0 50px rgba(0,255,65,0.15); }
            .radar::after { content: ''; position: absolute; width: 200px; height: 200px; background: linear-gradient(45deg, rgba(0,255,65,0.8) 0%, transparent 50%); transform-origin: bottom right; top: 0; left: 0; animation: scan 1.5s linear infinite; }
            .grid { position: absolute; width: 100%; height: 100%; background-image: linear-gradient(#00ff41 1px, transparent 1px), linear-gradient(90deg, #00ff41 1px, transparent 1px); background-size: 40px 40px; opacity: 0.1; }
            .face-mesh { position: absolute; width: 100px; height: 150px; border: 1px dashed #00ff41; top: 30%; left: 35%; border-radius: 50%; animation: pulse 2s infinite; }
            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(0,255,65,0.4); } 70% { box-shadow: 0 0 0 30px rgba(0,255,65,0); } 100% { box-shadow: 0 0 0 0 rgba(0,255,65,0); } }
        </style>
        <div class="radar"><div class="grid"></div><div class="face-mesh"></div></div>
    """, height=450)

with col2:
    st.markdown('<h2 style="font-size: 3.5rem;">THE <span class="gradient-text">TELEMETRIC</span><br>ENGINE.</h2>', unsafe_allow_html=True)
    st.markdown("""
        <p style="font-size: 1.3rem; color: #8b949e; line-height: 1.8; margin-top: 30px;">
            Standard 2D hand tracking relies on sluggish Neural Network classifications. It shakes. It stutters. It fails in low light.
            <br><br>
            T.O.M.M.Y. abandons CNNs entirely in favor of raw <b>Euclidean Matrix Geometry</b>. By tethering the cursor physically to <b>FaceMesh Node 1</b> (The nose), we completely bypass biological arm fatigue.
            <br><br>
            <b>OCULAR PROTOCOLS:</b><br>
            <span style="color:#00ff41; font-weight:bold;">> 1 Blink:</span> Left Mouse Click<br>
            <span style="color:#00ff41; font-weight:bold;">> 2 Blinks:</span> Right Mouse Click<br>
            <span style="color:#00ff41; font-weight:bold;">> Mouth Open Gate:</span> Triggers Shift/Modifier Keys<br>
            <span style="color:#00ff41; font-weight:bold;">> Head Roll Left/Right:</span> Media Player Control
        </p>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 4: THE VOICE DAEMON
# =========================================================================
st.markdown('<div class="cinematic-section" style="background: #020202;">', unsafe_allow_html=True)
col3, col4 = st.columns([1, 1], gap="large")
with col3:
    st.markdown('<h2 style="font-size: 3.5rem;">DETERMINISTIC<br><span class="gradient-text">VOICE</span> ISOLATION.</h2>', unsafe_allow_html=True)
    st.markdown("""
        <p style="font-size: 1.3rem; color: #8b949e; line-height: 1.8; margin-top: 30px;">
            Waiting 2,000ms for ChatGPT to "generate" an API response just to mute your computer volume is a catastrophic failure in OS design.
            <br><br>
            We banned LLMs from the primary logic loop. T.O.M.M.Y. rips out heavy generative AI and replaces it with the <b>spaCy</b> grammatical engine. It runs locally, totally offline, parsing your exact human intent in under 15ms.
            <br><br>
            <span style="color:#00ff41; font-family:'Courier New', monospace;"><b>[+] ZERO CLOUD HOOKS.</b></span><br>
            <span style="color:#00ff41; font-family:'Courier New', monospace;"><b>[+] ZERO AUDIO DATA LOGGED.</b></span>
        </p>
    """, unsafe_allow_html=True)

with col4:
    components.html("""
        <style>
            .wave-container { display: flex; align-items: center; justify-content: center; height: 400px; gap: 8px; }
            .bar { width: 25px; background: #00ff41; border-radius: 12px; animation: sound 0ms -800ms linear infinite alternate; box-shadow: 0 0 20px rgba(0,255,65,0.6); }
            @keyframes sound { 0% { height: 20px; opacity: 0.3; } 100% { height: 250px; opacity: 1; } }
            .bar:nth-child(1)  { animation-duration: 474ms; } .bar:nth-child(2)  { animation-duration: 433ms; }
            .bar:nth-child(3)  { animation-duration: 407ms; } .bar:nth-child(4)  { animation-duration: 458ms; }
            .bar:nth-child(5)  { animation-duration: 400ms; } .bar:nth-child(6)  { animation-duration: 427ms; }
            .bar:nth-child(7)  { animation-duration: 441ms; } .bar:nth-child(8)  { animation-duration: 419ms; }
        </style>
        <div class="wave-container">
            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
        </div>
    """, height=450)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 5: DEPLOYMENT TERMINAL
# =========================================================================
st.markdown('<div class="cinematic-section">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 3rem; text-align:center;">>_ DEPLOY THE KERNEL</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#8b949e; font-size:1.2rem; max-width:800px; margin: 20px auto 50px auto;">We engineered T.O.M.M.Y. to infect your machine cleanly, without polluting your Windows PATH. <b>Double-click the payload</b> and let the sandbox build itself.</p>', unsafe_allow_html=True)

components.html("""
    <div style="background: #010409; border: 1px solid #30363d; border-radius: 8px; width: 80%; margin: 0 auto; font-family: 'Courier New', monospace; box-shadow: 0 10px 40px rgba(0,0,0,0.8); overflow: hidden;">
        <div style="background: #161b22; padding: 15px; border-bottom: 1px solid #30363d; display: flex; gap: 8px;">
            <div style="width: 14px; height: 14px; border-radius: 50%; background: #ff5f56;"></div>
            <div style="width: 14px; height: 14px; border-radius: 50%; background: #ffbd2e;"></div>
            <div style="width: 14px; height: 14px; border-radius: 50%; background: #27c93f;"></div>
            <div style="color: #8b949e; margin-left: 15px; font-size: 0.9rem;">setup.bat — PowerShell Handoff</div>
        </div>
        <div style="padding: 30px; color: #fff; font-size: 1.2rem; line-height: 1.8;">
            <span style="color:#00ff41;">C:\\Windows\\System32></span> git clone https://github.com/chiragphogat/tommy-os.git<br>
            <span style="color:#00ff41;">C:\\Windows\\System32></span> cd tommy-os<br>
            <span style="color:#00ff41;">C:\\tommy-os></span> .\\setup.bat<br>
            <br>
            <span style="color:#8b949e;">[+] Securing Virtual Sandbox (venv)... DONE</span><br>
            <span style="color:#8b949e;">[+] Injecting spaCy Syntactic Arrays... DONE</span><br>
            <span style="color:#8b949e;">[+] Overriding Windows Execution Policies... DONE</span><br>
            <br>
            <span style="color:#3fb950; font-weight:bold;">PS C:\\tommy-os></span> python tommy_os.py<span style="animation: blink 1s infinite;">█</span>
        </div>
    </div>
    <style>@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }</style>
""", height=400)

st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://github.com/chiragphogat/tommy-os" target="_blank" style="background: #00ff41; color: #000; padding: 20px 60px; font-size: 1.5rem; font-family: 'Courier New', monospace; font-weight: 900; text-decoration: none; border-radius: 4px; display: inline-block; box-shadow: 0 0 30px rgba(0, 255, 65, 0.4); transition: transform 0.2s;">DOWNLOAD SOURCE CODE</a>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 6: FOOTER (ACADEMIC)
# =========================================================================
st.markdown("""
<div style="background: #0a0a0a; border-top: 1px solid #222; padding: 80px 20px; text-align: center;">
    <h3 style="color:#58a6ff; font-size: 1.5rem; margin-bottom: 30px;">// ACADEMIC RESOURCES</h3>
    <p style="color:#8b949e; max-width: 800px; margin: 0 auto 30px auto; line-height: 1.6;">
        T.O.M.M.Y. was engineered at Lovely Professional University to evaluate the absolute limits of Multi-Process Hardware Concurrency on Python Operating System Wrappers. By mathematically bridging process memory walls, we successfully dodged the Global Interpreter Lock (GIL).
    </p>
    <div style="display: flex; justify-content: center; gap: 40px; margin-bottom: 40px; color: #fff;">
        <div><b>Chirag Phogat</b><br><span style="color:#8b949e; font-size:0.9rem;">Lead Architect</span></div>
        <div><b>Chava Harshavardhan</b><br><span style="color:#8b949e; font-size:0.9rem;">Gaze Estimation Math</span></div>
        <div><b>Lalmalsawm Guite</b><br><span style="color:#8b949e; font-size:0.9rem;">Lead Researcher</span></div>
        <div><b>Kaushal Pathak</b><br><span style="color:#8b949e; font-size:0.9rem;">Project Mentor</span></div>
    </div>
    <div style="font-family: 'Courier New', monospace; color: #444; font-size: 0.9rem;">
        © 2026 T.O.M.M.Y. OS PLATFORM. ALL SYSTEMS NOMINAL.
    </div>
</div>
""", unsafe_allow_html=True)
