from PySide6.QtWidgets import QMessageBox

class QuestionPopup:
    # The title can contain HTML elements too
    def __init__(self, parent, title, message, buttons):
        # self.msg_box = QMessageBox.question(parent, title, message)
        
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # Map the button text to the standard button
        button_map = {
            'yes': QMessageBox.Yes,
            'no': QMessageBox.No,
            'cancel': QMessageBox.Cancel,
            'ok': QMessageBox.Ok,
            'abort': QMessageBox.Abort,
            'retry': QMessageBox.Retry,
            'ignore': QMessageBox.Ignore,
            'save': QMessageBox.Save,
            'discard': QMessageBox.Discard,
            'apply': QMessageBox.Apply,
            'reset': QMessageBox.Reset,
            'restoredefaults': QMessageBox.RestoreDefaults,
        }

        # Add each button to the message box
        for button_text in buttons:
            button = button_map.get(button_text.lower())
            if button is not None:
                msg_box.addButton(button_text.lower(), button)

        # Display the message box and return the clicked button
        return msg_box.exec_()