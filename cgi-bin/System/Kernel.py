# -*- coding: UTF-8  -*-

import importlib, os

class Kernel:
    
    kernelOS = 0
    config = {}
    autoloader = 0
    imortLib = 0
    responseObject = 0
    
    framework = 0
    templating = 0
    # """ Konstruktor """
    def __init__(self):
        self.kernelOS = os
        self.imortLib = importlib
        
        # Pobieranie ustawien
        configs = importlib.import_module("Config.Config")
        self.config = configs.config
        
       
        # Odpalanie autoloadera
        self.autoloader = importlib.import_module("System.Autoloader.Autoloader")
        self.autoloader = self.autoloader.Autoloader(self);
        
        self.responseObject = self.autoloader.load('System.Http.Response')
       
        
        
        
        requestObject = self.autoloader.load("System.Http.Request", False, True)        
        
        firstSegment = requestObject.getSegment(0);
        
        end = 'Front'
        appName = 'Homepage'
        controller = 'Controller'
        method = 'defaultRun'
        
        segment = 0
        
        
        
        if(firstSegment == self.config['ADMIN_DIR']):
            segment += 1;
            firstSegment = requestObject.getSegment(segment);
            end = 'Back'            
        
        segment += 1;
        
        if(firstSegment != ''):           
            appName = firstSegment
        
        controllerSegment = requestObject.getSegment(segment);
        
        segment += 1;
        
        
        if(controllerSegment != ''):
            controller = controllerSegment
            
        methodSegment = requestObject.getSegment(segment);
        
        if(methodSegment != ''):
            method = methodSegment+'Run'
        # dodatek do szablon�w
        self.appName = appName
        self.controller = controller
        # odpalanie managera szablon�w
        self.templating = self.autoloader.load('System.Templating.Templating', True, True)
        self.framework = self.autoloader.load("System.Framework.Framework", True, True)
        
        
        modulePath = 'Applications.'+end+'.'+appName+'.'+controller
        
        if(not(self.autoloader.moduleExists(modulePath))):
            print "nie ma takiego modu�u <b>"+modulePath+"  </b>"
            return False
        
        newApp = importlib.import_module(modulePath)
        
        
            
        controller = getattr(newApp, controller)(self.framework)
        
        if(not(method in dir(controller))):
            print "nie ma takiej metody"
            return False
            
        
            
        controlerres = getattr(controller, method)()
        
        # Wysy�anie ciasteczek
        self.autoloader.load('System.Http.Session').setCookies()
        
        # Wysy�anie nag��wka do przegl�darki
        self.responseObject.setHttpResponse()
        self.templating.display()
        