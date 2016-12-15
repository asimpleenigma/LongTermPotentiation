# Monitor

from numpy import *

from datastructure import *
from biochem import *

from constituent import *
from neurongroup import *
from connection import * 

import copy

__all__ = ['Monitor']


class Monitor(Constituent):
    """ Records the value of a given state variable of a given constituent once every interval given. """
    def __init__(self, constituent, state_variable_names='All'):#, interval=1):
        name                        = "Monitor: "+ constituent.name
        Constituent.__init__(self, name)
        self.constituent            = constituent
        #self.interval               = interval
        if state_variable_names == 'All':
            state_variable_names   = set(constituent)&dynamic_variables
        self.state_variable_names   = set(state_variable_names)
        for var_name in self.state_variable_names:
            self[var_name]              = [] # meta list for variable
            self.derivative[var_name]   = []
            
        self.eval_avg             = Aspect('average: '+self.name)
        self.eval_change          = Aspect('change: '+self.name)
        
    def integrate(self):
        for var_name in self.state_variable_names:
            b               = copy.copy(self.constituent[var_name])
            self[var_name][-1][-1] += [b]
            
    def activate(self):
        for var_name in self.state_variable_names:
            b = copy.copy(self.constituent.derivative[var_name])
            self.derivative[var_name][-1][-1] += [b]
            
    def evaluate(self, pattern, n_timesteps):
        for var_name in self.state_variable_names:
            #print self
            self[var_name][-1]              += [[]] # meta list for pattern 
            self.derivative[var_name][-1]   += [[]]

    def cycle(self):
        for var_name in self.state_variable_names:
            #print 'hi'
            self[var_name]              += [[]] # meta list for training cycle 
            self.derivative[var_name]   += [[]]
            
    def wrapUp(self):
        for var_name in self.state_variable_names:
            self[var_name]              = array(self[var_name])
            self.derivative[var_name]   = array(self.derivative[var_name])
            self.eval_avg[var_name]     = self.patternAverage(var_name)
            self.eval_change[var_name]  = self.patternChange(var_name)
    # Monitor[variable][cycle][pattern][timestep] = array

            
    def patternAverage(self, variable_name):
        """ Average value of a variable while training each pattern. """
        return average(self[variable_name], axis=2)
        
            
    def patternChange(self, variable_name):
        """ Total change in a variable while training each pattern. """
        return sum(self.derivative[variable_name], axis=2)

        
