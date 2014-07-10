# -*- coding: UTF-8  -*-




class Autoloader:
    
    collections = {}
    kernelObj = 0
    
    def __init__(self, kernel):
         self.kernelObj = kernel
   
    
    def load(self, name, asNew = False, addKernel = False):
        
        if(name in self.collections and asNew == False):           
            return self.collections[name]       
            
        if(self.moduleExists(name)):
            self.collections[name] = self.kernelObj.imortLib.import_module(name)
            
            if(addKernel):
                if(asNew):
                    return getattr(self.collections[name], name.split('.')[-1])(self.kernelObj)
                self.collections[name] = getattr(self.collections[name], name.split('.')[-1])(self.kernelObj)
            else:
                if(asNew):
                    getattr(self.collections[name], name.split('.')[-1])()
                self.collections[name] = getattr(self.collections[name], name.split('.')[-1])()
            
            return self.collections[name]
        return False
            
    def moduleExists(self, moduleName):     
        moduleName = moduleName.replace('.', '/')            
        return self.kernelObj.kernelOS.path.isfile(self.kernelObj.kernelOS.environ["PY_PATH"] +'/'+moduleName+'.py')
        
           