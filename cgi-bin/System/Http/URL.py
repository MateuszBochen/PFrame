# -*- coding: UTF-8  -*-

import cgi


class URL:
    
    kernelObj = 0
    
    segments = []
    currentUrl = ''
    
    def __init__(self, kernel):        
        self.kernelObj = kernel
        self.currentUrl = self.kernelObj.kernelOS.environ["REQUEST_URI"].replace(self.kernelObj.config['DIRECTORY'], '')        
        self.currentUrl = self.currentUrl.strip(' \t\n\r/')       
        self.segments = self.currentUrl.split('/')
        
    
    def getCurrentUrl(self):        
        return self.currentUrl
        
    def getSegment(self, index):
        if(index > len(self.segments)-1):
            return ''
        
        return self.segments[index]
        
    def getSegments(self):
        return self.segments