import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="T.O.M.M.Y. OS",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================================
# GLOBAL CSS - UNIFIED DASHBOARD
# =========================================================================
st.markdown("""
    <style>
        .stApp {
            background-color: #050505;
            color: #e6e6e6;
            font-family: 'Inter', sans-serif;
            overflow: hidden;
        }
        header, #MainMenu, footer { visibility: hidden; }
        .block-container { padding-top: 1rem; max-width: 1800px; padding-bottom: 0rem;}
        
        h1, h2, h3, h4 { font-family: 'Courier New', monospace; font-weight: 900; text-transform: uppercase; margin-bottom: 5px; color: #fff;}
        .neon-green { color: #00ff41; }
        
        .dash-panel {
            background: rgba(10, 15, 10, 0.8);
            border: 1px solid rgba(0, 255, 65, 0.3);
            border-radius: 8px;
            padding: 20px;
            box-shadow: inset 0 0 20px rgba(0, 255, 65, 0.05);
            height: 100%;
        }
        
        .footer-bar {
            background: #020202;
            border-top: 1px solid #00ff41;
            padding: 15px;
            text-align: center;
            margin-top: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

# Main Grid: Left Panel (Vision), Center Panel (Simulator), Right Panel (Voice/Terminal)
col_left, col_center, col_right = st.columns([1, 1.8, 1], gap="medium")

# =========================================================================
# LEFT PANEL: VISION & TELEMETRY
# =========================================================================
with col_left:
    st.markdown('<div class="dash-panel">', unsafe_allow_html=True)
    st.markdown('<h3><span class="neon-green">>></span> TELEMETRIC ENGINE</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color:#8b949e; font-size:0.9rem;">FaceMesh Node-1 Lock-On Matrix active. Bypassing biological arm jitter via strict Euclidean limits.</p>', unsafe_allow_html=True)
    
    # Radar Component
    components.html("""
        <style>
            body { margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; background: transparent; }
            .radar { width: 200px; height: 200px; border-radius: 50%; border: 2px solid #00ff41; overflow: hidden; position: relative; box-shadow: 0 0 30px rgba(0,255,65,0.2); margin-top: 10px;}
            .radar::after { content: ''; position: absolute; width: 100px; height: 100px; background: linear-gradient(45deg, rgba(0,255,65,0.8) 0%, transparent 50%); transform-origin: bottom right; top: 0; left: 0; animation: scan 2s linear infinite; }
            .grid { position: absolute; width: 100%; height: 100%; background-image: linear-gradient(#00ff41 1px, transparent 1px), linear-gradient(90deg, #00ff41 1px, transparent 1px); background-size: 20px 20px; opacity: 0.15; }
            .face-mesh { position: absolute; width: 50px; height: 75px; border: 1px dashed #00ff41; top: 30%; left: 35%; border-radius: 50%; animation: pulse 1s infinite; }
            @keyframes scan { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(0,255,65,0.4); } 70% { box-shadow: 0 0 0 15px rgba(0,255,65,0); } 100% { box-shadow: 0 0 0 0 rgba(0,255,65,0); } }
        </style>
        <div class="radar"><div class="grid"></div><div class="face-mesh"></div></div>
    """, height=220)
    
    st.markdown('<hr style="border-color: rgba(0, 255, 65, 0.2);">', unsafe_allow_html=True)
    
    # Live Metrics Component
    components.html("""
        <div style="font-family: 'Courier New', monospace; text-align: center;">
            <div style="margin-bottom: 15px; background: rgba(0,255,65,0.1); border: 1px solid #00ff41; padding: 10px;">
                <div style="color: #8b949e; font-size: 0.8rem;">VISION LATENCY</div>
                <div style="color: #fff; font-size: 2rem; font-weight: bold;" id="met1">18.0<span style="color:#00ff41; font-size:1rem;">ms</span></div>
            </div>
            <div style="background: rgba(0,255,65,0.1); border: 1px solid #00ff41; padding: 10px;">
                <div style="color: #8b949e; font-size: 0.8rem;">IPC SYNCHRONIZATION</div>
                <div style="color: #fff; font-size: 2rem; font-weight: bold;" id="met2">60.0<span style="color:#00ff41; font-size:1rem;">FPS</span></div>
            </div>
        </div>
        <script>
            setInterval(() => {
                document.getElementById('met1').innerHTML = (17 + Math.random() * 2).toFixed(1) + '<span style="color:#00ff41; font-size:1rem;">ms</span>';
                document.getElementById('met2').innerHTML = (59 + Math.random() * 2).toFixed(1) + '<span style="color:#00ff41; font-size:1rem;">FPS</span>';
            }, 800);
        </script>
    """, height=220)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# CENTER PANEL: HERO & SIMULATOR
# =========================================================================
with col_center:
    # Glitch Hero
    components.html("""
        <style>
            .glitch-wrapper { display: flex; flex-direction: column; justify-content: center; align-items: center; padding-top: 10px; }
            .glitch { font-size: 5rem; font-weight: 900; text-transform: uppercase; position: relative; color: #fff; letter-spacing: 10px; font-family: 'Courier New', monospace; text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.025em -0.05em 0 rgba(0,255,0,0.75), 0.025em 0.05em 0 rgba(0,0,255,0.75); animation: glitch 500ms infinite; margin: 0; line-height: 1;}
            @keyframes glitch { 0% { text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.05em -0.025em 0 rgba(0,255,0,0.75), -0.025em 0.05em 0 rgba(0,0,255,0.75); } 20% { text-shadow: -0.05em -0.025em 0 rgba(255,0,0,0.75), 0.025em 0.025em 0 rgba(0,255,0,0.75), -0.05em -0.05em 0 rgba(0,0,255,0.75); } 40% { text-shadow: 0.025em 0.05em 0 rgba(255,0,0,0.75), 0.05em 0 0 rgba(0,255,0,0.75), 0 -0.05em 0 rgba(0,0,255,0.75); } 60% { text-shadow: -0.025em 0 0 rgba(255,0,0,0.75), -0.025em -0.025em 0 rgba(0,255,0,0.75), -0.025em -0.05em 0 rgba(0,0,255,0.75); } 80% { text-shadow: 0.05em -0.05em 0 rgba(255,0,0,0.75), 0.025em 0.05em 0 rgba(0,255,0,0.75), -0.05em -0.025em 0 rgba(0,0,255,0.75); } 100% { text-shadow: -0.025em 0.05em 0 rgba(255,0,0,0.75), -0.05em -0.05em 0 rgba(0,255,0,0.75), 0.025em 0 0 rgba(0,0,255,0.75); } }
            .sub-glitch { color: #00ff41; font-size: 1rem; letter-spacing: 3px; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00ff41; margin-top: 10px;}
        </style>
        <div class="glitch-wrapper">
            <div class="glitch" data-text="T.O.M.M.Y.">T.O.M.M.Y.</div>
            <div class="sub-glitch">TELEMETRIC OPTICAL & MULTIMODAL KERNEL</div>
        </div>
    """, height=120)

    # Interactive Simulator Sandbox
    st.markdown('<div class="dash-panel" style="padding: 10px; display: flex; flex-direction: column; align-items: center; border: 2px solid #00ff41;">', unsafe_allow_html=True)
    st.markdown('<h4 style="text-align: center; font-size: 1.5rem; letter-spacing: 2px;">INTERACTIVE PHYSICS SIMULATOR</h4>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color:#8b949e; font-size:0.9rem; margin-bottom: 5px;">Use your mouse to track the red target. Keep your cursor inside the 55-pixel Euclidean boundary to lock the Telemetric Engine!</p>', unsafe_allow_html=True)
    
    components.html("""
        <style> body {margin: 0; display:flex; flex-direction:column; align-items:center; background: transparent;} </style>
        <canvas id="simCanvas" style="border: 1px solid #30363d; border-radius: 4px; background: #010409; cursor: crosshair; width: 100%; height: 350px;"></canvas>
        <div style="margin-top: 10px; width: 100%; height: 12px; background: #111; border-radius: 6px; overflow: hidden; border: 1px solid #333;">
            <div id="lockBar" style="width: 0%; height: 100%; background: #00ff41; transition: width 0.1s;"></div>
        </div>
        <div id="simStatus" style="color:#8b949e; font-family:'Courier New', monospace; font-size: 14px; margin-top: 5px; font-weight: bold; text-align: center;">STATUS: AWAITING TARGET ACQUISITION</div>
        
        <script>
            const canvas = document.getElementById('simCanvas');
            const ctx = canvas.getContext('2d');
            
            function resizeCanvas() {
                canvas.width = canvas.offsetWidth;
                canvas.height = canvas.offsetHeight;
            }
            window.addEventListener('resize', resizeCanvas);
            resizeCanvas();
            
            let mouseX = canvas.width / 2; let mouseY = canvas.height / 2;
            let targetX = canvas.width / 2; let targetY = canvas.height / 2;
            let tVx = 4; let tVy = 4;
            let lockScore = 0;
            
            canvas.addEventListener('mousemove', (e) => {
                const rect = canvas.getBoundingClientRect();
                mouseX = e.clientX - rect.left;
                mouseY = e.clientY - rect.top;
            });

            function animate() {
                requestAnimationFrame(animate);
                ctx.fillStyle = '#010409';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                // Draw Matrix Grid
                ctx.strokeStyle = "rgba(0, 255, 65, 0.1)";
                ctx.lineWidth = 1;
                for(let i=0; i<canvas.width; i+=40) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke(); }
                for(let i=0; i<canvas.height; i+=40) { ctx.beginPath(); ctx.moveTo(0,i); ctx.lineTo(canvas.width,i); ctx.stroke(); }
                
                // Move Target
                targetX += tVx; targetY += tVy;
                if(targetX < 20 || targetX > canvas.width - 20) { tVx *= -1; tVx += (Math.random() - 0.5)*2; }
                if(targetY < 20 || targetY > canvas.height - 20) { tVy *= -1; tVy += (Math.random() - 0.5)*2; }
                
                tVx = Math.max(-6, Math.min(6, tVx));
                tVy = Math.max(-6, Math.min(6, tVy));

                // Draw Target
                ctx.beginPath(); ctx.arc(targetX, targetY, 12, 0, Math.PI * 2);
                ctx.fillStyle = '#F85149'; ctx.fill();
                
                // Math
                let dx = mouseX - targetX;
                let dy = mouseY - targetY;
                let distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 55) {
                    ctx.strokeStyle = '#00ff41'; ctx.lineWidth = 2;
                    lockScore = Math.min(100, lockScore + 1.5);
                    document.getElementById('simStatus').innerText = "STATUS: TELEMETRIC LOCK ENGAGED";
                    document.getElementById('simStatus').style.color = "#00ff41";
                    canvas.style.boxShadow = "inset 0 0 30px rgba(0,255,65,0.4)";
                } else {
                    ctx.strokeStyle = '#8b949e'; ctx.lineWidth = 1;
                    lockScore = Math.max(0, lockScore - 2);
                    document.getElementById('simStatus').innerText = "STATUS: TRACKING TARGET...";
                    document.getElementById('simStatus').style.color = "#8b949e";
                    canvas.style.boxShadow = "none";
                }
                
                document.getElementById('lockBar').style.width = lockScore + "%";
                
                // Cursor Collision Box
                ctx.beginPath(); ctx.arc(mouseX, mouseY, 55, 0, Math.PI * 2); ctx.stroke();
                
                // Connection Line
                ctx.beginPath(); ctx.moveTo(mouseX, mouseY); ctx.lineTo(targetX, targetY); ctx.stroke();
            }
            animate();
        </script>
    """, height=400)
    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# RIGHT PANEL: VOICE & TERMINAL
# =========================================================================
with col_right:
    st.markdown('<div class="dash-panel">', unsafe_allow_html=True)
    st.markdown('<h3><span class="neon-green">>></span> OFFLINE VOICE CORE</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color:#8b949e; font-size:0.9rem;">LLMs are banned from the logic loop. Deterministic spaCy syntactical routing handles NLP locally.</p>', unsafe_allow_html=True)
    
    # Audio Waveform Component
    components.html("""
        <style>
            body { margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; background: transparent; }
            .wave-container { display: flex; align-items: center; justify-content: center; height: 100px; gap: 4px; margin-top: 10px; }
            .bar { width: 12px; background: #00ff41; border-radius: 6px; animation: sound 0ms -800ms linear infinite alternate; box-shadow: 0 0 10px #00ff41; }
            @keyframes sound { 0% { height: 10px; opacity: 0.3; } 100% { height: 80px; opacity: 1; } }
            .bar:nth-child(1) { animation-duration: 474ms; } .bar:nth-child(2) { animation-duration: 433ms; }
            .bar:nth-child(3) { animation-duration: 407ms; } .bar:nth-child(4) { animation-duration: 458ms; }
            .bar:nth-child(5) { animation-duration: 400ms; } .bar:nth-child(6) { animation-duration: 427ms; }
            .bar:nth-child(7) { animation-duration: 441ms; }
        </style>
        <div class="wave-container">
            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
            <div class="bar"></div><div class="bar"></div><div class="bar"></div>
        </div>
    """, height=120)
    
    st.markdown('<hr style="border-color: rgba(0, 255, 65, 0.2);">', unsafe_allow_html=True)
    
    st.markdown('<h4>>_ SANDBOX DEPLOYMENT</h4>', unsafe_allow_html=True)
    # Terminal Emulator Component
    components.html("""
        <div style="background: #010409; border: 1px solid #30363d; border-radius: 4px; font-family: 'Courier New', monospace; padding: 10px; height: 200px; overflow: hidden; position: relative; box-shadow: inset 0 0 10px #000;">
            <div style="color: #8b949e; font-size: 0.8rem; margin-bottom: 5px; border-bottom: 1px solid #333; padding-bottom: 3px;">setup.bat - PowerShell Handoff</div>
            <div id="term" style="color: #fff; font-size: 0.85rem; line-height: 1.4;"></div>
        </div>
        <script>
            const lines = [
                "<span style='color:#00ff41;'>C:\\></span> git clone tommy-os",
                "<span style='color:#00ff41;'>C:\\></span> .\\\\setup.bat",
                "<span style='color:#8b949e;'>[+] Building Virtual Sandbox... DONE</span>",
                "<span style='color:#8b949e;'>[+] Bypassing Exec Policies... DONE</span>",
                "<span style='color:#3fb950; font-weight:bold;'>PS C:\\></span> python tommy_os.py"
            ];
            let out = document.getElementById("term");
            let i = 0;
            function runTerm() {
                if(i < lines.length) {
                    out.innerHTML += lines[i] + "<br>";
                    i++;
                    setTimeout(runTerm, 600);
                } else {
                    out.innerHTML += "<span style='animation: blink 1s infinite;'>█</span>";
                    document.head.insertAdjacentHTML("beforeend", `<style>@keyframes blink { 50% { opacity: 0; } }</style>`);
                }
            }
            setTimeout(runTerm, 500);
        </script>
    """, height=220)
    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# BOTTOM BAR: FOOTER & DOWNLOAD
# =========================================================================
st.markdown('<div class="footer-bar">', unsafe_allow_html=True)
c_f1, c_f2, c_f3 = st.columns([1, 2, 1], vertical_alignment="center")

with c_f1:
    st.markdown("""
        <div style="font-family:'Courier New', monospace; color:#8b949e; font-size:0.8rem; text-align: left;">
            <b>ARCHITECTS:</b><br>
            C. Phogat, C. Harshavardhan,<br>
            L. Guite, K. Pathak<br>
            LPU Engineering © 2026
        </div>
    """, unsafe_allow_html=True)

with c_f2:
    st.markdown("""
        <div style="text-align: center;">
            <a href="https://github.com/chiragphogat/tommy-os" target="_blank" style="background: #00ff41; color: #000; padding: 10px 40px; font-size: 1.2rem; font-family: 'Courier New', monospace; font-weight: 900; text-decoration: none; border-radius: 4px; display: inline-block; box-shadow: 0 0 20px rgba(0, 255, 65, 0.4); transition: transform 0.2s;">[ GET T.O.M.M.Y. OS ]</a>
        </div>
    """, unsafe_allow_html=True)

with c_f3:
    try:
        with open("assets/T.O.M.M.Y_Research.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 IEEE PAPER PDF",
                data=pdf_file,
                file_name="TOMMY_Research_Paper.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except FileNotFoundError:
        st.error("⚠️ PDF Not Found in /assets/")

st.markdown('</div>', unsafe_allow_html=True)
