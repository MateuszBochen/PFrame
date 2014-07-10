# -*- coding: UTF-8  -*-

class Login:
        
    
    framework = 0
    
    def __init__(self, app):        
        self.framework = app
        
    def defaultRun(self):
        
        message = 'ok'
        type = 'alert'
        
        form = self.framework.module('System.Http.Post');
        database = self.framework.module('System.Database.MySql');
                
        return self.framework.render('', {'message': message, 'type': type}, 'clear')