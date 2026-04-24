import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="T.O.M.M.Y. OS",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================================
# GLOBAL CSS INJECTION (CINEMATIC FADES & SCROLL)
# =========================================================================
st.markdown("""
    <style>
        .stApp {
            background-color: #010203;
            color: #e6e6e6;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }
        
        header, #MainMenu, footer { visibility: hidden; }
        .block-container { padding-top: 2rem; max-width: 1400px; padding-bottom: 2rem; }
        
        h1, h2, h3 { font-family: 'Courier New', monospace; font-weight: 900; text-transform: uppercase; margin-bottom: 0; }
        .gradient-text { background: linear-gradient(90deg, #00ff41, #008f11); -webkit-background-clip: text; color: transparent; }
        
        /* Cinematic Fade Up Animation */
        .cinematic-section {
            padding: 60px 20px;
            margin: 40px 0;
            border-bottom: 1px solid rgba(0, 255, 65, 0.05);
            position: relative;
            animation: fadeUp 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        
        @keyframes fadeUp {
            0% { opacity: 0; transform: translateY(60px); filter: blur(5px); }
            100% { opacity: 1; transform: translateY(0); filter: blur(0); }
        }
    </style>
""", unsafe_allow_html=True)


# =========================================================================
# SECTION 1: MATRIX HERO & METRICS
# =========================================================================
components.html("""
    <style>
        body { margin: 0; padding: 0; background: #010203; overflow: hidden; font-family: 'Courier New', monospace;}
        .hero-container { position: relative; width: 100%; height: 500px; display: flex; flex-direction: column; align-items: center; justify-content: center; }
        canvas { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; opacity: 0.3; }
        .content { position: relative; z-index: 10; display: flex; flex-direction: column; align-items: center; }
        .glitch { font-size: 8rem; font-weight: 900; text-transform: uppercase; color: #fff; letter-spacing: 12px; text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.025em -0.05em 0 rgba(0,255,0,0.75), 0.025em 0.05em 0 rgba(0,0,255,0.75); animation: glitch 500ms infinite; margin: 0; }
        @keyframes glitch { 0% { text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.05em -0.025em 0 rgba(0,255,0,0.75), -0.025em 0.05em 0 rgba(0,0,255,0.75); } 20% { text-shadow: -0.05em -0.025em 0 rgba(255,0,0,0.75), 0.025em 0.025em 0 rgba(0,255,0,0.75), -0.05em -0.05em 0 rgba(0,0,255,0.75); } 40% { text-shadow: 0.025em 0.05em 0 rgba(255,0,0,0.75), 0.05em 0 0 rgba(0,255,0,0.75), 0 -0.05em 0 rgba(0,0,255,0.75); } 60% { text-shadow: -0.025em 0 0 rgba(255,0,0,0.75), -0.025em -0.025em 0 rgba(0,255,0,0.75), -0.025em -0.05em 0 rgba(0,0,255,0.75); } 80% { text-shadow: 0.05em -0.05em 0 rgba(255,0,0,0.75), 0.025em 0.05em 0 rgba(0,255,0,0.75), -0.05em -0.025em 0 rgba(0,0,255,0.75); } 100% { text-shadow: -0.025em 0.05em 0 rgba(255,0,0,0.75), -0.05em -0.05em 0 rgba(0,255,0,0.75), 0.025em 0 0 rgba(0,0,255,0.75); } }
        .sub-glitch { color: #00ff41; font-size: 1.5rem; letter-spacing: 5px; margin-top: 10px; text-shadow: 0 0 15px #00ff41; }
        .metrics-row { display: flex; justify-content: center; gap: 80px; text-align: center; margin-top: 60px; }
        .metric-label { color: #8b949e; font-size: 1rem; }
        .metric-val { color: #fff; font-size: 3.5rem; font-weight: 900; }
        .metric-unit { color:#00ff41; font-size:1.5rem; }
    </style>
    
    <div class="hero-container">
        <canvas id="matrixCanvas"></canvas>
        <div class="content">
            <div class="glitch" data-text="T.O.M.M.Y.">T.O.M.M.Y.</div>
            <div class="sub-glitch">TELEMETRIC OPTICAL & MULTIMODAL KERNEL</div>
            <div class="metrics-row">
                <div><div class="metric-label">VISION LATENCY</div><div class="metric-val">18<span class="metric-unit">ms</span></div></div>
                <div><div class="metric-label">CLOUD APIs</div><div class="metric-val">0<span class="metric-unit">.0%</span></div></div>
                <div><div class="metric-label">IPC BRIDGE</div><div class="metric-val">60<span class="metric-unit">FPS</span></div></div>
            </div>
        </div>
    </div>
    
    <script>
        // Matrix Rain Animation
        const canvas = document.getElementById('matrixCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth; canvas.height = 500;
        const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'.split('');
        const fontSize = 14; const columns = canvas.width / fontSize;
        const drops = []; for(let x = 0; x < columns; x++) drops[x] = 1;
        
        function drawMatrix() {
            ctx.fillStyle = 'rgba(1, 2, 3, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#00ff41'; ctx.font = fontSize + 'px monospace';
            for(let i = 0; i < drops.length; i++) {
                const text = chars[Math.floor(Math.random() * chars.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if(drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
            }
        }
        setInterval(drawMatrix, 33);
    </script>
""", height=500)


