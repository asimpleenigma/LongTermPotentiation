# Benjamin Lloyd Cloer
# trainingdata

from numpy import *
#from activationfunctions import *
from scipy.stats.mstats import gmean

__all__ = ['DataSet']

class DataSet(object):
    """ Class object to be passed to the network 'train' method.
        ''DataSet'' takes a list of attributes.
    """
    def __init__(self, category, attribute_names, scalar_normalize=True,
                 magnitude_normalize=True, name=None):
        
        instance_names = category.instancesWith(attribute_names) # find instances that have all attributes
        
        instance_names = list(instance_names)
        
        data = []
        for inst_name in instance_names:
            row = []
            for attr_name in attribute_names:
                row += [category[inst_name][attr_name]]
            data += [row]
        data = array(data)
        
        

        self.name            = name
        self.category        = category
        self.attribute_names = attribute_names
        self.instance_names = instance_names
        self.n_attributes    = len(attribute_names)
        self.n_instances     = len(instance_names)
        self.data            = data
        
    def __str__(self):
        # floats in printed arrays are 17 spaces apart
        string = ""
        if self.name:
            string += str(self.name) + "\n"
        string += self.category.name + "\t"
        for attr_name in self.attribute_names:
            string += attr_name + "\t"
        for row in range(self.n_instances):
            string += "\n" + self.instance_names[row]
            for entry in range(self.n_attributes):
                string += "\t" + str(self.data[row][entry])
        return string
     

