# -*- coding: UTF-8  -*-




class Controller:
    
    framework = 0
    
    def __init__(self, kernel):        
        self.framework = kernel
    
    def defaultRun(self):
        
        # pobieranie sesji
        session = self.framework.module('System.Http.Session');
        
        user = session.get('User');
        token = session.get('Token');
        baseName = session.get('BaseName');
        
        
        
        if(user and token):
            user = session.get('User');
            token = session.get('Token');
        else:
            #return self.framework.path('Authorization/Login')
            return self.framework.redirect(self.framework.path('Authorization/Login'))
            
        
        #session.set('User', 'backen').set('Token', 'hwdp')
        
        
        
        return session.get('User')