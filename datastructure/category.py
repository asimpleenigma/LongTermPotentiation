# Category

#from numpy import *
#from activationfunctions import *
from aspect import *

home['category'] = Aspect('category')
class Category(Aspect):
    def __init__(self, category_name):
        Aspect.__init__(self, category_name)
    
        if not 'category' in home:
            print id(home)
            home['category'] = Aspect('category')
        
        home['category'][category_name] = self


class Instance(Aspect):
    def __init__(self, instance_name, mapping=dict()):
        Aspect.__init__(self, instance_name, mapping)
        category_name = self.__class__.__name__
        
        if not category_name in home['category']:
            Category(category_name)
            
        home['category'][category_name][self.name] = self
