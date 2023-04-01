from PySide6.QtWidgets import QComboBox
from PySide6.QtGui import QAction, QIcon

# setMaxCount - sets maximum ComboBox items limit

# QComboBox.NoInsert	No insert
# QComboBox.InsertAtTop	Insert as first item
# QComboBox.InsertAtCurrent	Replace currently selected item
# QComboBox.InsertAtBottom	Insert after last item
# QComboBox.InsertAfterCurrent	Insert after current item
# QComboBox.InsertBeforeCurrent	Insert before current item
# QComboBox.InsertAlphabetically	Insert in alphabetical order


class ComboBox(QComboBox):

    def __init__(self):
        super().__init__()

    def onItemSelect(self, func):
        self.currentIndexChanged.connect(
            lambda: func(self, self.currentText()))

    def getSelectedItem(self):
        return self.currentText()

    """
    This displays an image and text on the combobox
    [images('image'), 'text']
    """

    def addImageItems(self, *data):
        for values in data:
            icon = QIcon(values[0])
            text = values[1]

            self.addItem(icon, text)