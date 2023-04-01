import os
from js2py import base

class Paths:
    project_path = os.getcwd() # Better to be static for easy access in multiple locations
    
    @classmethod
    def scripts(cls, resource):
        return cls.path_res_joiner('js', resource)

    @classmethod
    def images(cls, resource):
        return cls.path_res_joiner('images', resource)
        
    @classmethod
    def plugins(cls):
        return cls.path_res_joiner(Paths.project_path, 'plugins')
            
    # When the below methods are called from JS, the arguments no longer gets treated
    # as a string, rather some js2py type and that's why I had to write the conditional setting
    @classmethod
    def path_res_joiner(cls, path, resource):
        return os.path.join(
            cls.project_path, path,
            resource.to_string().value if type(resource) == base.PyJsString else resource)