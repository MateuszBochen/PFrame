# -*- coding: UTF-8  -*-

class Framework:
        
    app = 0
    
    def __init__(self, kernel):
        self.app = kernel
    
    
        
    def path(self, path):
        return self.app.config['DIRECTORY']+'/'+path
        
    def redirect(self, url):
        return self.app.responseObject.redirect(url)
        
    def module(self, name):
        return self.app.autoloader.load(name)
        
    def file(self, path):
        return self.app.config['DIRECTORY']+'/'+path
     
    def tFile(self, path):
        myPath = self.app.kernelOS.environ["PY_PATH"].replace(self.app.kernelOS.path.dirname(self.app.kernelOS.environ["SCRIPT_NAME"]), '')
        # /home/backen/ftp/
        # return myPath
        return self.app.config['DIRECTORY']+'/'+self.app.config['TEMPLATE_DIR']+'/'+self.app.config['TEMPLATE_NAME']+'/'+path
        
       
        
    def render(self, template, data, mainFile = False):
        if(mainFile != False):
            self.app.templating.setMainFile(mainFile)
        return self.app.templating.render(template, data)