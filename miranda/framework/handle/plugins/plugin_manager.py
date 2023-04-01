import importlib.util
import os
from miranda.framework.handle.plugins.base_plugin import BasePlugin
from miranda.framework.handle.paths.misc_paths import Paths

class PluginManager:
    def __init__(self):
        self.plugins = []
        self.objects = {} # To hold all objects to be set in the JavaScript engine
        
        self.dir_path = Paths.plugins() # loads plugins in the user's project dir
        self.folders = self.__filter_folders()

    def load_plugins(self):
        for folder in self.folders:
            
            if folder == "__pycache__":
                continue
            
            plugin_path = os.path.join(self.dir_path, folder)
            for filename in os.listdir(plugin_path):
                if filename.endswith(".py") and filename.startswith('main'):
                    module_name = os.path.splitext(filename)[0]
                    spec = importlib.util.spec_from_file_location(module_name, os.path.join(self.dir_path, folder, filename))
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    for name in dir(module):
                        obj = getattr(module, name)
                        if isinstance(obj, type) and issubclass(obj, BasePlugin) and obj is not BasePlugin:
                            self.plugins.append(obj())

    def activate_plugins(self):
        for plugin in self.plugins:
            plugin_name = type(plugin).__name__
            
            self.objects.update({plugin_name: plugin})
            
    # All python objects obtained from all the plugins
    def plugin_pyobjects(self):
        return self.objects
            
    # Get all the dirs the plugins dir in the user's project dirs
    def __filter_folders(self):
        folders = []
        
        for item in os.listdir(self.dir_path):
            if os.path.isdir(os.path.join(self.dir_path, item)):
                folders.append(item)
                
        return folders