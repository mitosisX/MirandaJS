"""
20 March, 2023 8:23 AM (Monday) (UTC+02:00)

The code is a mess, I know.... get over it... or simply fix it ;-)
"""

import js2py
from js2py import base
import sys
import os
import sqlite3
from faker import Faker

import miranda # importing like this to get the root folder of the module

# The application's mainloop
from miranda.framework.core.runner.app import App
from miranda.framework.components.controls.dockers.menu.menuitem import MenuItem
# from miranda.framework.components.controls.dockers.menubar.submenu import SubMenu
from miranda.framework.components.controls.dockers.toolbar.toolbar_button import ToolbarButton
from miranda.framework.components.controls.dockers.toolbar.toolbar import Toolbar
from miranda.framework.components.controls.dockers.dockerwidget.docking import Docker

from miranda.framework.components.controls.widgets.widget import Widget
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
from miranda.framework.components.controls.dockers.menubar.menubar_item import MenuItem
from miranda.framework.components.controls.dockers.menubar.menubar import Menubar

from miranda.framework.components.controls.widgets.containers.tab import Tab
from miranda.framework.components.controls.widgets.containers.tabitem import TabItem
from miranda.framework.components.controls.widgets.fluent.folderlist import FolderList

# Plugins
from miranda.framework.handle.plugins.plugin_manager import PluginManager
from miranda.framework.handle.paths.misc_paths import Paths

class Engine:
    _instance = None

    # For whatever or whoever's reason, dare not have two engine instances running
    # Here's your singleton design pattern
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.engine = None
        return cls._instance
    
    def __init__(self):
        
        self.app = App() # holds the PySide6 application
        self.plugin_manager = PluginManager() # The code that init all user plugins
        
        self.miranda_root_dir = Paths.miranda_sitepackage_path()
        
        self.engine = None #holds the js2py engine
        
        # All python objects to be used in JS
        self.__pyObjects = {
            'scripts': Paths.scripts,
            'images': Paths.images,
            '__js_execute': self.execute,
            '__file': File,
            'fake': Faker(),
            # 
            # 
            # 
            'Window': Window,
            'Widget': Widget,
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
            'Theme': Theme,
            'Menubar': Menubar,
            'Menu': Menu,
            'MenuItem': MenuItem,
            # 'SubMenu': SubMenu,
            'Dock': Docker,
            'Toolbar': Toolbar,
            'ToolbarButton': ToolbarButton,
            'sqlite': sqlite3,
            'len': len,
            'alert': MessageBox,
            'Timer': Timer,
            'cmd': CMD,
            '__clipboard': Clipboard,
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
        
        # print('In engine')
        
    # Init the JavaScript engine
    def init_JsEngine(self):
        self.engine = js2py.EvalJs(self.__pyObjects, enable_require=True)
        # print('pybjects set to JS engine')
        
    """
    Sequence:
        1) Initialize plugins first
            * Set them to the __pyObject dict
        2) Set the dict to the JS engine
        3) Execute any vital JS files for the framework, ie, miranda.js
        4) Execute main.js
        5) Eventloop
        
    """
    def start(self):            
        self.init_plugins() # Has to load first coz we don't walk the engine to run before with only our py objects
        self.init_JsEngine() # Set the py objects to the engine
        self.execute_vital_js() # Set the py objects to the engine
        self.execute_main_js() # Set the py objects to the engine
        self.set_eventloop() # Set the PySide6 mainloop running. VITAL!!!!!!
        
    # All core js code for the Miranda framework
    def execute_vital_js(self):
        vital_files = [
            'framework.scripts.miranda',
            ]
        
        for vital_file in vital_files:
            clean_path_file = os.path.join(self.miranda_root_dir, Paths.dot_path(vital_file) + '.js')
            self.execute(clean_path_file)
                
                    
    """
    For executing any incoming JavaScript code
    
    Has to redesigned to determine whether or not the framework is being run after freeze or in "IDE"
    """
    def execute(self, script):
        # print('Executing')
        with open(script) as js_script:
            js_content = js_script.read()
            
            self.engine.execute(js_content)
    
    # The user's main.js entry point code
    def execute_main_js(self):
        path_to_main = Paths.scripts('main.js')
        self.execute(path_to_main)
    
    """
    param: objects 
    type: dict
    
    Used for plugin development, setting python objects to the JavaScript engine
    """
    def set_objects(self, objects):
        self.__pyObjects.update(objects)
        
    # The PySide6 engine that handles the mainloop of the program
    def set_eventloop(self):
        # print('PySide6 app mainloop')
        self.app.execute()
        
    """
    Load and intialize all plugins from the user
    """
    def init_plugins(self):
        # print('Init plugins')
        self.plugin_manager.load_plugins()
        self.plugin_manager.activate_plugins()
        
        self.set_objects(self.plugin_manager.plugin_pyobjects())