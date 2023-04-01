from PySide6.QtWidgets import QDockWidget, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class Docker(QDockWidget):
    def __init__(self, title = "Dock", parent=None,):
        super().__init__(title, parent = parent)
        
        self.widget = QWidget()
        self.setWidget(self.widget)
        
        self.setMagneticAreas()
        
    """
    we want PyQt to save and restore the dock widget’s
    size and position, and since there could be any number of dock widgets, PyQt
    uses the object name to distinguish between them
    """
    def setName(self, name):
        self.setObjectName(name)
        
    """
    Represents areas permitted areas for docking; more like magnetic areas
    could have been setAreas but I thought the "magnetic" name madeit look
    cool instead.
    
    Coz whenever one tries to dock some widget onto some areas, the allowed areas
    respond with a strong magnetic pull to signal the use that the particular area
    is ready to dock.
    
        Available positional enums
    NoDockWidgetArea
    LeftDockWidgetArea
    RightDockWidgetArea
    TopDockWidgetArea
    BottomDockWidgetArea
    AllDockWidgetAreas
    DockWidgetArea_Mask  
    """
    def setMagneticAreas(self, *areas):
        self.setAllowedAreas(Qt.LeftDockWidgetArea|
                            Qt.RightDockWidgetArea)
        
    def setTitle(self, title):
        self.setWindowTitle(title)
        
    def setIcon(self, icon):
         self.setWindowIcon(QIcon(icon))
         
    def setSize(self, width, height):
        self.resize(width, height)
        
    def addChild(self, child):
        
        self.setWidget()