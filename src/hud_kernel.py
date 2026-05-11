import sys
import os
import json
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFrame
from PyQt6.QtCore import Qt, QTimer, QPoint, QPropertyAnimation, QEasingCurve, QRect
from PyQt6.QtGui import QColor, QFont, QPainter, QPen

# --- IPC STATE PATH ---
STATE_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", ".tommy_state.json")

class TommyHUD(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T.O.M.M.Y. Cinematic HUD")
        
        # 1. TRANSPARENT OVERLAY CONFIG
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.WindowTransparentForInput | # Click-through!
            Qt.WindowType.Tool # Hide from taskbar
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # 2. DIMENSIONS
        screen = QApplication.primaryScreen().size()
        self.sw, self.sh = screen.width(), screen.height()
        self.setGeometry(0, 0, self.sw, self.sh)
        
        # 3. UI ELEMENTS
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Identity Badge (Top Center)
        self.id_badge = QLabel("SYSTEM STANDBY", self)
        self.id_badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.id_badge.setGeometry(int(self.sw/2)-200, 40, 400, 50)
        self.id_badge.setStyleSheet("""
            background-color: rgba(0, 0, 0, 180);
            color: #00ffcc;
            border: 1px solid #00ffcc;
            border-radius: 10px;
            font-family: 'Segoe UI Semibold';
            font-size: 18px;
            letter-spacing: 2px;
        """)
        
        # Mode Chips (Top Left)
        self.mode_chip = QLabel("VISION: INITIALIZING", self)
        self.mode_chip.setGeometry(40, 40, 250, 40)
        self.mode_chip.setStyleSheet("""
            background-color: rgba(0, 0, 0, 150);
            color: #ffffff;
            border-left: 5px solid #00ffcc;
            padding-left: 15px;
            font-family: 'Consolas';
            font-size: 14px;
        """)

        # Voice Status (Top Right)
        self.voice_chip = QLabel("VOICE: WAITING", self)
        self.voice_chip.setGeometry(self.sw - 290, 40, 250, 40)
        self.voice_chip.setStyleSheet("""
            background-color: rgba(0, 0, 0, 150);
            color: #ffffff;
            border-right: 5px solid #ff00ff;
            padding-right: 15px;
            font-family: 'Consolas';
            font-size: 14px;
        """)

        # 4. DATA POLLING
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_hud)
        self.timer.start(500)
        
        self.last_state = {}

    def update_hud(self):
        try:
            if os.path.exists(STATE_FILE):
                with open(STATE_FILE, "r") as f:
                    state = json.load(f)
            else:
                state = {}
        except: return

        # Identity Visualization
        is_locked = state.get("is_locked", False)
        identity_status = state.get("identity", "UNKNOWN")
        
        if is_locked:
            self.id_badge.setText("⚠️ SECURITY LOCKDOWN")
            self.id_badge.setStyleSheet(self.id_badge.styleSheet().replace("#00ffcc", "#ff4444"))
        elif identity_status == "VERIFIED":
            self.id_badge.setText("🛡️ ACCESS GRANTED: ARCHITECT")
            self.id_badge.setStyleSheet(self.id_badge.styleSheet().replace("#ff4444", "#00ffcc"))
        else:
            self.id_badge.setText("📡 SCANNING IDENTITY...")
            self.id_badge.setStyleSheet(self.id_badge.styleSheet().replace("#ff4444", "#00ffcc"))

        # Mode Updates
        vision_mode = state.get("vision_mode", "hand").upper()
        voice_mode = state.get("voice_mode", "normal").upper()
        
        self.mode_chip.setText(f"TRACKING: {vision_mode}")
        self.voice_chip.setText(f"VOICE: {voice_mode}")

    def paintEvent(self, event):
        # Optional: Draw futuristic corner brackets or scanlines
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        pen = QPen(QColor(0, 255, 204, 80))
        pen.setWidth(1)
        painter.setPen(pen)
        
        # Corner Brackets
        m = 20 # margin
        s = 50 # length
        # Top Left
        painter.drawLine(m, m, m+s, m)
        painter.drawLine(m, m, m, m+s)
        # Top Right
        painter.drawLine(self.sw-m, m, self.sw-m-s, m)
        painter.drawLine(self.sw-m, m, self.sw-m, m+s)
        # Bottom Left
        painter.drawLine(m, self.sh-m, m+s, self.sh-m)
        painter.drawLine(m, self.sh-m, m, self.sh-m-s)
        # Bottom Right
        painter.drawLine(self.sw-m, self.sh-m, self.sw-m-s, self.sh-m)
        painter.drawLine(self.sw-m, self.sh-m, self.sw-m, self.sh-m-s)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    hud = TommyHUD()
    hud.show()
    sys.exit(app.exec())
