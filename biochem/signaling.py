# Signaling
from numpy import *

from datastructure import *

from activationfunctions import *

__all__ = ['Signaling', 'signaling_category']

signaling_category = Category('Signaling')
class Signaling(Instance):
    """ Container for the relationships of an activator onto the associated regulator
        returns the portion of regulator that is activated by signal. """
    def __init__(self, signal_name, regulator_name, 
                 sensitivity = 1,   threshold = 0,  act_func = tanh,
                 purpose = 'processing',            mapping  = dict() ):
        name = str(signal_name)+" on "+str(regulator_name)
        Instance.__init__(self, name, mapping)

        self.signal_name    = signal_name
        self.regulator_name = regulator_name
        self.purpose        = purpose
        self.act_func       = act_func
        self.threshold      = threshold
        self.sensitivity    = sensitivity
        
        if purpose == 'processing':
            self.purpose = self.processing
        elif purpose == 'propagation':
            self.purpose = self.propagation
        elif purpose == 'backPropagation':
            self.purpose = self.backPropagation
        else:
            raise "Invalid signaling purpose."
        
    def __call__(self, constituent):
        return self.purpose(constituent)
        
    def analyzing(self, constituent): # signal is Boolian
        return constituent[signal_name]

    def processing(self, constituent): # signal and regulator are in same object
        result = self.act_func( self.sensitivity * (constituent[self.signal_name] - self.threshold) )
        return result

    def propagation(self, connection): # signal in pre neuron. regulator in connnection
        #             n_source  --> n_source * n_target
        #           singal      --> regulator
        #           pre neuron  --> Connection
        # e.g.    Celft_Glu     --> AMPA            # activation is n_source length array
        activation  = self.act_func( self.sensitivity * (connection.source[self.signal_name] - self.threshold) )
        result      = tile(activation, (connection.target.n_neurons, 1) ).transpose()
        return result
    
    def backPropagation(self, connection): # signal in post neuron, regulator in connnections
        # singal      --> regulator  
        # post neuron --> connection 
        # e.g. Vm     -->   NMDA            # activation is n_target length array
        activation  = self.act_func( self.sensitivity * (connection.target[self.signal_name] - self.threshold) )
        result      = tile(activation, (connection.source.n_neurons, 1) )
        #print self.name
        #print activation
        return result