# =========================================================================
# SECTION 2: 3D AI CORE SIMULATOR
# =========================================================================
st.markdown('<div class="cinematic-section" style="background: radial-gradient(circle, rgba(10,20,10,0.6) 0%, rgba(1,2,3,1) 100%); border-radius: 12px; border: 1px solid rgba(0,255,65,0.3); padding: 40px; box-shadow: 0 20px 60px rgba(0,0,0,0.9);">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 3rem; text-align:center;">3D <span class="gradient-text">TELEMETRIC</span> KERNEL SIMULATOR</h2>', unsafe_allow_html=True)

# 3D Sphere Interactive Canvas
components.html("""
    <style>
        body { margin: 0; display:flex; flex-direction:column; align-items:center; font-family: 'Courier New', monospace; background: transparent; color: #fff; }
        .canvas-container { position: relative; width: 100%; max-width: 900px; }
        canvas { width: 100%; height: 500px; background: #010203; border: 2px solid #1a1f24; border-radius: 8px; cursor: crosshair; box-shadow: 0 10px 40px rgba(0,0,0,0.8); transition: box-shadow 0.5s; }
        .overlay-text { position: absolute; top: 20px; left: 0; width: 100%; text-align: center; pointer-events: none; z-index: 10; font-weight: bold; font-size: 1.2rem; text-shadow: 0 0 15px #000; color: #8b949e; letter-spacing: 2px;}
        .win-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 255, 65, 0.1); display: none; flex-direction: column; justify-content: center; align-items: center; border-radius: 8px; pointer-events: none; z-index: 20;}
        .win-overlay h2 { color: #00ff41; font-size: 4rem; text-shadow: 0 0 30px #00ff41; margin: 0; animation: pulse 0.5s infinite; }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
    </style>
    
    <div class="canvas-container">
        <div class="overlay-text" style="color:#00ff41; animation: pulse 2s infinite;">SIMULATOR: MOVE MOUSE TO ROTATE CORE <span style="color:#fff;">|</span> PRESS [SPACEBAR] TO HYPER-BLINK</div>
        <canvas id="simCanvas"></canvas>
        <div class="win-overlay" id="winScreen">
            <h2 id="winTitle">HYPERSPACE ENGAGED</h2>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('simCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = 900; canvas.height = 500;
        
        let mouseX = 0; let mouseY = 0;
        let isBlinking = false;
        let hyperspaceSpeed = 0;
        
        // 3D Sphere Mathematics
        const points = [];
        const numPoints = 250;
        const radius = 150;
        
        // Generate points on a sphere (Fibonacci lattice)
        const phi = Math.PI * (3 - Math.sqrt(5)); 
        for (let i = 0; i < numPoints; i++) {
            let y = 1 - (i / (numPoints - 1)) * 2; 
            let r = Math.sqrt(1 - y * y);
            let theta = phi * i;
            let x = Math.cos(theta) * r;
            let z = Math.sin(theta) * r;
            points.push({ x: x * radius, y: y * radius, z: z * radius, origZ: z * radius, origX: x*radius, origY: y*radius });
        }
        
        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            // Map mouse to center of screen -1 to 1
            mouseX = (((e.clientX - rect.left) / rect.width) * 2 - 1) * 2;
            mouseY = (((e.clientY - rect.top) / rect.height) * 2 - 1) * 2;
        });

        window.addEventListener('keydown', (e) => {
            if(e.code === 'Space' || e.key === ' ') {
                e.preventDefault();
                if (!isBlinking) {
                    isBlinking = true;
                    hyperspaceSpeed = 30; // Explosion force
                    document.getElementById('winScreen').style.display = "flex";
                    canvas.style.boxShadow = "0 0 80px rgba(0,255,65,0.8)";
                }
            }
        });
        window.addEventListener('keyup', (e) => {
            if(e.code === 'Space' || e.key === ' ') {
                isBlinking = false;
                document.getElementById('winScreen').style.display = "none";
                canvas.style.boxShadow = "0 10px 40px rgba(0,0,0,0.8)";
            }
        });

        // 3D Rotation Math
        function rotate3D(point, pitch, yaw) {
            let cosa = Math.cos(yaw), sina = Math.sin(yaw);
            let cosb = Math.cos(pitch), sinb = Math.sin(pitch);
            
            // Y-axis rotation (yaw)
            let x1 = point.x * cosa - point.z * sina;
            let z1 = point.x * sina + point.z * cosa;
            
            // X-axis rotation (pitch)
            let y2 = point.y * cosb - z1 * sinb;
            let z2 = point.y * sinb + z1 * cosb;
            
            return { x: x1, y: y2, z: z2 };
        }

        let baseAngle = 0;
        
        function animate() {
            requestAnimationFrame(animate);
            ctx.fillStyle = isBlinking ? 'rgba(0,20,0,0.3)' : 'rgba(1, 2, 3, 1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            baseAngle += 0.005; // Auto rotation
            let yaw = baseAngle + mouseX;
            let pitch = mouseY;
            
            // Hyperspace Physics
            if (isBlinking) {
                hyperspaceSpeed *= 1.05; // Accelerate outwards
            } else {
                hyperspaceSpeed *= 0.9; // Snap back
            }

            // Project and Draw
            ctx.translate(canvas.width / 2, canvas.height / 2);
            
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                
                // Explode z coordinate during blink
                p.x = p.origX * (1 + hyperspaceSpeed * 0.01);
                p.y = p.origY * (1 + hyperspaceSpeed * 0.01);
                p.z = p.origZ * (1 + hyperspaceSpeed * 0.01);
                
                let rotated = rotate3D(p, pitch, yaw);
                
                // 3D Perspective Projection
                let perspective = 400 / (400 + rotated.z);
                let px = rotated.x * perspective;
                let py = rotated.y * perspective;
                
                // Color scaling based on Z-depth
                let alpha = (rotated.z + radius) / (radius * 2);
                alpha = Math.max(0.1, Math.min(1, alpha));
                let size = perspective * (isBlinking ? 4 : 2);
                
                ctx.fillStyle = isBlinking ? `rgba(255, 255, 255, ${alpha})` : `rgba(0, 255, 65, ${alpha})`;
                
                ctx.beginPath();
                ctx.arc(px, py, size, 0, Math.PI * 2);
                ctx.fill();
                
                // Draw connecting lines to simulate wireframe mesh
                if (i > 0 && i % 3 === 0 && !isBlinking) {
                    let prevRotated = rotate3D(points[i-1], pitch, yaw);
                    let prevPersp = 400 / (400 + prevRotated.z);
                    ctx.strokeStyle = `rgba(0, 255, 65, ${alpha * 0.3})`;
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(px, py);
                    ctx.lineTo(prevRotated.x * prevPersp, prevRotated.y * prevPersp);
                    ctx.stroke();
                }
            }
            
            ctx.translate(-canvas.width / 2, -canvas.height / 2);
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
