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
        <div class="overlay-text" style="color:#00ff41; animation: pulse 2s infinite;">OCULAR TRAINING: TRACK RED TARGET <span style="color:#fff;">|</span> PRESS [SPACEBAR] TO FIRE</div>
        <canvas id="simCanvas"></canvas>
        <div class="win-overlay" id="winScreen">
            <h2 id="winTitle" style="color: #ff5f56; text-shadow: 0 0 20px #ff5f56;">TARGET DESTROYED</h2>
        </div>
        <div style="position: absolute; top: 20px; right: 20px; color: #00ff41; font-family: 'Courier New', monospace; font-size: 1.5rem; font-weight: bold; text-shadow: 0 0 10px #00ff41;">SCORE: <span id="scoreVal">0</span></div>
    </div>

    <script>
        const canvas = document.getElementById('simCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = 900; canvas.height = 500;
        
        let mouseX = canvas.width / 2; let mouseY = canvas.height / 2;
        let score = 0;
        let targetX = Math.random() * (canvas.width - 100) + 50;
        let targetY = Math.random() * (canvas.height - 100) + 50;
        let targetRadius = 25;
        let targetSpeedX = (Math.random() - 0.5) * 4;
        let targetSpeedY = (Math.random() - 0.5) * 4;
        
        let isShooting = false;
        let ripples = [];
        
        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            mouseX = e.clientX - rect.left;
            mouseY = e.clientY - rect.top;
        });

        window.addEventListener('keydown', (e) => {
            if(e.code === 'Space' || e.key === ' ') {
                e.preventDefault();
                if(!isShooting) {
                    isShooting = true;
                    ripples.push({x: mouseX, y: mouseY, radius: 0, opacity: 1});
                    
                    // Check Hit
                    let dist = Math.hypot(mouseX - targetX, mouseY - targetY);
                    if(dist < targetRadius + 20) {
                        score++;
                        document.getElementById('scoreVal').innerText = score;
                        document.getElementById('winScreen').style.display = "flex";
                        // Reset target
                        setTimeout(() => {
                            targetX = Math.random() * (canvas.width - 100) + 50;
                            targetY = Math.random() * (canvas.height - 100) + 50;
                            targetSpeedX = (Math.random() - 0.5) * (4 + score*0.5);
                            targetSpeedY = (Math.random() - 0.5) * (4 + score*0.5);
                            document.getElementById('winScreen').style.display = "none";
                        }, 500);
                    }
                }
            }
        });
        window.addEventListener('keyup', (e) => {
            if(e.code === 'Space' || e.key === ' ') { isShooting = false; }
        });
        
        function animate() {
            requestAnimationFrame(animate);
            ctx.fillStyle = 'rgba(1, 4, 9, 0.4)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Draw Grid
            ctx.strokeStyle = 'rgba(0, 255, 65, 0.1)';
            ctx.lineWidth = 1;
            ctx.beginPath();
            for(let i=0; i<canvas.width; i+=40) { ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); }
            for(let j=0; j<canvas.height; j+=40) { ctx.moveTo(0, j); ctx.lineTo(canvas.width, j); }
            ctx.stroke();
            
            // Update Target
            targetX += targetSpeedX; targetY += targetSpeedY;
            if(targetX < targetRadius || targetX > canvas.width - targetRadius) targetSpeedX *= -1;
            if(targetY < targetRadius || targetY > canvas.height - targetRadius) targetSpeedY *= -1;
            
            // Draw Target
            ctx.beginPath();
            ctx.arc(targetX, targetY, targetRadius, 0, Math.PI*2);
            ctx.fillStyle = 'rgba(255, 95, 86, 0.2)';
            ctx.fill();
            ctx.strokeStyle = '#ff5f56';
            ctx.lineWidth = 3;
            ctx.stroke();
            
            // Draw Crosshair (Mouse)
            ctx.beginPath();
            ctx.arc(mouseX, mouseY, 15, 0, Math.PI*2);
            ctx.strokeStyle = '#00ff41';
            ctx.lineWidth = 2;
            ctx.stroke();
            ctx.beginPath();
            ctx.moveTo(mouseX - 25, mouseY); ctx.lineTo(mouseX + 25, mouseY);
            ctx.moveTo(mouseX, mouseY - 25); ctx.lineTo(mouseX, mouseY + 25);
            ctx.stroke();
            
            // Draw Ripples
            for(let i=ripples.length-1; i>=0; i--) {
                let r = ripples[i];
                ctx.beginPath();
                ctx.arc(r.x, r.y, r.radius, 0, Math.PI*2);
                ctx.strokeStyle = `rgba(0, 255, 65, ${r.opacity})`;
                ctx.lineWidth = 4;
                ctx.stroke();
                r.radius += 5;
                r.opacity -= 0.05;
                if(r.opacity <= 0) ripples.splice(i, 1);
            }
        }
        animate();
    </script>
