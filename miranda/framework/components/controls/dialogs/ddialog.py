from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QDialogButtonBox

"""
This is a Dumb Dialog. Oftenly used for "Ok", "Cancel" operations
"""
class DDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok
                                          |QDialogButtonBox.Cancel)
        self.buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
        