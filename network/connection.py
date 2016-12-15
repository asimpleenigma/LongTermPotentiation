#connection

from numpy import *

from datastructure import *
from biochem import *

from constituent import *
from neurongroup import *

__all__ = ['Connection']

class Connection(Constituent): # Connection proforms any calculation involving both a source and target.
    """ ``Connection`` represents the connections from every neuron in one neuron group to every neuron in another.
        Math equivilant: linear transformation.
    """
    def __init__(self, name, source, target):
        Constituent.__init__(self, name)
        # set attributes
        self.source           = source            # Source; Connection.source = pre-synaptic neuron group.
        self.target           = target            # Target; Connection.target = post-synaptic neuron group.
        self.n_axons          = source.n_neurons * \
                                target.n_neurons # integer; Connection.n_axons = number of dimensions of connection matrix
        self.reset()
        
    def reset(self):  
        self['Connection_Homeostasis']  = 1                  # regulator, static
        self['AMPA']                    = random.random((self.source.n_neurons,
                                                         self.target.n_neurons)) # Regulator, Dynamic
        self['Spine_Ca']        = random.random((self.source.n_neurons,
                                                 self.target.n_neurons))         # signal, dynamic
        self['LTP']             = 1      # Regulator, static
        Constituent.reset(self)
        
    def trainingMode(self):
        AMPA                    = self['AMPA'] # save weight
        self.reset()                # reset values
        self['LTP']             = 1      # Regulator, static
        self['AMPA']            = AMPA # load wieght

    def evaluationMode(self):
        self.reset()
        self['LTP']             = 0      # Regulator, static
        
