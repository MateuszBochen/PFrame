# -*- coding: UTF-8  -*-

import os,string
from System.Templating import airspeed


class Templating:
    
    viewReady = ''
    
    mainFile = 'index.html'
    
    app = 0
    
    def __init__(self, app):
        self.app = app
    
    def setMainFile(self, fileName):
        self.mainFile = fileName+'.html'
    
    
    def render(self, template, data):
        
        content = ''
        
        partFile = 'index'
        if(template !=''):
            partFile = template
        
        fw = self.app.framework    
        
        myPath = os.environ["PY_PATH"].replace(os.path.dirname(os.environ["SCRIPT_NAME"]), '')
        
        # część szablonu
        partPath = myPath+'/'+self.app.config['DIRECTORY'] +'/'+self.app.config['TEMPLATE_DIR']+'/'+self.app.config['TEMPLATE_NAME']+'/Apps/'+self.app.appName+'/'+self.app.controller+'/'+partFile+'.html'
        mainPath = myPath+'/'+self.app.config['DIRECTORY'] +'/'+self.app.config['TEMPLATE_DIR']+'/'+self.app.config['TEMPLATE_NAME']+'/'+self.mainFile
        
        if(os.path.isfile(partPath)):
            size = os.path.getsize(partPath)
            templateString = open(partPath).read(size)
            t = airspeed.Template(templateString)
            content = t.merge(locals())
        else:
            content = 'Taki widko nie istnieje'
        
        # główny plik szablonu
        if(os.path.isfile(mainPath)):
           size = os.path.getsize(mainPath)
           templateString = open(mainPath).read(size)
           
           t = airspeed.Template(templateString)
           
           self.viewReady = t.merge(locals())
            
        else:
            self.viewReady = os.environ["PY_PATH"]
    
    def display(self):
        print self.viewReady
        
        
    #def extract(self, data):
        
        
    