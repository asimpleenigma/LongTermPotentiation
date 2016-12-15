# Conversion

from numpy import *

from datastructure import *

from activationfunctions import *
from signaling import *

__all__ = ['Conversion', 'conversion_category']

conversion_category = Category('Conversion')
class Conversion(Instance):
    """ Function object that returns the number of units of source that a unit of active regulators will convert to units of target.
            The target concentration is assumed to not affect the rate.
        Container for the relationships of the associated regulator onto an converted value. """
    
    def __init__(self,  regulation, s_var_name, baseline = 0,
                 rate = 1, t_var_name = None, purpose = 'equilibrium', mapping = dict() ):
        converion_name = s_var_name+' conversion by '+regulation.name
        Instance.__init__(self, converion_name, mapping)
        
        self.purpose    = purpose
        self.regulation = regulation
        self.baseline   = baseline
        self.rate       = rate
        self.s_var_name = s_var_name
        self.t_var_name = t_var_name
        
        if purpose == 'equilibrium':
            self.purpose = self.equilibrium
        elif purpose == 'decay':
            self.purpose = self.decay
        elif purpose == 'translation':
            self.purpose = self.translation
        elif purpose == 'transmission':
            self.purpose = self.transmission
        elif purpose == 'adjustment':
            self.purpose = self.adjustment
        else:
            raise "Invalid purpose"

    def __call__(self, constit, activated_regulator):
        self.purpose(constit, activated_regulator)

    def adjustment(self, connection, activated_LTP):
        amount_adjusted = self.rate * activated_LTP
        connection.derivative[self.s_var_name] += amount_adjusted
        
    def gradient(self, constit):
        current_value = constit[self.s_var_name]
        gradient      = self.baseline - current_value
        return gradient
    
    def equilibrium(self, constit, activated_regulator):
        """ Value exponentially approaches baseline. """
        amount_restorated = activated_regulator * self.rate * self.gradient(constit)
        constit.derivative[self.s_var_name] += amount_restorated
        
    def decay(self, constit, activated_regulator):
        current_value = constit[self.s_var_name]
        amount_decayed = activated_regulator * self.rate * current_value
        constit.derivative[self.s_var_name] -= amount_decayed
        
    def translation(self, constit, activated_regulator):
        """ Source value exponentially approaches baseline. That change is subtracted form the target value """
        #print self.name
            
        amount_translated   = activated_regulator * self.rate * self.gradient(constit)
        constit.derivative[self.s_var_name] += amount_translated
        constit.derivative[self.t_var_name] -= amount_translated
        
    def transmission(self, connection, activated_regulator):
        """ n_source * n_target --> n_target
                     regulator  --> convertee
                     connection --> post neuron
                   e.g.  AMPA   -->     Vm """
        amount_transmitted  = activated_regulator * self.rate * self.gradient(connection.target)
        result              = sum(amount_transmitted, axis=0) # sum over source
        connection.target.derivative[self.s_var_name] += result
        
