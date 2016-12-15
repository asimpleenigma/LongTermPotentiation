# Constituent

from numpy import *

from datastructure import *
from biochem import *

__all__ = ['Constituent']

class Constituent(Aspect):
    """ Dictionary of state values of constituents contained in Networks.
        Attributes:
            regulator_names:    set of  that change state values
            derivative:         difference state values will change in next timestep
        Has methods:
            integrate: updates self.derivative
            activate:  advances to next time unit according to self.derivative
    """
    def __init__(self, name, mapping=dict() ):
        Aspect.__init__(self, name, mapping)
        self.regulator_names = set(self) & set(home['category']['Regulation'])
        self.derivative = Aspect('d('+str(self.name)+')/dt')
            
    def reset(self):
        self.regulator_names = set(self) & set(home['category']['Regulation'])
        self.derivative = Aspect('d('+str(self.name)+')/dt')
        for var in dynamic_variables & set(self):
            self.derivative[var] = zeros((self[var].shape))

    def integrate(self): # update self's derivative
        """ ``integrate`` updates self.derivative """
        for key in self.derivative:                     # for each regulated state variable
            self.derivative[key] = zeros((self[key].shape))
            #if key =='AMPA':
                #print 'integrate:'
                #print self['AMPA']
        for reg_name in self.regulator_names:           # for each regulator:
            home['category']['Regulation'][reg_name](self)  # find partial derivative with respect to it regulation
        
    def activate(self):
        """ ``activate`` updates constituent self according to it derivative. """
        for key in self.derivative:                     # for each regulated state variable
            #if key == 'AMPA':
                #print key
                #print self[key]
                #print self.derivative[key]
            self[key] += self.derivative[key]
            #if key == 'AMPA':
                #print self[key]
    def wrapUp(self):
        pass
    def trainingMode(self):
        pass
    def evaluationMode(self):
        pass
