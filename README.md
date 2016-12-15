# LongTermPotentiation
A detailed simulation of NMDA-mediated learning in glutamatergic neurons.

## LTP Overview
Long term potentiation (LTP) is a process by which the weight of a synapse is changed for a long period of time (longer than 1 hour). The CA3 to CA1 synapse in the hipocampus is the most studied synapse ever. The NMDA receptor acts as a coincidence detector, only activating when both the pre-neuron has released glutamate and the post-neuron is depolarized, resulting in associative learning. Second messagers signaled via NMDA trigger AMPA receptors to fuse into the post-synaptic density. Short-term depression also takes place in these synapses due to glutamate depletion. This program simulates this processes. 

## Simulation Specifications
The simulation is a dynamical system model with the following variables for each neuron:
* Membrane potential.
* Action potential.
And these for each synapse:
* Glutamate concentration in the synaptic cleft.
* Glutamate docked in the presynaptic density.
* AMPA concentration in the postsynaptic density.

The derivatives of these variables are determined by parameters such as glutamate reuptake rate and NMDA sensitivity to membrane potential.  A full list of the 15 parameters can be found in the file biochem.py.

The greatest limitation of the program currently is that the length of the action potential cannot be specified.

## Learning in the Network
In an attempt to relate associative biological learning and associative machine learning, I built a Deep Belief Network (DBN)-type architecture for this network. I thought it would be interesting to apply math to social science, so I compiled dozens of statistics and indexes on nation-states for training data. I made a database in python to hold this data, as well as the relationships between the various parameters. Surely it could have been done more efficiently if I knew more SQL. It turned out that this simulation has way too much going on to have a reasonable runtime for doing machine learning, on my computer anyways.
