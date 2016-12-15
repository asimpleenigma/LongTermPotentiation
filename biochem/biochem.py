# biochem

from numpy import *

from datastructure import *

from activationfunctions import *
from signaling import *
from conversion import *
from regulation import *

dynamic_variables = set(['Docked_Glu', 'Cleft_Glu', 'AMPA', 'Action_Potential', 'Vm'])

# low Decays
# high threshold, high Vm general


# AMPA
    # rates
L_x = .005    # max weight adjustment rate, LTP, learning rate
    
R_w = .00001    # Rate of Weight Decay



# Glu
    # rates
R_c = .3    # C_Glu reuptake rate

R_y = .5    # Glu release rate

R_d = .1    # D_Glu Repenish rate, how short STD is.

    # sensitivity
S_a = 2    # AMPA sensitivity to Glu
        
S_p = 2    # LTP sensitivity to Glu


         
# Vm
    # rates
E_a = .05    # membrane conductance of Vm / AMPA

R_h = .0025    # Vm Homeostasis rate

    # Voltages
    
V_h = -3    # hyperpol Vm, Vr_K

V_b = 21     # homeostasis baseline

V_t = 20    # Spike threshold Vm, VgNaC open

V_a = 30    # Vm baseline by AMPA, Vr_Na

V_k = 35    # Spike Vm, Vr_Na

    # sensitivity
S_v = .01    # LTP sensitivity to Vm



#print 'Vm base: \t' + str(Vm_base)
g_homeo = Regulation('Neuron_Homeostasis') # equalibriums and decays
g_homeo.addConversion('Vm',         rate = R_h, baseline = V_b)
g_homeo.addConversion('Docked_Glu', rate = R_d, baseline = 1 )
g_homeo.addConversion('Cleft_Glu',  rate = R_c, purpose = 'decay')
c_homeo = Regulation('Connection_Homeostasis')
c_homeo.addConversion('AMPA',       rate = R_w, purpose = 'decay')

AMPA = Regulation('AMPA')   # synaptic weight
AMPA.addSignaling('Cleft_Glu',  sensitivity = S_a,           purpose = 'propagation')
AMPA.addConversion('Vm',        rate = E_a,  baseline = V_a, purpose = 'transmission')

LTP = Regulation('LTP')     # adjust weight
LTP.addSignaling('Cleft_Glu',   sensitivity = S_p,           purpose = 'propagation')
LTP.addSignaling('Vm',          sensitivity = S_v,           purpose = 'backPropagation')
LTP.addConversion('AMPA',       rate = L_x,                  purpose = 'adjustment')


spike = Regulation('Spike')             # All or nothing
spike.addSignaling('Vm',                threshold   = V_t,   act_func = step) # Vm passes threshold
spike.addConversion('Action_Potential', baseline    = 1  )  # Activates Action Potential
spike.addConversion('Vm',               baseline    = V_k )  # Vm depolarizes
hypol = Regulation('Hyperpolarization') # Reset
hypol.addSignaling('Action_Potential',                      act_func = step)
hypol.addConversion('Vm',               baseline    = V_h )
hypol.addConversion('Action_Potential')
synapto =Regulation('Synaptotagmin')    # NT Release
synapto.addSignaling('Action_Potential',                    act_func = step)
synapto.addConversion('Docked_Glu',     rate = R_y,         purpose  = 'translation',
                                                            t_var_name = 'Cleft_Glu')

