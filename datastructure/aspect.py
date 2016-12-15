# Aspect

from numpy import *
#from activationfunctions import *
from importcsv import *
#from scipy.stats.mstats import gmean

__all__ = ['Aspect', 'home', 'deeply']
             

class Aspect(dict):
    """ Dictionary base class for data structures.
        Has attributes: name
        Terms for types of aspects: Data Structure > Category > Instance > Attribute.
                e.g. Categories > Country > United States > GDP"""
    def __init__(self, name, mapping=dict() ):#, associations=set() ):#, value_function=lambda x:None):
        dict.__init__(self, mapping)
        self.name         = name
        #self[value]        = value_function(self)
        #self.image        = set()
        #self.associations = associations

    def update(self, alt_self=dict()):
        """ Takes an instance of the same name as self.
            Updates the attribute values in self with those in the given instance."""
        if isinstance(alt_self, Aspect):
            assert alt_self.name == self.name
        dict.update(self, alt_self)
        #self[value]  = value_function(self)

    def instancesWith(self, attribute_names):
        """ Takes a list of attribute names.
            Returns a list of the names of all instances contained in category self 
                that have all given attribute keys in their domain. """
        instance_names = set(self)             # take set of all instances in category that have all attributes so far 
        for attr_name in attribute_names: # for each attr name given
            result = set()                  # find the set of all instances with attr
            for inst_name in self:           # for each instance in the category
                if attr_name in self[inst_name]: # if instance has attr
                    result |= set([inst_name])         # add instance to result
            instance_names &= result         # remove any instances that do not have attr
        return instance_names

    #def associateWith(self, super_aspect):
     #   self.associations[super_aspect.name] = super_aspect
        
    #def incorporate(self, sub_aspect):
     #   self[sup_aspect.name] = sub_aspect
    
    def assimilateData(self, file_path):
        """ Takes csv file path.
            Updates the data structure self to them."""
        
        formated_data   = formatData(extractData(file_path)) # list of list of strings
        category_name   = formated_data[0].pop(0)  # string; e.g. "Country"
        if category_name not in self:
            self[category_name] = Aspect(category_name)
        category = self[category_name]
        attribute_names = formated_data.pop(0) # list of strings e.g. ['GDP (Per Capita) (by CIA)']
        n_attributes       = len(attribute_names)
        for row in formated_data: # for each data sample
            instance_name = row.pop(0)
            instance = Aspect(instance_name) # create an instance
            #print instance_name
            for n in range(n_attributes): # for each attribute
                #print row
                try:                     # assign attribute
                    instance[attribute_names[n]] = float(row[n]) 
                except(ValueError):     # do nothing if not convertable to int
                    pass
            if instance_name not in category: # if category doesn't have instance
                category[instance_name] = Aspect(instance_name) # make it one.
            category[instance_name].update(instance) # update category's instance to the new constructed one.
            
home = Aspect('home') # the "home directory" of the united data structure      

def deeply(method):
    def wrapper(*args):
        for consitit in self:    # for each neuron group:
            try:
                self[consitit].method(*args)    # find how future net values are affected from propagations this timestep.
            except:
                pass
    return wrapper
