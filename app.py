import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="T.O.M.M.Y. OS",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================================
# GLOBAL CSS INJECTION (SMOOTH CINEMATIC SCROLL)
# =========================================================================
st.markdown("""
    <style>
        .stApp {
            background-color: #020202;
            color: #e6e6e6;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        
        header, #MainMenu, footer { visibility: hidden; }
        .block-container { padding-top: 2rem; max-width: 1400px; padding-bottom: 2rem; }
        
        h1, h2, h3 { font-family: 'Courier New', monospace; font-weight: 900; text-transform: uppercase; margin-bottom: 0; }
        .gradient-text { background: linear-gradient(90deg, #00ff41, #008f11); -webkit-background-clip: text; color: transparent; }
        
        .cinematic-section {
            padding: 60px 20px;
            margin: 40px 0;
            border-bottom: 1px solid rgba(0, 255, 65, 0.1);
            position: relative;
        }
    </style>
""", unsafe_allow_html=True)


# =========================================================================
# SECTION 1: HERO & METRICS (FIXED HTML PARSING)
# =========================================================================
components.html("""
    <style>
        .hero-container { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px 0; }
        .glitch { font-size: 8rem; font-weight: 900; text-transform: uppercase; position: relative; color: #fff; letter-spacing: 12px; font-family: 'Courier New', monospace; text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.025em -0.05em 0 rgba(0,255,0,0.75), 0.025em 0.05em 0 rgba(0,0,255,0.75); animation: glitch 500ms infinite; margin: 0; }
        @keyframes glitch { 0% { text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.05em -0.025em 0 rgba(0,255,0,0.75), -0.025em 0.05em 0 rgba(0,0,255,0.75); } 20% { text-shadow: -0.05em -0.025em 0 rgba(255,0,0,0.75), 0.025em 0.025em 0 rgba(0,255,0,0.75), -0.05em -0.05em 0 rgba(0,0,255,0.75); } 40% { text-shadow: 0.025em 0.05em 0 rgba(255,0,0,0.75), 0.05em 0 0 rgba(0,255,0,0.75), 0 -0.05em 0 rgba(0,0,255,0.75); } 60% { text-shadow: -0.025em 0 0 rgba(255,0,0,0.75), -0.025em -0.025em 0 rgba(0,255,0,0.75), -0.025em -0.05em 0 rgba(0,0,255,0.75); } 80% { text-shadow: 0.05em -0.05em 0 rgba(255,0,0,0.75), 0.025em 0.05em 0 rgba(0,255,0,0.75), -0.05em -0.025em 0 rgba(0,0,255,0.75); } 100% { text-shadow: -0.025em 0.05em 0 rgba(255,0,0,0.75), -0.05em -0.05em 0 rgba(0,255,0,0.75), 0.025em 0 0 rgba(0,0,255,0.75); } }
        .sub-glitch { text-align: center; color: #00ff41; font-size: 1.5rem; letter-spacing: 5px; margin-top: 10px; font-family: 'Courier New', monospace; text-shadow: 0 0 15px #00ff41; }
        .metrics-row { display: flex; justify-content: center; gap: 80px; text-align: center; font-family: 'Courier New', monospace; margin-top: 60px; }
        .metric-label { color: #8b949e; font-size: 1rem; }
        .metric-val { color: #fff; font-size: 3.5rem; font-weight: 900; }
        .metric-unit { color:#00ff41; font-size:1.5rem; }
    </style>
    <div class="hero-container">
        <div class="glitch" data-text="T.O.M.M.Y.">T.O.M.M.Y.</div>
        <div class="sub-glitch">TELEMETRIC OPTICAL & MULTIMODAL KERNEL</div>
        <div class="metrics-row">
            <div><div class="metric-label">VISION LATENCY</div><div class="metric-val">18<span class="metric-unit">ms</span></div></div>
            <div><div class="metric-label">CLOUD APIs</div><div class="metric-val">0<span class="metric-unit">.0%</span></div></div>
            <div><div class="metric-label">IPC BRIDGE</div><div class="metric-val">60<span class="metric-unit">FPS</span></div></div>
        </div>
    </div>
""", height=400)


