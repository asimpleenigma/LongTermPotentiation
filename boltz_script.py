# Restricted Boltzman Machine Script

from numpy import *

from datastructure import *
from biochem import *
from network import *


# create network

net = RBM('net', 2, [5,4])

# create data set of training patterns

s1 = array([[1,0]])
s2 = array([[0,1]])
s3 = array([[.5,1]])
s4 = array([[.5,.5]])
s5 = array([[.5,0]])
s6 = array([[.6,.4]])
s7 = array([[.4,.6]])
data_set = concatenate((s1, s2, s3, s4, s5, s6, s7),axis=0)

# add monitors to the network

g0 = net['g0']
net.addMonitor(g0, 'All')#['Vm', 'Action_Potential'])
mg0 = net['Monitor: g0']

g1 = net['g1']
net.addMonitor(g1, 'All')#['Vm', 'Action_Potential'])
mg1 = net['Monitor: g1']

c0 = net['connection: g0 to g1']
net.addMonitor(c0, 'All')#['AMPA'])
mc0 = net['Monitor: connection: g0 to g1']

c1 = net['connection: g1 to g0']
net.addMonitor(c1, 'All')#['AMPA'])
mc1 = net['Monitor: connection: g1 to g0']

g2 = net['g2']
net.addMonitor(g2, 'All')#['Vm', 'Action_Potential'])
mg2 = net['Monitor: g2']

c2 = net['connection: g1 to g2']
net.addMonitor(c2, 'All')#['AMPA'])
mc2 = net['Monitor: connection: g1 to g2']

c3 = net['connection: g2 to g1']
net.addMonitor(c3, 'All')#['AMPA'])
mc3 = net['Monitor: connection: g2 to g1']

# train network

net.train(data_set,
          n_timesteps = 2**8,
          n_cycles = 6)

# analyze network

fr0 = mg0.eval_avg['Action_Potential']
fr1 = mg1.eval_avg['Action_Potential']
fr2 = mg2.eval_avg['Action_Potential']

cg0 = mg0.eval_avg['Cleft_Glu']
cg1 = mg1.eval_avg['Cleft_Glu']

wc0 = mc0.eval_change['AMPA']
wc1 = mc1.eval_change['AMPA']


print net
