# -*- coding: UTF-8  -*-

import time, os, shelve, sha



class Session:
    
   
    
   
    
    # session id 
    sessionId = ''
    
    # session cookie name
    sessionIdCookieName = 'PY_SESSID'
    
    # session directory
    sessionDir = 'tmp/.session'
    
    # shelve object 
    session = ''
    
    cookie = ''
    
    def __init__(self, cookieObj):
        self.cookie = cookieObj
        
        
        self.sessionId = self.cookie.get(self.sessionIdCookieName)
        if(not self.sessionId):
            self.sessionId = sha.new(repr(time.time())).hexdigest()
            self.cookie.set(self.sessionIdCookieName, self.sessionId)
        
        
        self.sessionDir = os.environ["PY_PATH"]+'/'+self.sessionDir
        
        if(not os.path.exists(self.sessionDir)):
            os.makedirs(self.sessionDir)
        
        self.session = shelve.open(self.sessionDir + '/sess_' + self.sessionId, writeback=True)
        
    
        
    
                
    def debug(self):
        return 'SID: '+self.sessionId+' -- V: '+str(self.getSession('dupa'))
        
    
            
    # get session value
    # @param name session name (session key)
    # @return session value if session exist or empty string otherwise
    def getSession(self, name):
        if(self.session.has_key(name)):
            return self.session.get(name)
        return ''
    
    # set session value
    # @param name session name (session key)
    # @param value session value
    # @return self
    def setSession(self, name, value):        
        self.session[name] = value
        self.session.close() 
        self.session = shelve.open(self.sessionDir + '/sess_' + self.sessionId, writeback=True)
        return self
     
    
        