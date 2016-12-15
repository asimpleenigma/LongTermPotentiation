from numpy import *

from datastructure import *
from biochem import *
from network import *

from attr_classification import *

# result[cycle][pattern][layer] = firing_rate
"""
This trains on these countries:
['Germany', 'Spain', 'Netherlands', 'Pakistan', 'Tanzania',
'New Zealand', 'Jamaica', 'Albania', 'Slovak Republic', 'India'

With these attributes:
['Gender Gap Index (2013)',
'Military Troops (Active) (per capita)',
'Internet Subscriptions (Mobile) (Per Capita) (2012)',
'Human Development Index (change per year) (2013) (by UN)',
'Military Troops (Para-)', 'population (1000s)']

printing net prints the average firing rate for each layer, for every pattern trained.
"""

net = RBM('net', z.data.shape[1], [4,6])
g0 = net['g0']
g1 = net['g1']
g2 = net['g2']
c0 = net['connection: g0 to g1']
c1 = net['connection: g1 to g0']

mg0 = net['Monitor: g0']
mg1 = net['Monitor: g1']
mg2 = net['Monitor: g2']
    
net.train(z.data[10:18],
        n_timesteps = 60,
        n_cycles = 4)
print net


