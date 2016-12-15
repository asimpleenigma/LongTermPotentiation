# neurongroup


from numpy import *

from datastructure import *
from biochem import *

from constituent import *
from neurongroup import *

__all__ = ['NeuronGroup']

class NeuronGroup(Constituent):
    """ ``NeuronGroup`` repreents cluster of neurons that share an activation function and synapse to the same neuron groups.
        Math equivilent: vector.
    """
    def __init__(self, name, n_neurons):
        Constituent.__init__(self, name)
        self.n_neurons      = n_neurons         # integer;  NeuronGroup.n                   = number of neurons in group.
        self.reset()
        
    def reset(self):
        self['Neuron_Homeostasis']  = True                  # regulator, static
        self['Vm']                  = random.random((self.n_neurons)) # signal, dynamic
        self['Spike']               = True               # regulator, static
        self['Action_Potential']    = random.random((self.n_neurons))#array([True]*self.n_neurons) # signal, regulator, dynamic
        self['Hyperpolarization']   = True               # regulator, static
        
        self['Synaptotagmin']       = True               # regulator, static
        self['Docked_Glu']          = random.random((self.n_neurons))# signal, dynamic
        self['Cleft_Glu']           = zeros((self.n_neurons))# signal, dynamic
        Constituent.reset(self)
