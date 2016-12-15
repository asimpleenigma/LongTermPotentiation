# Restricted Bolzman Machine

from numpy import *

from datastructure import *
from biochem import *

from constituent import *
from neurongroup import *
from connection import *
from monitor import *
from stimulator import *
from network import *

__all__ = ['RBM']

class RBM(Network):
    def __init__(self, name, n_inputs, n_hiddens=[]):
        Network.__init__(self, name)
        self.result = "zip"
        self.n_hiddens = n_hiddens
        self.addNeuronGroup(n_inputs)
        self.addMonitor(self['g0'], ['Action_Potential'])
        self.addStimulator(self['g0'])
        for n in range(len(n_hiddens)):
            self.addNeuronGroup(n_hiddens[n])
            self.addConnection(self['g'+str(n)], self['g'+str(n+1)])
            self.addConnection(self['g'+str(n+1)], self['g'+str(n)])
            self.addMonitor(self['g'+str(n+1)], ['Action_Potential'])
            #self.addMonitor(self['connection: g'+str(n)+' to g'+str(n+1)], 'All')
            #self.addMonitor(self['connection: g'+str(n+1)+' to g'+str(n)], 'All')

        #output = net['g0']
        #net.addMonitor(g0, set(g0)&dynamic_variables)
        #mg0 = net['Monitor: g0']

    def __str__(self):
        string = "\n"+self.name
        mg0 = self['Monitor: g0'].eval_avg['Action_Potential']
        dims = mg0.shape
        
        for cycle in range(dims[0]):
            string += "\nCycle "+str(cycle)
            for pattern in range(dims[1]):
                string += "\nPattern "+str(pattern)
                for layer in range(len(self.n_hiddens)+1):
                    APn = self['Monitor: g'+str(layer)].eval_avg['Action_Potential']
                    string += '\n'+ APn[cycle][pattern].__str__()
            string += '\n'
        return string
    
    def evaluate(self, pattern, n_timesteps):
        for monitor in self.monitors:
            self[monitor].evaluate(pattern, n_timesteps)
        self['Stim: g0'].pattern = pattern
        self.run(n_timesteps)

    def wrapUp(self):
        result = []
        mg0 = self['Monitor: g0'].eval_avg['Action_Potential']
        dims = mg0.shape
        
        for cycle in range(dims[0]):
            result += [[]] # Add Cycle list of patterns
            for pattern in range(dims[1]):
                result[cycle] += [[]] # Add Pattern list of layers
                for layer in range(len(self.n_hiddens)+1):
                    APn = self['Monitor: g'+str(layer)].eval_avg['Action_Potential']
                    result[cycle][pattern] += [APn[cycle][pattern]] # Add layer array of firing rates
        self.result = result

    def train(self, data_set, n_timesteps, n_cycles):
        for cy in range(n_cycles):
            for monitor in self.monitors:
                self[monitor].cycle()
            for pattern in data_set:
                self.evaluate(pattern, n_timesteps)
        for constit_name in self:
            self[constit_name].wrapUp()
        self.wrapUp()
        
    
