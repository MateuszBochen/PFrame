# -*- coding: UTF-8  -*-

import cgi, cgitb

class Post:
        
    form = []
    
    def __init__(self):
        self.form = cgi.FieldStorage()
    
    def get(self, name):
        return self.addslashes(self.form.getvalue(name))
    
    def getForm(self):
        return self.form
        
    def addslashes(self, s):
        l = ["\\", '"', "'", "\0", ]
        for i in l:
            if i in s:
                s = s.replace(i, '\\'+i)
        return s