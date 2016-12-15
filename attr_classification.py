# Country Attr classification

from numpy import *

from datastructure import *


countries = set(home['Country'])
attributes = set()
for country_name in countries:
    for attr in home['Country'][country_name]:
        attributes |= set([attr])



data_sets = []
for attr in attributes: # Create a dataset for each attribute
    ds = DataSet(home['Country'], [attr], name=attr,
                 scalar_normalize=False, magnitude_normalize=False)
    data_sets += [ds]


scalars = set()
indexes = set()
for ds in data_sets:   # identify scalars and indecies
    t = ds.data.transpose()
    if 1.*amin(t)/amax(t) > 1./20:
        #ds.data = log(ds.data)
        scalars |= set([ds.name])
    else:
        indexes |= set([ds.name])
    #ds.data = 1.*ds.data/amax(ds.data) #scalar_normalize

economic        = ['GDP (Nominal) (Per Capita) (in US Dollars) (2013) (by UN)',
                   'GDP (Real) (Percent Growth) (2013)',
                   'Wealth per capita',
                   'GDP per capita',
                   'Wealth Gini',
                   'Wealth per adult',
                   'Share of world wealth (%)',
                   'Share of world GDP (%)']

military        = ['Military Troops (Total)',
                   'Military Troops (Active) (per capita)',
                   'Military Troops (Total) (per capita)',
                   'Military Troops (Para-)',
                   'Military Troops (Active)',
                   'Military Troops (Reserve)',
                   'Global Militarization Index (Normalized) (2010)']


demographic     = ['Median Age (Male) (by CIA)',
                   'Ethnic Fractionalization Index (2003)',
                   'adults (1000s)',
                   'Share of world population (%)',
                   'population (1000s)',
                   'Share of adult population (%)',
                   'Median Age (Female) (by CIA)',
                   'Median Age (by CIA)',
                   'Cultural Diversity Index (2003)',
                   'Gender Gap Index (2013)']

humanitarian    = ['Human Development Index (2013) (by UN)',
                   'Human Development Index (change per year) (2013) (by UN)',
                   'Quality of Life Index (Normalized) (2005) (by EIU)',
                   'Human Development Index (Inequality Adjusted) (2012) (by UN',
                   'Global Peace Index (2013) (by IEP)',
                   'Mortality Rate (per capita) (2011) (by OECD)',
                   'Human Development Index (percent change after accounting for Inequality) (2012) (by UN)',]

development     = ['Internet Subscriptions (Mobile) (2012)',
                   'Internet Subscriptions (Mobile) (Per Capita) (2012)',
                   'Globalization Index (2013) (by KOF)',
                   'Internet Subscriptions (Fixed) (Per Capita) (2012)',
                   'Web Index (2013) (by WWWF)',
                   'Internet Subscriptions (Fixed) (2012)']

society = [economic, military, demographic, humanitarian, development]
asp = ['economic', 'military', 'demographic', 'humanitarian', 'development']


society_aspects = []
for a in range(len(society)): # Create a dataset for each aspect
    society_aspects += [DataSet(home['Country'], society[a], name=asp[a])]
"""
for a in range(len(society)): # for every society_aspect
    for b in range(len(society)-a-1): # for every society_aspect after it
        print asp[a] + ' & ' + asp[a+b+1]
        print len(set(society_aspects[a].instance_names) &
                  set(society_aspects[a+b].instance_names))
        print ""

economic & military
67

economic & demographic
55

economic & humanitarian
54

economic & development
0

military & demographic
130

military & humanitarian
99

demographic & humanitarian
109
"""
    
