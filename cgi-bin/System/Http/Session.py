# -*- coding: UTF-8  -*-

import time, os

class Session:
    
    collection = {}
    expires = 900
    
    def set(self, name, value):
        self.collection[name] = [value, self.expires]
        return self
        #print "Set-Cookie:UserID=XYZ;\r\n"
        #print "Set-Cookie:Password=XYZ123;\r\n"
        #print "Set-Cookie:Expires=Tuesday, 31-Dec-2007 23:12:40 GMT";\r\n"
        #print "Set-Cookie:Domain=www.tutorialspoint.com;\r\n"
        #print "Set-Cookie:Path=/perl;\n"
        #print "Content-type:text/html\r\n\r\n"
    
    def get(self, name):
    
        if os.environ.has_key('HTTP_COOKIE'):
            for cookie in os.environ['HTTP_COOKIE'].split(';'):   
                cookie = cookie.strip(' \t\n\r/')
                cookie = cookie.split('=');
                if name == cookie[0]:
                    return cookie[1]
        return ''
                
        
        
    def setCookies(self):
        future = time.time()
        
        for name, value in self.collection.iteritems():    
            expires = time.strftime("%A, %d-%m-%Y %H:%M:%S %Z", time.gmtime(future + value[1]))
            print "Set-Cookie:"+(name)+"="+(value[0])+";Expires="+(expires)+";"