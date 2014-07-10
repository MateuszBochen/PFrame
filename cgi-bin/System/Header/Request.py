# -*- coding: UTF-8  -*-

import cgi


class Request:
    
    kernelObj = 0
    
    segments = []
    
    def __init__(self, kernel):        
        self.kernelObj = kernel
    
    def getCurrentUrl(self):
        currentUrl = self.kernelObj.kernelOS.environ["REQUEST_URI"].replace(self.kernelObj.config['DIRECTORY'], '')
        return currentUrl.strip(' \t\n\r/');
        
    def getSegment(self):
    
    
    def getSegments(self):
        return self.segments 