# -*- coding: UTF-8  -*-


class Login:
        
    
    framework = 0
    
    def __init__(self, app):        
        self.framework = app
        
    def defaultRun(self):
        
        message = ''
        type = 'alert'
        
        form = self.framework.module('System.Http.Header.Post');
        database = self.framework.module('System.Database.MySql');
        
        session = self.framework.module('System.Http.Session');
        
        session.set('dupa', {'dfsdf': 1, 'dfssdfdf': 1, 'dfsdfsdff': 1 })
                    
        
   
       
        
                    
        #return self.framework.render('', {'message': session.debug(), 'type': type}, 'clear')
        return self.framework.render('', {'message': message, 'type': type}, 'clear')