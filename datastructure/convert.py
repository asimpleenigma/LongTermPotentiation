

from importcsv import *
from aspect import *
from dataset import *

data_structure = Aspect('Data Structure')

stat_files = ['Cultural and Ethnic Diversity Index (2003)',
              #'GDP (Nominal) (2012) (by CIA)',
              #'GDP (Nominal) (2012) (by IMF)',
              #'GDP (Nominal) (2012) (by UN)',
              #'GDP (Nominal) (Per Capita) (2013) (by CIA)',
              #'GDP (Nominal) (Per Capita) (2013) (by IMF)',
              #'GDP (Nominal) (Per Capita) (2013) (by WB)',
              'GDP (Nominal) (Per Capita) (2013) (by UN)',
              'GDP (Real) (Growth Rate) (2013)',
              'Gender Gap Index (2013)',
              'Global Militarization Index (2010)',
              'Global Peace Index (2013) (by IEP)',
              'Globalization Index (2013) (by KOF)',
              'Human Development Index (2013) (by UN)',
              'Human Development Index (Inequality Adjusted) (2012) (by UN)',
              'Median Age (2010) (by CIA)',
              #'Military Equipment',
              'Military Troops',
              'Mortality Rate (2011) (by OECD)',
              'Mortality Rate (2013) (by CIA)',
              #'Police Officers (UN)',
              'Quality of Life Index (2005) (by EIU)',
              'Broadband Internet Users (2012)',
              'Web Index (2013) (by WWWF)',
              'World Wealth Distribution']

for file_name in stat_files:
    home.assimilateData('Country Stats//'+file_name+'.csv')



x = home['Country']
us=x['United States']


def ke(di):
    k = dict.keys(di)
    #for key in k:
    #print key
    #print len(k)
    
a=list(set(us))[25:31]
z=DataSet(home['Country'], a)
#for row in z.data:
#   print row
#print z
#print a
#print z.data.shape

