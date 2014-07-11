# -*- coding: UTF-8  -*-

import sys, os

class Response:
        
    
    headersCollection = []
    
    
    def httpResponse(self):
        for x in self.headersCollection:
            print x
        print "Content-type: text/html;  charset: UTF-8; \n\n"
        
        
    def redirect(self, url):
        
        print "Location: http://"+os.environ['SERVER_NAME']+url+"\n"
        print "Connection: close\n"
        sys.exit(1)
        
    def setHeader(self, header):
        self.headersCollection.append(header)
        return self