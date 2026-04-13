import pyautogui
import base64
import requests
import json
import io
import time

def capture_desktop_base64():
    """
    Captures a physical screenshot of the Windows desktop and encodes it rapidly into a base64 string.
    Bypasses file I/O locks by buffering the image directly into localized RAM.
    """
    try:
        # Snap the screen using PyAutoGUI (safe OS-level hook)
        screenshot = pyautogui.screenshot()
        
        # Buffer the image natively into RAM instead of writing to disk
        buffered = io.BytesIO()
        screenshot.save(buffered, format="JPEG", quality=85)
        
        # Decode bytes into a universal string payload
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str
    except Exception as e:
        print(f"[ERROR] Failed to capture physical desktop buffer: {e}")
        return None

def trigger_visual_rag(prompt="Describe exactly what is happening on this computer screen."):
    """
    Orchestrates the Retrieval-Augmented Generation (RAG) Architecture.
    Fires the desktop's raw binary buffer into the local GPU Ollama instance (Moondream).
    Runs strictly OFF-GRID.
    """
    print(f"\n[SYS] Engaging Visual RAG Extraction...")
    print(f"[SYS] User Prompt: '{prompt}'")
    
    start_time = time.time()
    b64_image = capture_desktop_base64()
    
    if not b64_image:
        return "CRITICAL FAULT: Unable to grab visual desktop stream."
        
    print(f"[SYS] Captured Desktop RAM Buffer at {pyautogui.size()[0]}x{pyautogui.size()[1]} resolution.")
    print(f"[SYS] Firing Multi-Modal Request to local Ollama [Model: qwen3-vl:4b]...")
    
    # Payload built for the local Ollama container
    payload = {
        "model": "qwen3-vl:4b",
        "prompt": prompt,
        "images": [b64_image],
        "stream": False
    }
    
    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=45)
        if response.status_code == 200:
            ai_data = response.json()
            latency = round(time.time() - start_time, 2)
            answer = ai_data.get("response", "").strip()
            print(f"[SYS] Vision Array Generated in {latency}s: \n>> {answer}\n")
            return answer
        else:
            err = f"API Error {response.status_code}: {response.text}"
            print(f"[ERROR] {err}")
            return err
            
    except requests.exceptions.ConnectionError:
        err = "[FATAL] Cannot connect to Ollama. Ensure 'ollama serve' is running on localhost:11434!"
        print(err)
        return err
    except Exception as e:
        err = f"[ERROR] Uncaught RAG Fault: {str(e)}"
        print(err)
        return err

if __name__ == "__main__":
    # Test block
    print("=== T.O.M.M.Y. VISUAL RAG DIAGNOSTICS ===")
    answer = trigger_visual_rag("Analyze the currently opened windows and tell me what the user is working on.")
    print("=== DIAGNOSTICS COMPLETE ===")
