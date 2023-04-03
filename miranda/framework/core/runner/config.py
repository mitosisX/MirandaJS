from PySide6.QtWidgets import QApplication, QWidget
from qt_material import apply_stylesheet
from qt_material import list_themes
from miranda.framework.components.controls.dockers.menu.menuitem import MenuItem
from miranda.framework.components.controls.dockers.toolbar.toolbar_button import ToolbarButton
from miranda.framework.components.controls.dockers.dockerwidget.docking import Docker

# COllection of userful utilities
# from miranda.framework.handler.scripts.miranda import MirandaApp

# Tis is the class that controls the whole application
# event loop
from miranda.framework.core.runner.app import App
 
from miranda.framework.components.controls.widgets.button import Button
from miranda.framework.components.controls.widgets.checkbox import CheckBox
from miranda.framework.components.controls.widgets.radiobutton import RadioButton
from miranda.framework.components.controls.widgets.label import Label
from miranda.framework.components.controls.widgets.window import Window
from miranda.framework.components.controls.widgets.combobox import ComboBox
from miranda.framework.components.controls.widgets.layouts.olayout import OLayout
from miranda.framework.components.controls.widgets.layouts.grid import GridLayout
from miranda.framework.components.controls.widgets.spinbox import SpinBox
from miranda.framework.components.controls.widgets.progressbar import ProgressBar
from miranda.framework.components.controls.widgets.slider import Slider
from miranda.framework.components.controls.widgets.textedit import TextEdit
from miranda.framework.components.controls.widgets.listbox import ListBox

from miranda.framework.components.controls.widgets.segmenter import Segmenter
from miranda.framework.components.controls.dockers.toolbar.toolbar import Toolbar
from miranda.framework.components.controls.dialogs.messagebox import MessageBox
from miranda.framework.components.controls.dialogs.inputdialog import InputDialog
from miranda.framework.components.controls.dialogs.ddialog import DDialog

from miranda.framework.components.controls.dialogs.popups.about_popup import AboutPopup
from miranda.framework.components.controls.dialogs.popups.critical_popup import CriticalPopup
from miranda.framework.components.controls.dialogs.popups.information_popup import InformationPopup
from miranda.framework.components.controls.dialogs.popups.question_popup import QuestionPopup
from miranda.framework.components.controls.dialogs.popups.warning_popup import WarningPopup

from miranda.framework.handle.theming.material.theme import Style
from miranda.framework.handle.system.clipboard import Clipboard
from miranda.framework.handle.system.timer import Timer
from miranda.framework.handle.system.cmdargs import CMD

from miranda.framework.handle.system.file import File
from miranda.framework.handle.system.paths import Paths
from miranda.framework.handle.system.taskbar_progress import TaskbarProgress
from miranda.framework.handle.system.notifcation import Notification
from miranda.framework.handle.system.tray import Tray

from miranda.framework.components.controls.dockers.menu.menu import Menu
from miranda.framework.components.controls.dockers.menu.menuitem import MenuItem
from miranda.framework.components.controls.dockers.menubar.menubar import Menubar

from miranda.framework.components.controls.widgets.containers.tab import Tab
from miranda.framework.components.controls.widgets.containers.tabitem import TabItem
from miranda.framework.components.controls.widgets.fluent.folderlist import FolderList

class Config:
    pyObjects = {
                # 'app': MirandaApp,
                'scripts': scripts,
                'images': images,
                '__file': File,
                # 
                # 
                # 
                'Window': Window,
                'Button': Button,
                'CheckBox': CheckBox,
                'RadioButton': RadioButton,
                'Label': Label,
                'ComboBox': ComboBox,
                'Layout': OLayout,
                'GridLayout': GridLayout,
                'Spinner': SpinBox,
                'InputDialog': InputDialog,
                'ProgressBar': ProgressBar,
                'Slider': Slider,
                'TextEdit': TextEdit,
                'ListBox': ListBox,
                # 
                # 
                # 
                'Theme': Style,  # Replace with class to access different theming styles
                'themes': list_themes(),
                'Menu': Menu,
                'MenuItem': MenuItem,
                'Menubar':Menubar,
                'Dock': Docker,
                'Toolbar': Toolbar,
                'ToolbarButton': ToolbarButton,
                'sqlite': sqlite3,
                'len': len,
                'alert': MessageBox,
                'Timer': Timer,
                'cmd': CMD,
                'Clipboard': Clipboard,
                'SysTray': Tray,
                
                'DDialog': DDialog,
                '__aPopup': AboutPopup,
                '__cPopup': CriticalPopup,
                '__iPopup': InformationPopup,
                '__qPopup': QuestionPopup,
                '__wPopup': WarningPopup,
                'Segmenter': Segmenter,
                'TaskbarProgress': TaskbarProgress,
                'Tab': Tab,
                'TabItem':TabItem,
                'List': FolderList,
                
                'Notification': Notification,
                '__paths': Paths,
                'console.log': print,
                'print': print,
                'str': str,
                'eval': eval,
                # 
                # 
                # 'TestMenu': TemplateGenerator
            }