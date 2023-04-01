from miranda.framework.handle.plugins.base_plugin import BasePlugin
from PySide6.QtWidgets import QMainWindow

class Plugin2(BasePlugin):
    def __init__(self):
        super().__init__()
        
    def reverse(self, text):
        return text[::-1]
    
    def change(self, win):
        win.setWindowTitle('Plugin changed this')