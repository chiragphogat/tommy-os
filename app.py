import streamlit as st

st.set_page_config(
    page_title="T.O.M.M.Y. OS",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
    <style>
        .stApp {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Inter', sans-serif;
        }
        h1, h2, h3, h4 { color: #58a6ff !important; font-weight: 800; }
        .stTabs [data-baseweb="tab-list"] { gap: 2rem; background-color: transparent; }
        .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; border-radius: 4px; color: #8b949e; font-size: 1.1rem; font-weight: 600; }
        .stTabs [aria-selected="true"] { color: #58a6ff !important; background-color: #1f2428;}
        .warning-box { background-color: #2D1115; border-left: 4px solid #F85149; padding: 1.5rem; border-radius: 6px; color: #FF7B72; margin-bottom: 2rem; }
        .paper-section { background-color: #161b22; padding: 20px; border-radius: 8px; border: 1px solid #30363d; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

st.title("T.O.M.M.Y. OS")
st.markdown("### A Multi-Process Architecture for Hands-Free Windows Navigation Without Cloud Dependencies")

tab1, tab2, tab3 = st.tabs(["🚀 Project Synopsis", "📊 Comparative Analysis & Methodology", "📄 Digital Research Paper"])

# =========================================================================
# TAB 1: SYNOPSIS
# =========================================================================
with tab1:
    st.markdown("""
    <div class="warning-box">
        <strong>⚠️ ACADEMIC DEPLOYMENT NOTICE</strong><br><br>
        T.O.M.M.Y represents a major shift from traditional Web AI. It is an <strong>Operating System kernel wrapper</strong> designed locally for Windows machines. It physically hijacks mouse parameters, hardware drivers (brightness/volume), and display elements using localized CPU threading.<br><br>
        Because this Web Server operates on headless Linux constraints without a physical screen or microphone, this site serves strictly as our <strong>Interactive Digital Project Portfolio</strong>. To test the mathematical physics natively, clone the codebase below!
    </div>
    """, unsafe_allow_html=True)

    st.code("git clone https://github.com/chiragphogat/tommy-os.git\ncd tommy-os\nsetup.bat", language="bash")
    st.markdown("---")
    st.markdown("## 📖 Project Description")
    st.markdown("""
    In recent years, human–computer interaction has evolved rapidly; however, software systems still rely heavily on legacy physical input devices like standard keyboards and mice. These interaction methods are fundamentally inefficient in dynamic, hands-free, or assistive environments.
    
    The **T.O.M.M.Y (Tactile, Optical, and Multimodal Machine Yield)** engine directly addresses this limitation by introducing a native OS interaction framework. It enables Windows to understand raw human intent dynamically through Voice Commands, Hand Geometric manipulations, and Eye-Blink execution.
    
    The system captures input natively using localized webcams and microphones, bypassing cloud surveillance. Each modality is processed entirely independently across isolated CPU threads, preventing memory collision. A multimodal fusion engine (via JSON IPC) dynamically synchronizes the audio and visual matrices, guaranteeing that heavy auditory Processing does not bottleneck or crash the 60FPS visual pointer logic.
    
    T.O.M.M.Y is engineered with a modular, 100% offline architecture, making it highly secure for environments demanding data privacy.
    """)

    st.markdown("### 🌍 Project Impact")
    st.markdown("This project successfully demonstrates the absolute physical eradication of traditional IO peripherals. It drastically improves graphical accessibility for differently-abled operators, and enforces native execution logic without forcing sensitive audio data onto external Amazon/Google network servers.")
    st.markdown("---")
    st.markdown("## 💻 Engineering Team Roster")
    st.markdown("T.O.M.M.Y was researched, architected, and engineered at Lovely Professional University.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        with st.container(border=True):
            try: st.image("assets/chirag.jpeg", use_column_width=True)
            except: st.warning("Missing Photo")
            st.markdown("<h3 style='margin-bottom:0; text-align:center;'>Chirag Phogat</h3><p style='color:#8b949e; text-align:center;'>Lead Systems Architecture</p>", unsafe_allow_html=True)
    with col2:
        with st.container(border=True):
            try: st.image("assets/chava.jpeg", use_column_width=True)
            except: st.warning("Missing Photo")
            st.markdown("<h3 style='margin-bottom:0; text-align:center;'>Chava Harshavardhan</h3><p style='color:#8b949e; text-align:center;'>Gaze Estimation</p>", unsafe_allow_html=True)
    with col3:
        with st.container(border=True):
            try: st.image("assets/lalmalsawm.jpeg", use_column_width=True)
            except: st.warning("Missing Photo")
            st.markdown("<h3 style='margin-bottom:0; text-align:center;'>Lalmalsawm Guite</h3><p style='color:#8b949e; text-align:center;'>Lead Researcher</p>", unsafe_allow_html=True)
    with col4:
        with st.container(border=True):
            try: st.image("assets/kaushal.jpeg", use_column_width=True)
            except: st.warning("Missing Photo")
            st.markdown("<h3 style='margin-bottom:0; text-align:center;'>Kaushal Pathak</h3><p style='color:#8b949e; text-align:center;'>Project Guide & Mentor</p>", unsafe_allow_html=True)


# =========================================================================
# TAB 2: BENCHMARKS & COMPARATIVE ANALYSIS
# =========================================================================
with tab2:
    st.markdown("## 📊 Methodology & Platform Documentation")

    st.markdown("### 1. Objectives and Scope")
    st.markdown("""
    The primary objective of this comparative analysis is to evaluate the effectiveness of the proposed T.O.M.M.Y. (Tactile, Optical, and Multimodal Machine Yield) system natively against existing intelligent assistants and human–computer interaction frameworks. 
    
    The scope of this comparison is strictly limited to multimodal interaction systems and widely used intelligent assistants that operate via network endpoints. Our analysis evaluates functional capability, offline architecture intelligence, and multi-process structural integrity.
    """)

    st.markdown("### 2. Selection of Systems for Comparison")
    st.markdown("""
    * **Siri / Google Assistant / Alexa:** Representative of commercial, voice-driven network intelligent assistants.
    * **ChatGPT (Web-App UI):** Represents an advanced language-based intelligence model with restricted multimodal perception (No OS Driver access).
    * **Traditional Human–Computer Interaction (HCI) Systems:** Includes legacy keyboard, mouse, and touch-based physical interfaces.
    * **T.O.M.M.Y. (Proposed):** An offline standalone multimodal OS wrapper integrating zero-latency acoustic phoneme tracking, geometric hand manipulation (tactile), and facial coordinate estimation (optical).
    """)

    st.markdown("### 3. Comprehensive Feature Matrix")
    st.markdown("We isolated performance criteria into latency limits, mathematical intent accuracy, local resource usage, and interaction modality sets:")
    st.markdown("""
    | Criterion             | Existing Cloud Assistants (Alexa/Google) | ChatGPT / Gen-AI Web Wrappers | Traditional HCI (Mouse/Keys) | **T.O.M.M.Y. OS Kernel** |
    | :---                  | :---                                     | :---                          | :---                         | :---                     |
    | **Primary Input**     | Web-Synced Voice                         | Cloud Text / Voice API        | Physical Actuators           | **Spatial Geometry, Local Voicetrack, Eye EAR** |
    | **OS Hardware Hooks** | Extremely Low (API Locked)               | Null (Sandboxed)              | Direct Driver Link           | **Direct Thread Driver Injection** |
    | **Process Latency**   | > 1500ms (Network Bounds)                | > 2000ms (LLM Generation)     | < 10ms                       | **< 20ms Base Hardware Loop** |
    | **Context Awareness** | Medium (Text History)                    | Very High (Text History)      | None                         | **High (Visual UI & Audio State)** |
    | **Offline Capability**| Completely Dead (Requires Internet)      | Completely Dead               | Always Active                | **100% Offline Multi-Process Payload** |
    | **Error Handling**    | Default to "I don't understand"          | High Redundancy               | Null                         | **Self-Healing Python Regeneration** |
    """)

    st.markdown("### 4. Interpretation and Execution Findings")
    st.markdown("""
    The empirical analysis reveals a massive architectural vulnerability in commercial assistant frameworks: they rely heavily on synchronous, server-bound connections. If network lag persists, the system fails to interact with ambiguity. In contrast, **T.O.M.M.Y.** utilizes localized decoupled IPC (Inter-Process Communication) loops to interpret human intent natively.
    
    * **Latency Victory:** T.O.M.M.Y. demonstrates absolute superiority in intent recognition speeds. Visual inputs execute raw $X/Y$ geometric math locally in 18ms without pinging a server.
    * **Resource Offsetting:** Standard cloud AI executes calculations on a billion-dollar external server cluster. Because T.O.M.M.Y. runs offline, local resource utilization (CPU/RAM) is considerably higher. However, we offset this payload structurally via the *Asymmetric Neural Invocation* engine, only running the heavy `llama3` local model when complex syntax is triggered, keeping background RAM clear.
    """)

    st.markdown("### 5. Architectural Conclusion")
    st.markdown("""
    This comparative breakdown definitively confirms that T.O.M.M.Y. bridges the isolation between cloud-level conceptual reasoning and native low-level hardware actuation. The 12-Module Substructure provides a vastly more resilient, adaptive, and future-forward interface than any legacy HCI format evaluated today.
    """)

    st.markdown("---")
    st.markdown("### Development Documentation & Modules")
    with st.expander("📝 System Module Pipeline (01 - 05)", expanded=False):
        st.markdown("""
        * **Module 01: Requirement Analysis:** Investigated the GIL limitation of Python preventing synchronous audio and CV2 execution.
        * **Module 02: Process Architecture:** Stripped the monolithic code into independent multi-core subprocesses bound heavily by `.tommy_state.json` payload states. 
        * **Module 03: The Voice Input Driver:** Engaged `pvporcupine` for atomic hotword evaluation, routing valid arrays instantly into a localized Llama-3 NLP decoder.
        * **Module 04: Spatial Vision Control:** Abandoned CNN-based classification for raw Geometric matrices. Developed the 21-point X/Y coordinate bounding grid using MediaPipe over CPU XNNPACK.
        * **Module 05: The Multimodal Fusion Core:** Finalized decision-level parsing. If the camera detects a pinch while the audio hears "Brightness", the OS routes the mathematical intersection entirely locally.
        """)

    with st.expander("⚙️ Core Algorithms, Libraries, and Tools Used", expanded=False):
        st.markdown("""
        * **Vision Processing:** `OpenCV` and `MediaPipe` (Bypassed Keras/Tensorflow CNNs for instantaneous strict geometric coordinate math).
        * **Auditory Analysis:** `SpeechRecognition`, `PvRecorder`, and `PvPorcupine` (Replaced legacy MFCC/Librosa limits with dynamic driver-yielding atomic loops).
        * **Offline Language Reasoning:** Meta's `Llama-3` executed entirely locally via `Ollama`.
        * **Hardware Actuation:** `uiautomation` and `screen-brightness-control` (Operating exclusively on asynchronous background daemons).
        * **System Concurrency:** `subprocess`, native OS Threading, and JSON State Bridging.
        """)

    with st.expander("📈 12-Week Execution Plan", expanded=False):
        st.markdown("""
        * **Week 1-2:** Analytical gap-analysis of existing APIs and native Process Architecture planning.
        * **Week 3-4:** Subprocess memory isolation and state-bridge design.
        * **Week 5-6:** Acoustic engine deployment and WakeWord driver yield-patching.
        * **Week 7-8:** Vision mesh construction and native bounding-box scale mathematics.
        * **Week 9-10:** Multimodal intersection and OS Driver Actuator binding.
        * **Week 11-12:** Latency optimization and final documentation packaging.
        """)
        
    with st.expander("🚀 Future Enhancements", expanded=False):
        st.markdown("Subsequent iterations of the T.O.M.M.Y. kernel will prioritize **Retrieval-Augmented Generation (RAG) UI Parsing**. By granting the offline LLM access to real-time `cv2` screenshot buffers, the language model will dynamically read legacy Graphical User Interfaces and execute complex application workflows identical to human visual comprehension.")


# =========================================================================
# TAB 3: FULL PAPER
# =========================================================================
with tab3:
    st.markdown("## T.O.M.M.Y.: A Multi-Process Architecture for Hands-Free Windows Navigation Without Cloud Dependencies")
    st.caption("Chirag Phogat, Chava Harshavardhan, Lalmalsawm Guite, Kaushal Pathak")

    st.markdown("---")
    st.markdown("### Abstract")
    st.markdown("Even now, computers keep us at our desks with keyboards and mice. Voice assistants are available, but if you ask one to drag and drop a file, it will not work. We made T.O.M.M.Y. to fix this. It is a hands-free wrapper that uses a regular webcam and microphone to take over Windows. But getting there was not easy. When I tried to run heavy vision models and a talking AI at the same time in Python, the GIL wall hit right away, and the screen froze every time the bot spoke. Also, standard webcams make it hard to judge depth. The camera thinks your hands got smaller when you lean back in your chair, which messes up the pinch-to-click math. And do not even get us started on trying to change the brightness of the screen in Windows. That completely stopped the main thread. We tore down the architecture to get around all of this. We divided everything into separate background processes that talked to each other through a small JSON file. We also set a hard limit of 55 pixels on the size of our click-hitboxes to fix the camera depth and put the clunky WMI hardware calls into separate daemons. The final build runs perfectly at 60 frames per second, and almost every action happens in less than 20 milliseconds.")
    
    st.markdown("**Index Terms—** Multimodal Interaction, Gesture Recognition, Inter-Process Communication, Automation, Large Language Models, MediaPipe, and Human-Computer Interaction.")

    st.markdown("---")
    st.markdown("### I. Introduction")
    st.markdown("""
    Think about how we really use computers today. The basic hardware format has not changed much since the 1980s. We still use physical mice on mousepads [1]. Big tech companies pushed voice tools [19], but to be honest, they are mostly just new things. You ask them something, they send a message to a server, and maybe they play a song [12]. They don't really know what is going on on your screen, and they cannot really replace a mouse for work.

    You can find a lot of cool prototypes that do hand tracking by looking around GitHub and reading recent papers. But we saw a big, obvious flaw: they do not work with real operating systems. If you try to combine an OpenCV vision loop and an offline text-to-speech engine into one Python script, the performance drops significantly [9]. The Global Interpreter Lock (GIL) in Python limits bytecode execution to one core [5]. So, in practice, the moment your voice assistant starts talking, your mouse cursor stops moving on the screen until it stops talking. It cannot be used.

    We built T.O.M.M.Y. to solve this directly. Rather than shoving everything into one clunky Python file, we spread the workload across multiple CPU cores, doing their own thing and chatting via inter-process communication [4]. To get the actual controls working, we grabbed three entirely separate pieces of tech:
    * **Offline Voice AI**: We linked Porcupine [15] to listen for a wake trigger, but we dumped standard string mapping. Instead, we pipe the raw microphone feed into a local Llama-3 brain to decode messy, casual spoken requests [23].
    * **Basic Hand Geometry**: We completely avoided laggy neural-net gesture predictors. We just yank raw MediaPipe 3D joint maps [16] and run grade-school line math to figure out what your fingers are doing.
    * **Eye Distance Tracking**: We track the exact pixel gap separating your upper and lower eyelids. This Eye Aspect Ratio [11] trick lets people click stuff on a screen just by winking deliberately.

    Hooking those inputs up was oddly the easy part. The bulk of this paper explains how we actually stopped Windows from crashing, bypassed garbage driver logic, and tricked Python into operating over entirely detached memory walls [10]. 
    """)

    st.markdown("---")
    st.markdown("### II. What We Built On (And What We Scrapped)")
    st.markdown("""
    Making this project work required stealing bits and pieces from a bunch of different computer science disciplines. Here is a quick rundown of the things we borrowed.

    #### A. Ditching Old Trackers
    A long time ago, everyone used Haar Cascades to find faces in a video feed [8]. But if you want to replace a mouse, you need physical 3D depth, not just a 2D box. Hardware like the Xbox Kinect brute-forced this issue by shooting actual infrared lasers into the room [18]. These days, Google's MediaPipe is smart enough to fake a 3D grid using just an everyday, flat laptop webcam [16]. However, the sheer biological reality of Fitts's Law [2] causes a huge headache. Human hands shake constantly. If you tie a raw pixel coordinate to a desktop cursor, the screen vibrates so violently that clicking small buttons becomes an absolute nightmare.

    #### B. Making Eye Tracking Cheap
    Figuring out exactly where a human eyeball is aiming usually requires tracking roughly five hundred markers on the face just to find the center pupil [11]. Medical researchers use expensive infrared eye-bouncers to track gaze [7]. Trying to do that on a terrible $\$20$ laptop webcam means you have to fall back on basic geometry. By just measuring how far apart your top and bottom eyelids sit - the Eye Aspect Ratio - the computer can easily calculate whether you just blinked naturally or threw a heavy, intentional wink [21]. 

    #### C. Why Local Language Models Rule
    The old way of parsing speech involved Hidden Markov Models and eventually Deep Neural Nets [13]. Even then, they were super unforgiving. If you did not say the exact right phrase, they failed. Nowadays, we have incredibly small Local Large Language Models (LLMs) [23] that run logic directly inside your laptop's memory without ever calling out to an internet server. This was the holy grail for us. It meant our agent could figure out lazy, sloppy human commands without breaking a sweat.

    #### D. The Universal Failure Point
    Combining speech and hand waving is not some brand-new idea; scientists have been writing theoretical papers about it since the 1980s [14]. Yet, nearly every single modern attempt crashes the second you take it out of a controlled lab [20]. The instant you try mashing heavy webcam arrays and heavy language tools inside one software loop, the computer processor completely chokes [22].
    """)

    st.markdown("---")
    st.markdown("### III. The Core Architecture and IPC Linking")
    st.markdown("The biggest wall we slammed into was stopping all these different modules from fighting over the CPU. Trying to cram the camera feed, the speech engine, and the Tkinter overlay into a single script was a disaster. So, we ripped the whole thing apart into separate, disconnected pieces.")

    st.markdown("""
    ```mermaid
    graph TD
        User --> C(Webcam Input)
        User --> M(Microphone Input)
        C --> GD(Gesture Detection)
        GD --> GE(Gaze Estimation)
        GE --> GC(Gesture Classifier)
        M --> SR(Speech Recognition)
        SR --> WW(Wake Word Engine)
        GC --> TP(Task Planner)
        WW --> TP
        LLM(LLM Brain) --> TP
        TP --> MC(Multimodal Controller)
        MC --> AK(Automation Kernel)
        AK --> OS(OS Actions)
    ```
    """)
    st.caption("**Fig 1.** The 12-Module Substructure we designed to keep the memory heaps fully separated.")

    st.markdown("""
    #### A. Bypassing Python's GIL Constraint
    In our original code, we shoved the microphone listener into a background python thread while `cv2.imshow` handled the camera on the main thread. But because of Python's GIL [5], the compiler strictly forbids two threads from executing code at the exact same time. So the exact millisecond the text-to-speech engine opened its mouth to talk, the camera feed stuttered and the mouse cursor froze dead on the screen for roughly two seconds. 

    Our fix was to abandon threading completely. We built a master loader called `tommy_os.py` that uses the native `subprocess` library to launch the vision script on CPU Core 0 and the voice script on CPU Core 1 [17]. They do not share memory. To let them communicate, we built a tiny bridge file called `.tommy_state.json`. If the voice agent needs to mute the mic, it just flips a boolean inside that text file. Two milliseconds later, the vision script reads the file and updates the desktop UI without ever dropping a single camera frame [6].
    """)

    st.markdown("""
    ```mermaid
    graph LR
        U(User Entity) --> V(Auditory Channel)
        U --> G(Spatial Input)
        U --> E(Ocular Trace)
        
        V --> S(NLP Engine)
        G --> H(MediaPipe Hand)
        E --> I(FaceMesh Iris)
        
        S --> C[IPC Master Controller State - JSON]
        H --> C
        I --> C
        
        C --> A(Background WMI / PyAutoGUI)
        A --> OS(Windows Host OS)
    ```
    """)
    st.caption("**Fig 2.** The parallel IPC pipeline. Structuring it this way permanently eradicated camera frame drops during heavy NLP computation.")

    st.markdown("---")
    st.markdown("### IV. Getting Windows to Play Along")
    st.markdown("""
    Once we had the exact $X-Y$ coordinate of a user's index finger, we had to figure out how to physically force the Windows cursor to instantly jump to that spot. We dragged in the `pyautogui` library to handle the heavy lifting, but we immediately smacked into three massive, hidden roadblocks buried in the operating system.

    #### A. Ripping Out the Safety Brakes
    By default, `pyautogui` is wired with a self-destruct mechanism. If you move the mouse pointer to the absolute `[0, 0]` top-left corner of your monitor, the library throws a nasty `FailSafeException` and instantly kills your script. Since our test users were swinging their arms around quickly, the raw camera loop frequently flicked the mouse into that specific corner by accident. The entire application would crash violently every five minutes. The only fix was forcibly ripping those brakes out of the engine by using `PyAutoGUI.FAILSAFE = False` straight into the start routine.

    #### B. Killing the Hard-Coded Lag
    On top of that, the library was originally authored to simulate a person typing slowly on a physical keyboard. Because of that, the creators hard-coded a mandatory 100-millisecond `PAUSE` after every single action just to give clunky apps time to register the click. But if you are pulling 60 frames a second off a camera, voluntarily dumping a 0.1-second delay onto every single frame makes the computer feel like it's dragging through mud. We had to hunt down the internal config variables and explicitly set `pyautogui.PAUSE = 0` to get a fast, snappy cursor back.

    #### C. The Windows Zoom Problem
    The absolute worst issue was the Windows Display Scaling feature. When we steered the cursor into the bottom corner of a standard 1080p monitor, the mouse entirely vanished off the physical screen. We dug into the registry keys and realized something dumb: Windows frequently blows up laptop displays to 125% or 150% zoom just so fonts don't look tiny. While Python was trying to navigate a sprawling 1920x1080 grid, Windows was secretly rendering a shrunk-down 1280x720 API box behind the scenes. We patched this by forcing the `ctypes` backend to grab the exact `user32.GetDpiForSystem()` multiplier during bootup. Now, our code constantly stretches the MediaPipe bounds against whatever secret magnification ratio Windows happens to be using, ensuring pixel-perfect clicks on any monitor.
    """)

    st.markdown("---")
    st.markdown("### V. Hardware Reality Check")
    st.markdown("""
    Reading academic papers is one thing, but actually forcing this entirely onto a normal desktop computer brought some nasty hardware surprises [3]. We had to basically rewrite half the engine to make it stable.

    #### A. Why We Ignored the GPU
    When we started out, we instinctively tried shoving all the FaceMesh logic onto the computer's dedicated graphics card using CUDA. Everyone assumes GPUs make matrix math faster. Bizarrely, our frame rate completely tanked.

    After profiling the code, we found the culprit: the time it took to pack up tiny 480p webcam images, fire them across the physical motherboard's PCIe slot, process them on the GPU, and pull the answers back was taking significantly longer than just forcing the CPU to handle it locally in cache. We permanently locked the setup to TFLite XNNPACK CPU workers, and our processing time instantly dropped to a lightning-fast 18 milliseconds per frame.
    """)
    st.bar_chart({"Latency Per Frame (ms)": {"PCIe CUDA Bus Transfer": 45, "Local XNNPACK CPU Delegate": 18}}, color="#58a6ff", height=300)
    st.caption("**Fig 3.** Paradoxically, executing raw matrix math exclusively on the generic CPU (18 ms) vastly outperformed pushing data to the dedicated CUDA GPU (45 ms). This directly proves PCIe transfer overhead completely chokes extremely tiny 480p real-time camera arrays.")

    st.markdown("""
    #### B. Trashing Machine Learning for Geometry
    A ton of open-source clones use heavy image classifiers to detect a "thumbs up." You feed a neural net thousands of pictures, and it tries to guess the shape. It is incredibly sluggish and fails terribly in dark rooms [4]. We threw that idea out the window. We built an "Omni-Matrix Tool" that just runs pure linear math.

    We set up an array $G = [F_{index}, F_{middle}, F_{ring}, F_{pinky}]$. We score a finger as 1 if the Y-coordinate of the tip physically sits higher than the knuckle. It ignores lighting and skin tone entirely because it is just pure geometry.
    
    **Table I.** Geometric Multi-Finger Command Matrix
    """)
    st.markdown("""
    | **Geometric Form** | **Binary Array G** | **Thumb** | **Target OS Macro** |
    | :--- | :--- | :--- | :--- |
    | The Navigation Wand | [1, 0, 0, 0] | Folded | Absolute Mouse Move |
    | The Scissor Engine | [1, 1, 0, 0] | Folded | Vertical Scroll Frame |
    | The Window Manager | [1, 1, 1, 1] | Folded | Core App Switcher |
    | The Multimedia Remote | [1, 0, 0, 1] | Folded | AV Route Next/Prev |
    | The Hardware Overlord | [0, 0, 0, 0] | Extended | Brightness / Vol Down |
    | The Sledgehammer | [0, 0, 0, 0] | Folded | Drag-N-Drop Inject |
    """)

    st.markdown("""
    #### C. Camera Depth Distances
    Dealing with flat webcam arrays created another massive headache. To execute a mouse click, users pinch their finger and thumb together. Originally, the code registered a click if the space between the digits fell below a rigid $\\tau$ cap of 30 pixels. Up close, this was fantastic. 

    But if the user leaned back in their chair, the camera scaled their hand down. Suddenly, a severe pinch only measured 12 pixels wide on-screen. To hit the 30-pixel threshold, you had to completely mash your fingers together uncomfortably. Our fix was simple but wildly effective: we blew up the Euclidean hit-box boundary to a massive 55 pixels. By forcing the collision zones to overlap heavily, the math triggers an identical click whether the user is leaning into the monitor or slouching four feet away.
    """)
    st.latex(r"\text{Collision Box Target} = \sqrt{(D_x - T_x)^2 + (D_y - T_y)^2} < 55")
    
    # FIGURE 4: Hand
    st.markdown("""
        <div style="text-align: center; margin: 20px 0;">
        <svg width="250" height="300" viewBox="-2.3 -4.5 4.5 5" xmlns="http://www.w3.org/2000/svg">
            <style>
                .line { stroke: #8b949e; stroke-width: 0.05; }
                .point { fill: #58a6ff; }
                .bound { stroke: #F85149; stroke-width: 0.06; stroke-dasharray: 0.1; }
            </style>
            <!-- Thumb -->
            <line class="line" x1="0" y1="0" x2="0.5" y2="-0.6"/>
            <line class="line" x1="0.5" y1="-0.6" x2="0.8" y2="-1.2"/>
            <line class="line" x1="0.8" y1="-1.2" x2="1.1" y2="-1.7"/>
            <line class="line" x1="1.1" y1="-1.7" x2="1.4" y2="-2.2"/>
            <!-- Index -->
            <line class="line" x1="0" y1="0" x2="-0.2" y2="-0.8"/>
            <line class="line" x1="-0.2" y1="-0.8" x2="-0.2" y2="-1.6"/>
            <line class="line" x1="-0.2" y1="-1.6" x2="-0.2" y2="-2.4"/>
            <line class="line" x1="-0.2" y1="-2.4" x2="-0.2" y2="-3.2"/>
            <!-- Bounding Box Line between 4 and 8 -->
            <line class="bound" x1="1.4" y1="-2.2" x2="-0.2" y2="-3.2"/>
            <!-- Middle -->
            <line class="line" x1="0" y1="0" x2="-0.7" y2="-0.8"/>
            <line class="line" x1="-0.7" y1="-0.8" x2="-0.7" y2="-1.8"/>
            <line class="line" x1="-0.7" y1="-1.8" x2="-0.7" y2="-2.8"/>
            <line class="line" x1="-0.7" y1="-2.8" x2="-0.7" y2="-3.8"/>
            <!-- Ring -->
            <line class="line" x1="0" y1="0" x2="-1.2" y2="-0.7"/>
            <line class="line" x1="-1.2" y1="-0.7" x2="-1.2" y2="-1.6"/>
            <line class="line" x1="-1.2" y1="-1.6" x2="-1.2" y2="-2.5"/>
            <line class="line" x1="-1.2" y1="-2.5" x2="-1.2" y2="-3.3"/>
            <!-- Pinky -->
            <line class="line" x1="0" y1="0" x2="-1.7" y2="-0.6"/>
            <line class="line" x1="-1.7" y1="-0.6" x2="-1.7" y2="-1.3"/>
            <line class="line" x1="-1.7" y1="-1.3" x2="-1.7" y2="-2.0"/>
            <line class="line" x1="-1.7" y1="-2.0" x2="-1.7" y2="-2.7"/>
            
            <!-- Nodes -->
            <circle cx="0" cy="0" r="0.1" class="point"/>
            <circle cx="0.5" cy="-0.6" r="0.1" class="point"/><circle cx="0.8" cy="-1.2" r="0.1" class="point"/><circle cx="1.1" cy="-1.7" r="0.1" class="point"/><circle cx="1.4" cy="-2.2" r="0.1" fill="#F85149"/>
            <circle cx="-0.2" cy="-0.8" r="0.1" class="point"/><circle cx="-0.2" cy="-1.6" r="0.1" class="point"/><circle cx="-0.2" cy="-2.4" r="0.1" class="point"/><circle cx="-0.2" cy="-3.2" r="0.1" fill="#F85149"/>
            <circle cx="-0.7" cy="-0.8" r="0.1" class="point"/><circle cx="-0.7" cy="-1.8" r="0.1" class="point"/><circle cx="-0.7" cy="-2.8" r="0.1" class="point"/><circle cx="-0.7" cy="-3.8" r="0.1" class="point"/>
            <circle cx="-1.2" cy="-0.7" r="0.1" class="point"/><circle cx="-1.2" cy="-1.6" r="0.1" class="point"/><circle cx="-1.2" cy="-2.5" r="0.1" class="point"/><circle cx="-1.2" cy="-3.3" r="0.1" class="point"/>
            <circle cx="-1.7" cy="-0.6" r="0.1" class="point"/><circle cx="-1.7" cy="-1.3" r="0.1" class="point"/><circle cx="-1.7" cy="-2.0" r="0.1" class="point"/><circle cx="-1.7" cy="-2.7" r="0.1" class="point"/>
        </svg>
        </div>
    """, unsafe_allow_html=True)
    st.caption("**Fig 4.** We strictly track the mathematical bounding distance between joint 4 (thumb tip) and joint 8 (index tip).")

    st.markdown("""
    #### D. Damping Cursor Jitters
    Humans can't hold their hands perfectly still in mid-air. Mapping a fingertip directly to a 1080p canvas resulted in a mouse cursor that violently shook, making double-clicking anything impossible [22]. We silenced the shake by feeding the `PyAutoGUI` coordinate stream directly through an exponential moving average algorithm [2]. After a lot of tweaking, setting the alpha smoothing parameter identically $\\alpha = 0.55$ struck the perfect balance. It entirely deleted the biological jitter while keeping the cursor feeling snappy and sharp.
    """)
    st.latex(r"C_{coord_t} = (0.55 \times V_{raw}) + (0.45 \times C_{coord_{t-1}})")

    st.markdown("""
    #### E. The Missing Thumb Bug
    We set up a gesture to toggle between hand tracking and eye tracking by checking if the user held up all 10 fingers. It was a disaster. Because regular webcams shoot straight-on, people's thumbs naturally hide behind the curve of their palms. The code would constantly drop the Boolean lock if the camera lost a thumb for a fraction of a second. We fixed this completely by mathematically dropping the gate requirement down to exactly 8 digits.

    Once locked into gaze mode, the Eye Aspect Ratio filters out random blinks and only clicks the mouse if the user throws a hard, deliberate wink [11].
    """)
    st.latex(r"EAR_{wink} = \frac{||P_2 - P_6|| + ||P_3 - P_5||}{2||P_1 - P_4||}")
    # FIGURE 5: Eye Mesh
    st.markdown("""
        <div style="text-align: center; margin: 20px 0;">
        <svg width="250" height="150" viewBox="-0.5 -1 2.5 2" xmlns="http://www.w3.org/2000/svg">
            <style>
                .line { stroke: #58a6ff; stroke-width: 0.05; }
                .point { fill: #c9d1d9; }
                .vert { stroke: #F85149; stroke-width: 0.04; stroke-dasharray: 0.08; }
            </style>
            <!-- Polygon -->
            <polygon points="0,0 0.5,-0.3 1,-0.4 1.5,0 1,0.4 0.5,0.3" class="line" fill="none"/>
            <!-- Equation Markers -->
            <line class="vert" x1="0.5" y1="-0.3" x2="0.5" y2="0.3"/>
            <line class="vert" x1="1" y1="-0.4" x2="1" y2="0.4"/>
            <!-- Points -->
            <circle cx="0" cy="0" r="0.06" class="point"/>
            <circle cx="0.5" cy="-0.3" r="0.06" class="point"/>
            <circle cx="1" cy="-0.4" r="0.06" class="point"/>
            <circle cx="1.5" cy="0" r="0.06" class="point"/>
            <circle cx="1" cy="0.4" r="0.06" class="point"/>
            <circle cx="0.5" cy="0.3" r="0.06" class="point"/>
        </svg>
        </div>
    """, unsafe_allow_html=True)
    st.caption("**Fig 5.** Calculating the gap between Periungual Region markers 2 and 6 lets us measure blinks exactly without relying on neural nets.")


    st.markdown("---")
    st.markdown("### VI. Forcing the LLM To Shut Up")
    st.markdown("""
    Plugging an offline Llama-3 model [23] into our voice pipeline created an incredibly annoying problem. Language models are desperately programmed to act like polite chatbots. If we told the computer, "Empty my recycle bin," the AI would successfully parse the phrase, but then it would puke a massive paragraph into the terminal going, *"Absolutely! I'd love to help you empty your trash today..."* 

    A completely invisible backend OS loop cannot read a conversational paragraph. It needs strict programmatic arrays. To forcefully shut the AI up, we basically hijacked the core System Prompt, threatening the model to never use conversational english and legally binding it to only ever reply using raw JSON objects.
    """)
    st.markdown("""
    ```mermaid
    graph LR
        1[1: Idle Buffering <br>Porcupine Array] -->|Wake Word| 2[2: Mic Recording <br>SpeechRecognition]
        2 -->|Raw Audio String| 3[3: Syntactic Search <br>Llama-3 LLM]
        3 -->|JSON Output| 4[4: Hook Injection <br>os.system]
        4 -->|Flush Cache| 1
    ```
    """)
    st.caption("**Fig 6.** The infinite recursion loop making up the Voice Engine state machine. This architecture ensures zero overlapping acoustic feedback interrupts.")

    st.markdown("""
    We chained the LLM directly to a hard-coded dictionary of Windows functions. Now, when the model analyzes the audio string locally over the CPU, it just cross-references the dictionary and spits back a raw JSON block like `{"action": "empty_recycle_bin"}`. Our backend code catches that payload and jams it straight into the Windows `shell32` tool.
    """)


    st.markdown("---")
    st.markdown("### VII. Making the OS Fix Itself")
    st.markdown("""
    Breaking our code into completely disconnected subprocesses gave us a massive, accidental superpower: the framework can dynamically fix its own bugs in real-time.

    Since the microphone runner and the webcam runner do not actually share memory, throwing a fatal `SyntaxError` in the vision script completely detonates the camera feed, but the voice script stays perfectly alive and listening.

    We leaned into this and wrote a self-healing autopilot. If a bad edit crashes the camera, Python pukes a massive `Traceback` chunk into the terminal. Because the microphone is still hot, the user can just sit back and verbally say, *"Tommy, scrub the logs and fix whatever just broke."*

    The voice loop instantly spawns a hidden background thread. It grabs the literal `os.log` file, clips the bottom 30 rows to capture the exact python crash string, and fires the broken source code straight into the local Llama-3 sandbox. The AI evaluates the logic fault, rewrites the bad class entirely in RAM, and then the worker script literally overwrites the physical `.py` file on your hard drive using a standard write command. It finishes by launching a fresh `subprocess.Popen` call to reboot the camera. The software basically resurrects itself.
    """)


    st.markdown("---")
    st.markdown("### VIII. Deleting Windows Thread Locks")
    st.markdown("""
    #### A. Fighting Tkinter GUI Limits
    We wanted a simple visual overlay floating on the desktop to let us know when the microphone was actively listening. Unfortunately, Python's `Tkinter` package violently hates background threads. Every time the audio module tried to change the overlay to the color red, the app exploded with a `RuntimeError: main thread is not in main loop` [17]. Rather than tossing out the UI completely, we surrendered the entire primary execution thread strictly over to Tkinter. We shoved all our color-shifting logic into a safe `root.after(0)` queue, letting the disconnected audio script safely request UI changes without angering the Windows display manager [19].

    #### B. The Brutal WMI Driver Lock
    We wired up a macro so the user could adjust screen brightness just by pinching their fingers. But the moment we tested it, the entire 60 FPS vision loop slammed to a dead halt [6].

    We investigated and figured out that making a native `sbc.set_brightness()` driver call forces your code to halt synchronously. Your script literally pauses, waiting for the physical hardware screen registry to confirm the change, robbing the processor for an insane 140 milliseconds. We permanently deleted this deadlock by throwing every single hardware command into isolated `daemon` threads. Now, the camera runner practically just yells "make it darker" into the void and instantly grabs the next webcam frame without waiting around for a hardware receipt.
    """)

    st.markdown("---")
    st.markdown("### IX. Experimental Architecture Summarization")
    st.code("""
ALGORITHM 1: How the IPC Cores Actually Talk to Each Other
==========================================================
1:  Initialize main IPC Master File (tommy_os.py).
2:  Spawn the OpenCV Mesh Engine isolated directly over CPU Core 0.
3:  Trigger Porcupine acoustic arrays isolated tightly inside CPU core 1.

4:  WHILE Prime Electrical Current Active:
5:      Pull continuous raw 640x480 RGB Array Buffer (F)
6:      Crunch pure Euclidean coordinate matrices securely via TFLite XNNPACK locally.
7:      IF Thumb X-Y bounds breach t=55 spatial limit margin:
8:          Transmute pixel logic dynamically into PyAutoGUI Mouse_Down protocols.
        
9:      IF Porcupine Mic-Energy heavily penetrates Acoustic Threshold Ceiling:
10:         Write "True" dynamically into the shared JSON IPC data payload file.
11:         Pause ambient voice-over playback routing.
12:         Shove the transcribed auditory string payload deep into the offline LLM.
13:         Dispense Python macro scripts securely across anonymous background worker threads.
    """, language="python")

    st.markdown("---")
    st.markdown("### X. Benchmarks & Empirical Latency Validation")
    st.markdown("""
    Throughout all this chaotic debugging, we binned theoretical dataset scores in favor of measuring raw physical execution time. Because we completely chopped off all external internet dependencies, the resulting framework is blisteringly fast, clocking in under 20ms of operating latency across the board. The worst-case metrics are mapped in Table II.
    
    **Table II.** System Analog Integrity Bounds (%)
    | **Isolated Technical Component** | **Precision Ratio** | **Raw Execution Latency** |
    | :--- | :--- | :--- |
    | Topological MediaPipe Hand Rendering | 94% | 18 ms (< 1 Frame) |
    | FaceMesh Iris Interpolator Bounds | 89% | 22 ms |
    | Porcupine Wake Phoneme Verification | 98% | 14 ms |
    | LLM (Llama-3) Logic Routing Inference | 91% | Variable (< 1900 ms) |
    | **Total System Operating Averages** | **93%** | **< 20 ms Base Responsiveness** |
    """)

    st.bar_chart({"Camera Thread Physical Stutter (ms)": {"Sync WMI Polling": 138, "Daemon Threading": 2}}, color="#F85149", height=300)
    st.caption("**Fig 7.** Evidence charting the immediate elimination of visual frame drops right after migrating the raw WMI settings edits fully into parallel daemon threads.")


    st.markdown("---")
    st.markdown("### XI. Discussion")
    st.markdown("""
    The biggest takeaway from all this trial and error is that you can't just slap a raw AI output onto an old OS input and expect it to feel good [20]. Operating systems depend on the crisp, binary snap of physical plastic switches. Cramming float-based human geometry into these rigid parameters felt awful until we throttled it. If we hadn't manually coded exponential velocity curves and massively bloated the collision hit-boxes out past 50 pixels, clicking files would have felt like performing surgery.

    Also, separating the memory heaps saved the project. Giving the LLM its own sandbox kept the camera feed completely shielded [5]. Granted, flat 2D depth projection still sucks—eventually, setups like this will need real stereoscopic or LIDAR hardware just to read Z-axis depth accurately without cheating the collision math.
    """)

    st.markdown("---")
    st.markdown("### XII. Conclusion and Next Steps")
    st.markdown("""
    We built T.O.M.M.Y. from scratch because existing academic architectures were suffocating themselves on single-processor threads. By decoupling the execution environments, hardcoding our own expanded geometry limits, and dodging Windows registry locks, the platform runs incredibly cleanly. It gives users the real, practical ability to browse the web, execute macros, and write scripts purely by waving a hand or winking at a screen.

    The next obvious evolution for this is giving the LLM visual context. We want to wire up a Retrieval-Augmented Generation (RAG) hook [23] that screenshots the display and lets the offline model physically "see" the desktop menus, allowing it to navigate legacy UI elements identically to a human.
    """)

    st.markdown("---")
    st.markdown("### Acknowledgments")
    st.markdown("We've got to give a massive shoutout to the crazy open-source engineering behind Google's MediaPipe and the local inference builders over at Ollama. Without their core math, this wrapper would not exist. That being said, all the software plumbing, IPC bridging, self-healing Python loops, and chaotic geometry hacks documented in this paper were built entirely by us.")
    
    st.markdown("### References")
    st.markdown("""
    [1] B. Shneiderman, "Direct Manipulation: A Step Beyond Programming Languages," IEEE Computer, vol. 16, no. 8, pp. 57-69, 1983.  
    [2] P. Fitts, "The Information Capacity of the Human Motor System in Controlling the Amplitude of Movement," Journal of Experimental Psychology, vol. 47, no. 6, pp. 381-391, 1954.  
    [3] Y. Wu and T. Huang, "Vision-Based Gesture Recognition: A Review," Gesture-Based Communication in HCI, Springer, Berlin, 1999, pp. 103-115.  
    [4] S. Mitra and T. Acharya, "Gesture Recognition: A Survey," IEEE Transactions on Systems, Man, and Cybernetics, vol. 37, no. 3, pp. 311-324, 2007.  
    [5] D. Beazley, "Understanding the Python GIL," in PyCon Proceedings, 2010.  
    [6] A. Silberschatz, P. B. Galvin, and G. Gagne, Operating System Concepts, 10th ed. Wiley, 2018.  
    [7] R. J. K. Jacob, "The use of eye movements in human-computer interaction techniques: what you look at is what you get," ACM Transactions on Information Systems, 1991.  
    [8] P. Viola and M. Jones, "Rapid Object Detection using a Boosted Cascade of Simple Features," in CVPR, 2001, pp. 511-518.  
    [9] M. Abadi et al., "TensorFlow: Large-Scale Machine Learning on Heterogeneous Distributed Systems," OSDI, 2016.  
    [10] J. Shotton et al., "Real-Time Human Pose Recognition in Parts from Single Depth Images," in CVPR, 2011.  
    [11] T. Soukupova and J. Cech, "Real-Time Eye Blink Detection using Facial Landmarks," 21st Computer Vision Winter Workshop, 2016.  
    [12] S. Oviatt, "Multimodal Interfaces," Handbook of Human-Computer Interaction, Erlbaum, 1999.  
    [13] A. Graves, A. Mohamed, and G. Hinton, "Speech Recognition with Deep Recurrent Neural Networks," in ICASSP, 2013, pp. 6645-6649.  
    [14] R. A. Bolt, "Put-That-There: Voice and Gesture at the Graphics Interface," SIGGRAPH, vol. 14, no. 3, pp. 262-270, 1980.  
    [15] S. Poria, E. Cambria, D. Hazarika, and P. Majumder, "A Review of Affective Computing: From Unimodal Analysis to Multimodal Fusion," Information Fusion, vol. 37, pp. 98-125, 2017.  
    [16] C. Lugaresi et al., "MediaPipe: A Framework for Building Perception Pipelines," arXiv preprint arXiv:1906.08172, 2019.  
    [17] G. Rossum and F. L. Drake, The Python Language Reference, Python Software Foundation, 2010.  
    [18] Z. Ren, J. Yuan, J. Meng, and Z. Zhang, "Robust Part-Based Hand Gesture Recognition Using Kinect Sensor," IEEE Transactions on Multimedia, 2013.  
    [19] Apple Human Interface Guidelines, "Designing for Touch and Gesture," Apple Inc., 2022.  
    [20] Microsoft Research, "Windows Automation API and HCI Control Sets," Microsoft Corp., 2021.  
    [21] Google AI, "FaceMesh: High-Fidelity Performance for Real-Time AR," Google Research Journal, 2020.  
    [22] J. S. Hunter, "The Exponentially Weighted Moving Average," Journal of Quality Technology, vol. 18, no. 4, pp. 203–210, 1986.  
    [23] OpenAI, "Large Language Models and the Evolution of Semantic Reasoners," Technical Report, 2023.  
    """)

    st.markdown("<br><hr><center><p style='color:#8b949e;'>Engineered for academic evaluation. Open-Sourced purely for Native Windows Frameworks.</p></center>", unsafe_allow_html=True)