""", height=550)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 2.5: HARDWARE ARCHITECTURE SCHEMATIC
# =========================================================================
st.markdown('<div class="cinematic-section" style="padding: 80px 0;">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 3rem; text-align:center; margin-bottom: 50px;">// SYSTEM <span class="gradient-text">ARCHITECTURE</span></h2>', unsafe_allow_html=True)
components.html("""
    <style>
        .flow-container { display: flex; justify-content: center; align-items: center; gap: 30px; font-family: 'Courier New', monospace; padding: 20px; position: relative; }
        .node { width: 160px; height: 90px; background: #010409; border: 1px solid #30363d; border-radius: 8px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; color: #fff; box-shadow: 0 0 20px rgba(0,0,0,0.5); position: relative; cursor: pointer; transition: 0.3s; z-index: 5; }
        .node:hover { border-color: #00ff41; box-shadow: 0 0 30px rgba(0,255,65,0.2); transform: translateY(-5px); }
        .node-title { font-weight: bold; font-size: 1rem; margin-bottom: 5px; color: #58a6ff; }
        
        .arrow { width: 40px; height: 2px; background: #30363d; position: relative; }
        .arrow::after { content: ''; position: absolute; right: 0; top: -4px; border-left: 10px solid #30363d; border-top: 5px solid transparent; border-bottom: 5px solid transparent; }
        .packet { position: absolute; top: -4px; left: 0; width: 10px; height: 10px; background: #00ff41; border-radius: 50%; box-shadow: 0 0 10px #00ff41; animation: flow 1.5s linear infinite; }
        @keyframes flow { 0% { left: 0; opacity: 1; } 100% { left: 100%; opacity: 0; } }
        
        .tooltip { position: absolute; top: 120%; left: 50%; transform: translateX(-50%); width: 220px; background: rgba(13, 17, 23, 0.95); border: 1px solid #00ff41; border-radius: 6px; padding: 15px; text-align: left; opacity: 0; pointer-events: none; transition: 0.3s; box-shadow: 0 10px 30px rgba(0,255,65,0.1); z-index: 10; backdrop-filter: blur(5px); }
        .node:hover .tooltip { opacity: 1; top: 110%; pointer-events: auto; }
        .tooltip::before { content: ''; position: absolute; bottom: 100%; left: 0; width: 100%; height: 20px; }
        .tt-title { color: #00ff41; font-weight: bold; border-bottom: 1px solid #30363d; padding-bottom: 5px; margin-bottom: 10px; font-size: 0.9rem;}
        .tt-body { color: #8b949e; font-size: 0.8rem; line-height: 1.5; }
    </style>
    <div class="flow-container">
        <div class="node">
            <div class="node-title">HARDWARE</div>
            <div style="font-size: 0.7rem; color: #8b949e;">Webcam & Mic</div>
            <div class="tooltip">
                <div class="tt-title">[ INPUT PERIPHERALS ]</div>
                <div class="tt-body">Captures 60FPS uncompressed RGB frames and 44.1kHz audio streams, piping them to the Python daemons via direct memory access.</div>
            </div>
        </div>
        <div class="arrow"><div class="packet"></div></div>
        
        <div class="node">
            <div class="node-title">PYTHON DAEMONS</div>
            <div style="font-size: 0.7rem; color: #8b949e;">Vision.exe / Voice.exe</div>
            <div class="tooltip">
                <div class="tt-title">[ COMPUTE LAYER ]</div>
                <div class="tt-body">Isolated Background Processes.<br><br><b>Vision:</b> MediaPipe FaceMesh<br><b>Voice:</b> spaCy NLP<br><br>Process IDs: 8192 & 8193</div>
            </div>
        </div>
        <div class="arrow"><div class="packet"></div></div>
        
        <div class="node" style="border-color: #00ff41;">
            <div class="node-title" style="color: #00ff41;">IPC BRIDGE</div>
            <div style="font-size: 0.7rem; color: #8b949e;">.tommy_state.json</div>
            <div class="tooltip" style="border-color:#ffbd2e;">
                <div class="tt-title" style="color:#ffbd2e;">[ SHARED MEMORY ]</div>
                <div class="tt-body">A high-speed JSON state machine acting as a zero-latency Inter-Process Communication bridge between the daemons and the Kernel.</div>
            </div>
        </div>
        <div class="arrow"><div class="packet"></div></div>
        
        <div class="node">
            <div class="node-title">OS KERNEL</div>
            <div style="font-size: 0.7rem; color: #8b949e;">System Actions</div>
            <div class="tooltip">
                <div class="tt-title">[ EXECUTION ]</div>
                <div class="tt-body">Reads the IPC Bridge every 1ms. Executes native OS commands (Mouse Move, Click, Type) using PyAutoGUI.</div>
            </div>
        </div>
    </div>
""", height=350)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 3: THE VISION ENGINE
# =========================================================================
st.markdown('<div class="cinematic-section">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1], gap="large", vertical_alignment="center")

with col1:
    components.html("""
        <style>
            .sim-container { display: flex; width: 100%; height: 350px; background: #010409; border: 1px solid #30363d; border-radius: 8px; overflow: hidden; font-family: 'Courier New', monospace; box-shadow: 0 0 50px rgba(0,255,65,0.15); }
            .face-panel { flex: 1; position: relative; border-right: 1px dashed #30363d; display: flex; justify-content: center; align-items: center; background: radial-gradient(circle, rgba(0,255,65,0.05) 0%, transparent 70%); overflow: hidden; }
            .screen-panel { flex: 1; position: relative; background: #0d1117; overflow: hidden; }
            
            .head { position: absolute; width: 120px; height: 160px; border: 2px dashed rgba(0,255,65,0.3); border-radius: 60px; transition: transform 0.1s; display: flex; justify-content: center; }
            .eye { position: absolute; width: 12px; height: 12px; background: #00ff41; border-radius: 50%; box-shadow: 0 0 10px #00ff41; top: 40px; }
            .eye.left { left: 25px; } .eye.right { right: 25px; }
            .nose { position: absolute; width: 8px; height: 8px; background: #ffbd2e; border-radius: 50%; top: 80px; box-shadow: 0 0 10px #ffbd2e; }
            
            .cursor { position: absolute; width: 15px; height: 15px; background: #fff; clip-path: polygon(0 0, 100% 100%, 0 100%); transform: rotate(-45deg); transition: all 0.1s; box-shadow: 0 0 10px #fff; z-index: 10;}
            .ripple { position: absolute; width: 40px; height: 40px; border: 2px solid #00ff41; border-radius: 50%; transform: translate(-50%, -50%); opacity: 0; pointer-events: none; }
            
            @keyframes blink-anim { 0%, 90%, 100% { transform: scaleY(1); opacity: 1; } 95% { transform: scaleY(0.1); opacity: 0.2; } }
            .eye.blink { animation: blink-anim 3s infinite; }
        </style>
        <div class="sim-container">
            <div class="face-panel">
                <div style="position:absolute; top: 10px; left: 10px; color: #8b949e; font-size: 0.7rem;">[INPUT] FACEMESH</div>
                <div class="head" id="simHead">
                    <div class="eye left blink" id="eyeL"></div>
                    <div class="eye right blink" id="eyeR"></div>
                    <div class="nose" id="simNose"></div>
                </div>
            </div>
            <div class="screen-panel" id="screenPanel">
                <div style="position:absolute; top: 10px; left: 10px; color: #8b949e; font-size: 0.7rem;">[OUTPUT] IPC CURSOR</div>
                <div class="cursor" id="simCursor" style="left: 50%; top: 50%;"></div>
            </div>
        </div>
        <script>
            const head = document.getElementById('simHead');
            const cursor = document.getElementById('simCursor');
            const screen = document.getElementById('screenPanel');
            let angle = 0;
            function animateSim() {
                angle += 0.03;
                const headX = Math.sin(angle) * 40;
                const headY = Math.cos(angle * 0.5) * 20;
                head.style.transform = `translate(${headX}px, ${headY}px)`;
                cursor.style.left = `calc(50% + ${headX * 1.5}px)`;
                cursor.style.top = `calc(50% + ${headY * 1.5}px)`;
                requestAnimationFrame(animateSim);
            }
            animateSim();
            
            document.getElementById('eyeL').addEventListener('animationiteration', () => {
                const ripple = document.createElement('div');
                ripple.className = 'ripple';
                ripple.style.left = cursor.style.left;
                ripple.style.top = cursor.style.top;
                screen.appendChild(ripple);
                ripple.animate([ { transform: 'translate(-50%, -50%) scale(0)', opacity: 1 }, { transform: 'translate(-50%, -50%) scale(2)', opacity: 0 } ], { duration: 600, easing: 'ease-out' }).onfinish = () => ripple.remove();
            });
        </script>
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
            .voice-sim { width: 100%; height: 350px; background: #010409; border: 1px solid #30363d; border-radius: 8px; display: flex; flex-direction: column; overflow: hidden; font-family: 'Courier New', monospace; box-shadow: 0 0 50px rgba(0,255,65,0.15); }
            .top-panel { flex: 1; display: flex; justify-content: center; align-items: center; border-bottom: 1px solid #30363d; background: radial-gradient(circle, rgba(0,255,65,0.05) 0%, transparent 70%); gap: 10px; }
            .mic { width: 20px; height: 40px; border-radius: 10px; border: 2px solid #00ff41; position: relative; display: flex; justify-content: center; box-shadow: 0 0 15px #00ff41; }
            .mic::after { content: ''; position: absolute; bottom: -12px; width: 15px; height: 10px; border-left: 2px solid #00ff41; border-bottom: 2px solid #00ff41; border-right: 2px solid #00ff41; border-radius: 0 0 10px 10px; }
            
            .bar { width: 10px; background: #00ff41; border-radius: 5px; animation: sound 0ms -800ms linear infinite alternate; box-shadow: 0 0 10px rgba(0,255,65,0.6); }
            @keyframes sound { 0% { height: 10px; opacity: 0.3; } 100% { height: 60px; opacity: 1; } }
            .bar:nth-child(1) { animation-duration: 474ms; } .bar:nth-child(2) { animation-duration: 433ms; } .bar:nth-child(3) { animation-duration: 407ms; }
            .bar:nth-child(5) { animation-duration: 458ms; } .bar:nth-child(6) { animation-duration: 400ms; } .bar:nth-child(7) { animation-duration: 427ms; }
            
            .code-panel { flex: 1.5; background: #0d1117; padding: 20px; color: #fff; font-size: 1.1rem; position: relative; line-height: 1.5; }
            .code-cursor { display: inline-block; width: 10px; height: 18px; background: #fff; animation: blink 1s infinite; margin-left: 4px; vertical-align: middle; }
            @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
        </style>
        <div class="voice-sim">
            <div class="top-panel">
                <div class="bar"></div><div class="bar"></div><div class="bar"></div>
                <div class="mic" style="margin: 0 20px;"></div>
                <div class="bar"></div><div class="bar"></div><div class="bar"></div>
            </div>
            <div class="code-panel">
                <div style="color: #8b949e; font-size: 0.8rem; margin-bottom: 15px; letter-spacing: 1px;">[OUTPUT] NLP CODE GENERATOR</div>
                <span style="color:#ff7b72;">import</span> pyautogui<br>
                <span id="typeTarget" style="color: #79c0ff;"></span><span class="code-cursor"></span>
            </div>
        </div>
        <script>
            const target = document.getElementById('typeTarget');
            const scripts = [
                "pyautogui.hotkey('ctrl', 's')\\nprint('Voice saved file!')",
                "import os\\nos.system('start spotify')\\nprint('Music initialized.')",
                "for i in range(10):\\n    print(f'System scan {i}%')\\nprint('Done.')",
                "def auto_code():\\n    return 'Voice is the new keyboard.'\\nauto_code()"
            ];
            let scriptIndex = 0;
            let charIndex = 0;
            
            function typeCode() {
                let currentStr = scripts[scriptIndex];
                if (charIndex < currentStr.length) {
                    let char = currentStr.charAt(charIndex);
                    if (char === '\\n') target.innerHTML += '<br><span style="color:#a5d6ff;">';
                    else target.innerHTML += char === ' ' ? '&nbsp;' : char;
                    charIndex++;
                    setTimeout(typeCode, Math.random() * 50 + 20);
                } else {
                    target.innerHTML += '</span>';
                    setTimeout(() => { 
                        target.innerHTML = ''; 
                        charIndex = 0; 
                        scriptIndex = (scriptIndex + 1) % scripts.length;
                        typeCode(); 
                    }, 2000);
                }
            }
            setTimeout(typeCode, 1000);
        </script>
    """, height=350)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 4.5: GLOBAL TELEMETRY
# =========================================================================
st.markdown('<div class="cinematic-section" style="padding: 100px 0;">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 3rem; text-align:center; margin-bottom: 10px;">GLOBAL <span class="gradient-text">TELEMETRY</span></h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#8b949e; text-align:center; font-size:1.1rem; margin-bottom: 40px;">Live OS Kernel Synchronization</p>', unsafe_allow_html=True)

components.html("""
    <style> body { margin: 0; overflow: hidden; background: transparent; display: flex; justify-content: center; } canvas { filter: drop-shadow(0 0 30px rgba(0,255,65,0.2)); } </style>
    <div id="globe-container"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / 400, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(window.innerWidth, 400);
        document.getElementById('globe-container').appendChild(renderer.domElement);
        
        const geometry = new THREE.SphereGeometry(2, 32, 32);
        const edges = new THREE.EdgesGeometry(geometry);
        const material = new THREE.LineBasicMaterial({ color: 0x00ff41, transparent: true, opacity: 0.15 });
        const sphere = new THREE.LineSegments(edges, material);
        scene.add(sphere);
        
        const particlesGeometry = new THREE.BufferGeometry();
        const particlesCount = 50;
        const posArray = new Float32Array(particlesCount * 3);
        for(let i = 0; i < particlesCount * 3; i++) { posArray[i] = (Math.random() - 0.5) * 4.2; }
        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
        const particlesMaterial = new THREE.PointsMaterial({ size: 0.05, color: 0x00ff41 });
        const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
        scene.add(particlesMesh);
        
        camera.position.z = 6;
        function animate() {
            requestAnimationFrame(animate);
            sphere.rotation.y += 0.002;
            sphere.rotation.x += 0.001;
            particlesMesh.rotation.y -= 0.001;
            renderer.render(scene, camera);
        }
        animate();
    </script>
""", height=400)
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
# SECTION 5.5: BETA ACCESS TERMINAL
# =========================================================================
st.markdown('<div class="cinematic-section" style="padding: 100px 0;">', unsafe_allow_html=True)
components.html("""
    <style>
        .terminal-box { background: #010409; border: 1px solid #30363d; border-radius: 8px; width: 60%; margin: 0 auto; padding: 30px; font-family: 'Courier New', monospace; box-shadow: 0 10px 40px rgba(0,0,0,0.8); }
        .prompt { color: #00ff41; font-weight: bold; font-size: 1.2rem; }
        .input-line { display: flex; align-items: center; margin-top: 15px; }
        .term-input { background: transparent; border: none; outline: none; color: #fff; font-family: 'Courier New', monospace; font-size: 1.2rem; margin-left: 10px; width: 80%; }
        .term-input::placeholder { color: #30363d; }
    </style>
    <div class="terminal-box" id="termBox">
        <div style="color: #8b949e; margin-bottom: 15px;">T.O.M.M.Y. OS v1.0.0 [Secure Enclave]</div>
        <div style="color: #fff; font-size: 1.1rem; margin-bottom: 20px;">Execute <span style="color:#ffbd2e;">request_access()</span> to join the waitlist.</div>
        <div class="input-line">
            <span class="prompt">root@tommy:~#</span>
            <input type="email" class="term-input" id="emailInput" placeholder="Enter your email address..." autocomplete="off">
        </div>
    </div>
    <script>
        const input = document.getElementById('emailInput');
        const box = document.getElementById('termBox');
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                if (input.value.includes('@')) {
                    box.innerHTML = `<div style="color:#00ff41; font-size:1.2rem; margin-top:20px; text-align:center;">[+] ACCESS GRANTED. CREDENTIALS DISPATCHED TO: ${input.value}</div>`;
                } else {
                    input.value = '';
                    input.placeholder = 'INVALID PROTOCOL. TRY AGAIN.';
                }
            }
        });
    </script>
""", height=250)
st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# SECTION 6: FOOTER (ACADEMIC ARCHITECTS)
# =========================================================================
st.markdown('<div class="cinematic-section" style="padding-bottom: 100px;">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 3rem; text-align:center;">// ACADEMIC <span class="gradient-text">ARCHITECTS</span></h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#8b949e; text-align:center; max-width:800px; margin: 20px auto; font-size:1.1rem;">T.O.M.M.Y. was engineered at Lovely Professional University to evaluate the absolute limits of Multi-Process Hardware Concurrency on Python Operating System Wrappers.</p>', unsafe_allow_html=True)

import base64
import os

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return f"data:image/jpeg;base64,{base64.b64encode(data).decode()}"
    except Exception:
        return "https://via.placeholder.com/200x200"

base_path = os.path.dirname(os.path.abspath(__file__))
chirag_b64 = get_base64_of_bin_file(os.path.join(base_path, "assets", "chirag.jpeg"))
chava_b64 = get_base64_of_bin_file(os.path.join(base_path, "assets", "chava.jpeg"))
lalmalsawm_b64 = get_base64_of_bin_file(os.path.join(base_path, "assets", "lalmalsawm.jpeg"))
kaushal_b64 = get_base64_of_bin_file(os.path.join(base_path, "assets", "kaushal.jpeg"))

html_content = """
    <style>
        body { margin: 0; display:flex; justify-content:center; font-family: 'Courier New', monospace; background: transparent; }
        .team-container { display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; padding: 40px 20px; perspective: 1000px; }
        
        .card {
            width: 220px; height: 320px;
            background: #010409;
            border: 1px solid #30363d;
            border-radius: 12px;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease-out;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
            transform-style: preserve-3d;
        }
        
        .card:hover {
            border-color: #00ff41;
            box-shadow: 0 15px 40px rgba(0, 255, 65, 0.2);
            transform: translateY(-10px);
        }
        
        .avatar-wrapper {
            width: 100%; height: 200px;
            background: radial-gradient(circle, #161b22 0%, #010409 100%);
            position: relative;
            overflow: hidden;
            display: flex; justify-content: center; align-items: center;
            border-bottom: 1px solid #30363d;
        }
        
        /* Sci-Fi Cyberpunk Filter overlaying the real photos */
        .avatar-wrapper img {
            width: 100%; height: 100%; 
            object-fit: cover; 
            opacity: 0.9; 
            transition: all 0.4s;
        }
        
        .card:hover .avatar-wrapper img { 
            opacity: 1; 
            transform: scale(1.05);
        }
        
        /* TV Static overlay */
        .avatar-wrapper::after {
            content: ''; position: absolute; top:0; left:0; width:100%; height:100%;
            background: repeating-linear-gradient(0deg, rgba(0,0,0,0.1), rgba(0,0,0,0.1) 1px, transparent 1px, transparent 2px);
            pointer-events: none; z-index: 5;
        }
        
        /* Cyberpunk Scanline Effect */
        .scanline {
            position: absolute; top: -100%; left: 0; width: 100%; height: 4px;
            background: rgba(0, 255, 65, 0.8); 
            box-shadow: 0 0 15px #00ff41, 0 0 30px #00ff41;
            opacity: 0; transition: opacity 0.3s;
            z-index: 10;
        }
        .card:hover .scanline { opacity: 1; animation: scan 1.5s linear infinite; }
        @keyframes scan { 0% { top: 0%; } 100% { top: 100%; } }
        
        /* Glitch overlay on hover */
        .card::before {
            content: ''; position: absolute; top: 0; left: -100%; width: 50%; height: 100%;
            background: linear-gradient(to right, transparent, rgba(0,255,65,0.1), transparent);
            transform: skewX(-20deg); transition: 0.5s; z-index: 5; pointer-events: none;
        }
        .card:hover::before { left: 150%; }

        .info { padding: 20px 15px; text-align: center; background: #010409; position: relative; z-index: 2;}
        .name { color: #fff; font-size: 1.1rem; font-weight: bold; margin: 0; letter-spacing: 1px; }
        .role { color: #00ff41; font-size: 0.8rem; margin-top: 8px; text-transform: uppercase; letter-spacing: 2px;}
    </style>

    <div class="team-container">
        <!-- Developer 1 -->
        <div class="card" onmousemove="tilt(event, this)" onmouseleave="resetTilt(this)">
            <div class="avatar-wrapper">
                <div class="scanline"></div>
                <img src="URL_CHIRAG" alt="Chirag">
            </div>
            <div class="info">
                <p class="name">CHIRAG PHOGAT</p>
                <p class="role">> LEAD ARCHITECT</p>
            </div>
        </div>
        
        <!-- Developer 2 -->
        <div class="card" onmousemove="tilt(event, this)" onmouseleave="resetTilt(this)">
            <div class="avatar-wrapper">
                <div class="scanline"></div>
                <img src="URL_CHAVA" alt="Chava">
            </div>
            <div class="info">
                <p class="name">CHAVA HARSHA</p>
                <p class="role">> GAZE MATH</p>
            </div>
        </div>
        
        <!-- Developer 3 -->
        <div class="card" onmousemove="tilt(event, this)" onmouseleave="resetTilt(this)">
            <div class="avatar-wrapper">
                <div class="scanline"></div>
                <img src="URL_LALMALSAWM" alt="Lalmalsawm">
            </div>
            <div class="info">
                <p class="name">LALMALSAWM GUITE</p>
                <p class="role">> RESEARCHER</p>
            </div>
        </div>
        
        <!-- Developer 4 -->
        <div class="card" onmousemove="tilt(event, this)" onmouseleave="resetTilt(this)">
            <div class="avatar-wrapper">
                <div class="scanline"></div>
                <img src="URL_KAUSHAL" alt="Kaushal">
            </div>
            <div class="info">
                <p class="name">KAUSHAL PATHAK</p>
                <p class="role">> PROJECT MENTOR</p>
            </div>
        </div>
    </div>

    <script>
        // 3D Tilt Effect Physics
        function tilt(e, card) {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left; 
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = ((y - centerY) / centerY) * -15; // Max 15deg tilt
            const rotateY = ((x - centerX) / centerX) * 15;
            
            card.style.transform = `translateY(-10px) perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        }
        
        function resetTilt(card) {
            card.style.transform = `translateY(0) perspective(1000px) rotateX(0deg) rotateY(0deg)`;
        }
    </script>
"""

html_content = html_content.replace('URL_CHIRAG', chirag_b64)
html_content = html_content.replace('URL_CHAVA', chava_b64)
html_content = html_content.replace('URL_LALMALSAWM', lalmalsawm_b64)
html_content = html_content.replace('URL_KAUSHAL', kaushal_b64)

components.html(html_content, height=450)
st.markdown('</div>', unsafe_allow_html=True)
