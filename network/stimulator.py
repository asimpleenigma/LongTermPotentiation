# Stimulator

from numpy import *

from datastructure import *
from biochem import *

from constituent import *

__all__ = ['Stimulator']

class Stimulator(Constituent):
    """ Takes a pattern, constituent, and state variable.
        Adds the pattern values to the constituent's state variable each timestep."""
    def __init__(self, constituent, pattern=0, state_variable_name='Vm'):
        name = 'Stim: '+constituent.name
        Constituent.__init__(self, name)
        self.pattern                = pattern
        self.constituent            = constituent
        self.state_variable_name    = state_variable_name

    def integrate(self):
        self.constituent.derivative[self.state_variable_name] += self.pattern

    def activate(self):
        pass
