# -*- coding: UTF-8  -*-

import sys, os

class Response:
        
    
    def setHttpResponse(self):
        print "Content-type: text/html;  charset: UTF-8; \n\n"
        
    def redirect(self, url):
        #print "HTTP/1.1 302 Found"
        #print "Content-type: text/html;  charset: UTF-8;\n"
        #print "HTTP/1.1 302 Found"
        #print os.environ['SERVER_NAME']
        print "Location: http://"+os.environ['SERVER_NAME']+url+"\n"
        print "Connection: close\n"
        sys.exit(1)