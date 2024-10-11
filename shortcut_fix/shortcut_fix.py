from krita import *
from PyQt5.QtCore import QTimer

VK_F22 = 0x85
KEYEVENTF_KEYDOWN = 0x0
KEYEVENTF_KEYUP = 0x2

# 轮询间隔，ms
INTERVAL = 100

def release_key(vk_code):
    import ctypes
    # when it's pressed, release it.
    # 检查是否按下是必要的，直接抬起F22的话会导致win键偶尔不能用，不知道原因
    if ctypes.windll.user32.GetAsyncKeyState(vk_code) & 0x8000:
        ctypes.windll.user32.keybd_event(vk_code, 0, KEYEVENTF_KEYUP, 0)

class shortcut_fix(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def go(self):
        release_key(VK_F22)
        QTimer.singleShot(INTERVAL, self.go)

    def setup(self):
        self.go()

    def createActions(self, window):
        pass

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(shortcut_fix(Krita.instance())) 
