# Regulation
from numpy import *

from datastructure import *

from activationfunctions import *

from signaling import *
from conversion import *

import copy

__all__ = ['Regulation', 'regulation_category']

regulation_category = Category('Regulation')
class Regulation(Instance):
    def __init__(self, regulator_name, mapping=dict()):
        Instance.__init__(self, regulator_name, mapping=mapping)
        self.conversions = set(self) & set(home['category']['Conversion'])
        self.signalings  = set(self) & set(home['category']['Signaling'])

    def __call__(self, constituent):
        """ returns a dictionary of the partial derivatives of constituent with respect to self """
        activated_regulator = copy.copy(constituent[self.name])
            
        for signaling_name in self.signalings:
            activated_regulator *= self[signaling_name](constituent)
            
        for conversion_name in self.conversions:
            self[conversion_name](constituent, activated_regulator)
            
    def addSignaling(self,          signal_name,     sensitivity = 2,
                     threshold = 0, act_func = tanh, purpose = 'processing'):
        signaling = Signaling(signal_name = signal_name,  regulator_name = self.name,
                              sensitivity = sensitivity,  threshold      = threshold,
                              purpose     = purpose,      act_func       = act_func)
        self[signaling.name] = signaling
        self.signalings     |= set([signaling.name])

    def addConversion(self,     s_var_name,        baseline = 0,
                      rate = 1, t_var_name = None, purpose  = 'equilibrium'):
        
        conversion = Conversion(regulation = self,    s_var_name = s_var_name,
                                rate       = rate,    t_var_name = t_var_name,
                                purpose    = purpose, baseline   = baseline)
        self[conversion.name] = conversion # add conversion to self.
        self.conversions |= set([conversion.name])
    
