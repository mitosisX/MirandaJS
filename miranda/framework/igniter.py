# 
# from project Abigail 
#   - Every code I write falls under "project Abigail"
# 
# This is Miranda framework, named after one of Neptune's moon, simply because
# of it's destinct features (uniqueness).
# 
# 25 November, 2022 (11:25 am) (UTC+02:00) Malawi, Africa
# Re-writing this after the first working source-code got lost
# P.S: Neglegence to utilize github's power
# 
# 

import js2py
from js2py import base
import sys
import os
import sqlite3

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
from miranda.framework.components.controls.widgets.calendar import Calendar
from miranda.framework.components.controls.widgets.groupbox import GroupBox
from miranda.framework.components.controls.widgets.table import TableGrid
from miranda.framework.components.controls.widgets.radiobutton import RadioButton
from miranda.framework.components.controls.widgets.label import Label
from miranda.framework.components.controls.widgets.window import Window
from miranda.framework.components.controls.widgets.combobox import ComboBox
from miranda.framework.components.layouts.olayout import OLayout
from miranda.framework.components.layouts.vlayout import VerticalLayout
from miranda.framework.components.layouts.hlayout import HorizontalLayout
from miranda.framework.components.layouts.grid import GridLayout
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

from miranda.framework.handle.theming.themer import Theme
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

# Playground code
# from playground.fromtemplate import TemplateGenerator

#  use
# pyqtdarktheme
# qdarkstyle
#

from win11toast import toast
# gets the path for the user files
src = os.path.join(os.getcwd(), 'source')

def images(path):
    global src
    return os.path.join(
        src, 'images',
        path.to_string().value if type(path) == base.PyJsString else path)

def scripts(path):
    global src
    return os.path.join(
        src, 'scripts',
        path.to_string().value if type(path) == base.PyJsString else path)

app = App()

"""
All keys marked by __ signify that I do not intent them to be accessed directly by the user
but by some internal JS function
"""
objects = {
    # 'app': MirandaApp,
    'scripts': scripts,
    'images': images,
    '__file': File,
    'toast': toast,
    # 
    # 
    # 
    'Window': Window,
    'Button': Button,
    'Calendar': Calendar,
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
    'VLayout': VerticalLayout,
    'HLayout': HorizontalLayout,
    'GroupBox': GroupBox,
    'TableGrid': TableGrid,
    # 
    # 
    # 
    'Theme': Theme,  # Replace with class to access different theming styles
    'themes': list_themes(),
    'Menu': Menu,
    'MenuItem': MenuItem,
    'Menubar': Menubar,
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

context = js2py.EvalJs(objects, enable_require=True)

# The main entry file of the user's JS file

app_code = open('framework\scripts\miranda.js', 'r').read()
js_code = open(scripts('tablegrid.js'), 'r').read()

context.execute(app_code)
context.execute(js_code)

sys.exit(app.execute())
