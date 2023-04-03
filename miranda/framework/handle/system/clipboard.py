# clipboard = QApplication.clipboard()
# clipboard.setText("I've been clipped!")
# clipboard.text()
from miranda.framework.core.runner.app import App

class Clipboard:
    app = App.app.clipboard()
    
    @staticmethod
    def setText(text):
        Clipboard.app.setText(text)
    
    @staticmethod
    def getText():
        return Clipboard.app.text()