# =========================================================================
# SECTION 2: THE REWARDING INTERACTIVE SIMULATOR
# =========================================================================
st.markdown('<div class="cinematic-section" style="background: radial-gradient(circle, rgba(10,20,10,0.6) 0%, rgba(2,2,2,1) 100%); border-radius: 12px; border: 1px solid rgba(0,255,65,0.3); padding: 40px;">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 3rem; text-align:center;">LIVE <span class="gradient-text">TELEMETRIC</span> SIMULATOR</h2>', unsafe_allow_html=True)

# The HTML5 Game with Particle Explosions
components.html("""
    <style>
        body { margin: 0; display:flex; flex-direction:column; align-items:center; font-family: 'Courier New', monospace; background: transparent; color: #fff; }
        .canvas-container { position: relative; width: 100%; max-width: 900px; }
        canvas { width: 100%; height: 450px; background: #010409; border: 2px solid #30363d; border-radius: 8px; cursor: crosshair; box-shadow: 0 10px 40px rgba(0,0,0,0.8); transition: border-color 0.3s, box-shadow 0.3s; }
        .overlay-text { position: absolute; top: 20px; left: 0; width: 100%; text-align: center; pointer-events: none; z-index: 10; font-weight: bold; font-size: 1.5rem; text-shadow: 0 0 10px #000; }
        .status-bar { margin-top: 15px; width: 100%; max-width: 900px; height: 15px; background: #111; border-radius: 8px; overflow: hidden; border: 1px solid #333; }
        #lockBar { width: 0%; height: 100%; background: #00ff41; transition: width 0.1s linear; }
        #simStatus { color: #8b949e; font-size: 1.1rem; margin-top: 10px; font-weight: bold; text-align: center; }
        
        .win-overlay {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 255, 65, 0.1); display: none;
            flex-direction: column; justify-content: center; align-items: center; border-radius: 8px; pointer-events: none;
            backdrop-filter: blur(2px);
        }
        .win-overlay h2 { color: #00ff41; font-size: 3rem; text-shadow: 0 0 20px #00ff41; margin: 0; animation: pulse 1s infinite; }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
    </style>
    
    <div class="canvas-container">
        <div class="overlay-text" id="instructText" style="color:#00ff41; animation: pulse 1s infinite;">>_ USE YOUR MOUSE TO CHASE THE RED TARGET _<</div>
        <canvas id="simCanvas"></canvas>
        <div class="win-overlay" id="winScreen">
            <h2>SYSTEM OVERRIDE SUCCESSFUL</h2>
            <p style="color:#fff; font-size:1.2rem; background: #000; padding: 5px 10px;">FaceMesh Telemetry Locked at 18ms.</p>
        </div>
    </div>
    <div class="status-bar"><div id="lockBar"></div></div>
    <div id="simStatus">STATUS: AWAITING TARGET ACQUISITION</div>

    <script>
        const canvas = document.getElementById('simCanvas');
        const ctx = canvas.getContext('2d');
        
        // Match internal resolution to display size for sharp rendering
        canvas.width = 900;
        canvas.height = 450;
        
        let mouseX = canvas.width / 2; let mouseY = canvas.height / 2;
        let targetX = canvas.width / 2; let targetY = canvas.height / 2;
        let tVx = 6; let tVy = 6;
        let lockScore = 0;
        let gameState = "PLAYING"; // PLAYING, WIN
        let particles = [];
        
        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            // Scale mouse coordinates to internal canvas resolution
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;
            mouseX = (e.clientX - rect.left) * scaleX;
            mouseY = (e.clientY - rect.top) * scaleY;
        });

        function createExplosion(x, y) {
            for(let i=0; i<60; i++) {
                particles.push({
                    x: x, y: y,
                    vx: (Math.random() - 0.5) * 20,
                    vy: (Math.random() - 0.5) * 20,
                    life: 1.0,
                    color: Math.random() > 0.5 ? '#F85149' : '#00ff41'
                });
            }
        }

        function animate() {
            requestAnimationFrame(animate);
            ctx.fillStyle = '#010409';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Draw Grid
            ctx.strokeStyle = "rgba(0, 255, 65, 0.1)"; ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=50) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke(); }
            for(let i=0; i<canvas.height; i+=50) { ctx.beginPath(); ctx.moveTo(0,i); ctx.lineTo(canvas.width,i); ctx.stroke(); }

            if (gameState === "PLAYING") {
                // Move Target
                targetX += tVx; targetY += tVy;
                if(targetX < 30 || targetX > canvas.width - 30) { tVx *= -1; tVx += (Math.random() - 0.5)*3; }
                if(targetY < 30 || targetY > canvas.height - 30) { tVy *= -1; tVy += (Math.random() - 0.5)*3; }
                
                tVx = Math.max(-8, Math.min(8, tVx));
                tVy = Math.max(-8, Math.min(8, tVy));

                // Draw Target
                ctx.beginPath(); ctx.arc(targetX, targetY, 15, 0, Math.PI * 2);
                ctx.fillStyle = '#F85149'; ctx.fill();
                
                // Math
                let dx = mouseX - targetX; let dy = mouseY - targetY;
                let distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 55) {
                    ctx.strokeStyle = '#00ff41'; ctx.lineWidth = 3;
                    lockScore += 0.8; // Takes roughly 2 seconds to fill
                    document.getElementById('simStatus').innerText = "STATUS: TELEMETRIC LOCK ENGAGED (HOLD POSITION)";
                    document.getElementById('simStatus').style.color = "#00ff41";
                    canvas.style.borderColor = "#00ff41";
                    canvas.style.boxShadow = "0 0 40px rgba(0,255,65,0.5)";
                } else {
                    ctx.strokeStyle = '#8b949e'; ctx.lineWidth = 1;
                    lockScore = Math.max(0, lockScore - 1);
                    document.getElementById('simStatus').innerText = "STATUS: TRACKING TARGET... (MOVE MOUSE INSIDE TARGET)";
                    document.getElementById('simStatus').style.color = "#8b949e";
                    canvas.style.borderColor = "#30363d";
                    canvas.style.boxShadow = "0 10px 40px rgba(0,0,0,0.8)";
                }
                
                document.getElementById('lockBar').style.width = lockScore + "%";
                
                // Draw 55px Mouse Boundary
                ctx.beginPath(); ctx.arc(mouseX, mouseY, 55, 0, Math.PI * 2); ctx.stroke();
                // Connection Line
                ctx.beginPath(); ctx.moveTo(mouseX, mouseY); ctx.lineTo(targetX, targetY); ctx.stroke();
                
                // Check Win
                if (lockScore >= 100) {
                    gameState = "WIN";
                    createExplosion(targetX, targetY);
                    document.getElementById('winScreen').style.display = "flex";
                    document.getElementById('instructText').style.display = "none";
                    document.getElementById('simStatus').innerText = "STATUS: TARGET DESTROYED. KERNEL OVERRIDE.";
                    setTimeout(() => {
                        // Reset Game after 5 seconds
                        gameState = "PLAYING";
                        lockScore = 0;
                        document.getElementById('winScreen').style.display = "none";
                        document.getElementById('instructText').style.display = "block";
                        document.getElementById('lockBar').style.width = "0%";
                    }, 5000);
                }
            } else if (gameState === "WIN") {
                // Update and draw particles
                for (let i = particles.length - 1; i >= 0; i--) {
                    let p = particles[i];
                    p.x += p.vx; p.y += p.vy;
                    p.life -= 0.02;
                    if (p.life <= 0) { particles.splice(i, 1); continue; }
                    ctx.globalAlpha = p.life;
                    ctx.fillStyle = p.color;
                    ctx.beginPath(); ctx.arc(p.x, p.y, 4, 0, Math.PI * 2); ctx.fill();
                }
                ctx.globalAlpha = 1.0;
            }
        }
        animate();
    </script>
""", height=550)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 3: THE VISION ENGINE
# =========================================================================
st.markdown('<div class="cinematic-section">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1], gap="large", vertical_alignment="center")

with col1:
    components.html("""
        <style>
            .radar { width: 350px; height: 350px; border-radius: 50%; border: 2px solid #00ff41; margin: 0 auto; overflow: hidden; position: relative; box-shadow: 0 0 50px rgba(0,255,65,0.15); }
            .radar::after { content: ''; position: absolute; width: 175px; height: 175px; background: linear-gradient(45deg, rgba(0,255,65,0.8) 0%, transparent 50%); transform-origin: bottom right; top: 0; left: 0; animation: scan 1.5s linear infinite; }
            .grid { position: absolute; width: 100%; height: 100%; background-image: linear-gradient(#00ff41 1px, transparent 1px), linear-gradient(90deg, #00ff41 1px, transparent 1px); background-size: 40px 40px; opacity: 0.1; }
            .face-mesh { position: absolute; width: 100px; height: 150px; border: 1px dashed #00ff41; top: 30%; left: 35%; border-radius: 50%; animation: pulse 2s infinite; }
            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(0,255,65,0.4); } 70% { box-shadow: 0 0 0 30px rgba(0,255,65,0); } 100% { box-shadow: 0 0 0 0 rgba(0,255,65,0); } }
        </style>
        <div class="radar"><div class="grid"></div><div class="face-mesh"></div></div>
    """, height=400)

with col2:
    st.markdown('<h2 style="font-size: 3rem;">THE <span class="gradient-text">TELEMETRIC</span><br>ENGINE.</h2>', unsafe_allow_html=True)
    st.markdown("""
        <p style="font-size: 1.2rem; color: #8b949e; line-height: 1.8; margin-top: 20px;">
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
st.markdown('<div class="cinematic-section" style="background: rgba(10,10,10,0.5); border-radius: 12px; padding: 40px;">', unsafe_allow_html=True)
col3, col4 = st.columns([1, 1], gap="large", vertical_alignment="center")

with col3:
    st.markdown('<h2 style="font-size: 3rem;">DETERMINISTIC<br><span class="gradient-text">VOICE</span> ISOLATION.</h2>', unsafe_allow_html=True)
    st.markdown("""
        <p style="font-size: 1.2rem; color: #8b949e; line-height: 1.8; margin-top: 20px;">
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
            .wave-container { display: flex; align-items: center; justify-content: center; height: 350px; gap: 8px; }
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
    """, height=350)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 5: DEPLOYMENT TERMINAL
# =========================================================================
st.markdown('<div class="cinematic-section">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 3rem; text-align:center;">>_ DEPLOY THE KERNEL</h2>', unsafe_allow_html=True)

components.html("""
    <div style="background: #010409; border: 1px solid #30363d; border-radius: 8px; width: 70%; margin: 40px auto; font-family: 'Courier New', monospace; box-shadow: 0 10px 40px rgba(0,0,0,0.8); overflow: hidden; position: relative;">
        <div style="background: #161b22; padding: 15px; border-bottom: 1px solid #30363d; display: flex; justify-content: space-between; align-items:center;">
            <div style="display: flex; gap: 8px; align-items:center;">
                <div style="width: 14px; height: 14px; border-radius: 50%; background: #ff5f56;"></div>
                <div style="width: 14px; height: 14px; border-radius: 50%; background: #ffbd2e;"></div>
                <div style="width: 14px; height: 14px; border-radius: 50%; background: #27c93f;"></div>
                <div style="color: #8b949e; margin-left: 15px; font-size: 0.9rem;">setup.bat — PowerShell Handoff</div>
            </div>
            <button id="copyBtn" onclick="copyCmds()" style="background: transparent; border: 1px solid #00ff41; color: #00ff41; padding: 5px 15px; border-radius: 4px; cursor: pointer; font-family: 'Courier New', monospace; font-weight: bold; transition: all 0.2s;">[ COPY COMMANDS ]</button>
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
    <script>
        function copyCmds() {
            const text = "git clone https://github.com/chiragphogat/tommy-os.git\\ncd tommy-os\\n.\\\\setup.bat";
            const el = document.createElement('textarea');
            el.value = text;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            document.getElementById("copyBtn").innerText = "[ COPIED! ]";
            document.getElementById("copyBtn").style.background = "#00ff41";
            document.getElementById("copyBtn").style.color = "#000";
            setTimeout(() => {
                document.getElementById("copyBtn").innerText = "[ COPY COMMANDS ]";
                document.getElementById("copyBtn").style.background = "transparent";
                document.getElementById("copyBtn").style.color = "#00ff41";
            }, 2000);
        }
    </script>
    <style>
        @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
        #copyBtn:hover { background: rgba(0,255,65,0.2) !important; }
    </style>
""", height=400)

install_script = """@echo off
color 0A
echo ===================================================
echo   T.O.M.M.Y. OS - REMOTE DEPLOYMENT INITIALIZED
echo ===================================================
echo.
echo [*] Fetching kernel from GitHub...
git clone https://github.com/chiragphogat/tommy-os.git
cd tommy-os
echo [*] Triggering native setup sandbox...
call setup.bat
pause
"""

st.markdown("""
    <style>
        .stDownloadButton button { background: #00ff41; color: #000; padding: 15px 40px; font-size: 1.5rem; font-family: 'Courier New', monospace; font-weight: 900; text-decoration: none; border-radius: 4px; box-shadow: 0 0 30px rgba(0, 255, 65, 0.4); border: none; width: 100%; transition: transform 0.2s;}
        .stDownloadButton button:hover { transform: scale(1.02); background: #00ff41; color: #000; border: none;}
    </style>
""", unsafe_allow_html=True)

col_d1, col_d2, col_d3 = st.columns([1, 2, 1])
with col_d2:
    st.download_button(
        label="⚡ DOWNLOAD 1-CLICK INSTALLER (.BAT)",
        data=install_script,
        file_name="install_tommy.bat",
        mime="application/x-msdownload"
    )

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 6: FOOTER (ACADEMIC)
# =========================================================================
st.markdown("""
<div style="background: #0a0a0a; border-top: 1px solid #222; padding: 60px 20px; text-align: center; margin-top: 40px;">
    <h3 style="color:#58a6ff; font-size: 1.5rem; margin-bottom: 20px;">// ACADEMIC RESOURCES</h3>
    <p style="color:#8b949e; max-width: 800px; margin: 0 auto 30px auto; line-height: 1.6;">
        T.O.M.M.Y. was engineered at Lovely Professional University to evaluate the absolute limits of Multi-Process Hardware Concurrency on Python Operating System Wrappers.
    </p>
    <div style="display: flex; justify-content: center; gap: 40px; margin-bottom: 40px; color: #fff;">
        <div><b>Chirag Phogat</b><br><span style="color:#8b949e; font-size:0.9rem;">Lead Architect</span></div>
        <div><b>Chava Harshavardhan</b><br><span style="color:#8b949e; font-size:0.9rem;">Gaze Estimation Math</span></div>
        <div><b>Lalmalsawm Guite</b><br><span style="color:#8b949e; font-size:0.9rem;">Lead Researcher</span></div>
        <div><b>Kaushal Pathak</b><br><span style="color:#8b949e; font-size:0.9rem;">Project Mentor</span></div>
    </div>
</div>
""", unsafe_allow_html=True)
