# -*- coding: UTF-8  -*-

import time, os, shelve, sha

class Session:
    
    # collection of cookies to send before send headers
    collection = {}
    
    # cookie live time
    expires = 900 # 15 minut
    
    # session id 
    sessionId = ''
    
    # session cookie name
    sessionIdCookieName = 'PY_SESSID'
    
    # session directory
    sessionDir = 'tmp/.session'
    
    # shelve object 
    session = ''
    
    
    def __init__(self):
        self.sessionId = self.get(self.sessionIdCookieName)
        if(not self.sessionId):
            self.sessionId = sha.new(repr(time.time())).hexdigest()
            self.set(self.sessionIdCookieName, self.sessionId)
        
        
        self.sessionDir = os.environ["PY_PATH"]+'/'+self.sessionDir
        
        if(not os.path.exists(self.sessionDir)):
            os.makedirs(self.sessionDir)
        
        self.session = shelve.open(self.sessionDir + '/sess_' + self.sessionId, writeback=True)
        
    # set cookie 
    # @param name cookie name
    # @param value cookie value    
    # @return  self
    def set(self, name, value):
        self.collection[name] = [value, self.expires]
        return self
        
    # get value from cookie
    # @param name cookie name
    # @return cookie value or empty string if cookie does not exist
    def get(self, name):
    
        if os.environ.has_key('HTTP_COOKIE'):
            for cookie in os.environ['HTTP_COOKIE'].split(';'):   
                cookie = cookie.strip(' \t\n\r/')
                cookie = cookie.split('=')
                if name == cookie[0]:
                    return cookie[1]
        return ''
                
    def debug(self):
        return 'SID: '+self.sessionId+' -- V: '+str(self.getSession('dupa'))
        
    # write cookie headers    
    def setCookies(self):
        future = time.time()
        
        for name, value in self.collection.iteritems():    
            expires = time.strftime("%A, %d-%m-%Y %H:%M:%S %Z", time.gmtime(future + value[1]))
            print "Set-Cookie:"+(name)+"="+(value[0])+";Expires="+(expires)+";"
            
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
     
    
        