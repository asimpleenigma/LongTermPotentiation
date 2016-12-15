# Network

from numpy import *

from datastructure import *
from biochem import *

from constituent import *
from neurongroup import *
from connection import *
from monitor import *
from stimulator import *

__all__ = ['Network', 'network_category']

network_category = Category('Network')
class Network(Constituent):
    """ ``Network`` is a container class for NeuronGroups, Connections, and other Networks.
        Networks keep track of time, connected networks share clocks by default.
            Networks conduct training
    """
    def __init__(self, name):
        Constituent.__init__(self, name)
        
        self.clock = 0  # integer;          Network.clock            = number of timesteps simulated.
        self.neuron_groups = set()
        self.connections = set()
        self.monitors = set()
        self.simulators = set()
        
    def integrate(self):
        """``integrate`` finds derivitive of self. Can be based on anything except other object's derivatives. """
        for consitit_name in self:    # for each neuron group:
            self[consitit_name].integrate()    # find how future net values are affected from propagations this timestep.
        
    def activate(self):
        """``Network.activate`` activates each of the network's constituents, and advances the clock. """
        for consitit_name in self:    # for each neuron group:
            self[consitit_name].activate()    # find how future net values are affected from propagations this timestep.
                          # set net values for the next timestep.
        self.clock += 1                     # advance net's clock.
        
    def run(self, run_time):
        """``Network.run`` integrates each of the network's constituents, and then activates each constituent, run_time number of times. """
        for t in range(run_time):           # for each timestep:
            #print "Integrate:"
            self.integrate()                         # find net's state in the next timestep.
            #print ""
            
            #print "Activate:"
            self.activate()
            #print ""

    def evaluate(self, run_time):
        """``Network.run`` integrates each of the network's constituents, and then activates each constituent, run_time number of times. """
        self.evaluationMode()
        self.run(run_time)
        
    def train(self, pattern, run_time):
        """``Network.run`` integrates each of the network's constituents, and then activates each constituent, run_time number of times. """
        self.trainingMode()
        self.run(run_time)
    
    def addNeuronGroup(self, n_neurons):
        neuron_group_index = str(len(self.neuron_groups))
        neuron_group_name = 'g'+ neuron_group_index
        neuron_group = NeuronGroup(neuron_group_name, n_neurons=n_neurons)
        
        self[neuron_group_name] = neuron_group
        self.neuron_groups |= set([neuron_group_name])
        
    def addConnection(self, source, target):
        connection_name = 'connection: '+ source.name +' to '+ target.name
        connection = Connection(connection_name, source=source, target=target)
        
        self[connection_name] = connection
        self.connections |= set([connection_name])
        
    def addMonitor(self, constituent, state_variable_names):
        monitor = Monitor(constituent, state_variable_names)
        self[monitor.name] = monitor
        self.monitors |= set([monitor.name])

    def addStimulator(self, constituent, pattern=0, state_variable_name='Vm'):
        simulator = Stimulator(constituent, pattern, state_variable_name=state_variable_name)
        self[simulator.name] = simulator
        self.simulators |= set([simulator.name])
        
    def trainingMode(self):
        for constit_name in self:
            self[constit_name].trainingMode()
    def evaluationMode(self):
        for constit_name in self:
            self[constit_name].evaluationMode()
