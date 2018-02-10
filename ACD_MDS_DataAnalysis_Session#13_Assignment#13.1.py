# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:39:06 2018

@author: HP
"""

import numpy as np
import pandas as pd
import re

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

#1 - Some values in the the FlightNumber column are missing.
fn = np.linspace(10045, 10095, 5, endpoint=False, dtype=np.int)
df['FlightNumber'] = fn

#2- The From_To column would be better as two separate columns
ft = df['From_To']
df['From'] = ft.str.split('_').str.get(0)
df['To'] = ft.str.split('_').str.get(1)
tdf = df.drop('From_To', axis=1)

#3 - Standardise city names so that only the first letter is uppercase
fr = tdf['From']
tdf['From'] = fr.str.title()
to = tdf['To']
tdf['To'] = to.str.title()
air = str(tdf['Airline'])

# Clean Airline Field
tdf['Airline_Clean'] = tdf['Airline'].apply(lambda x: re.sub(r'\W|\d', "", x))
tdf = tdf.drop('Airline', axis=1)

#5 RecentDelays column, split the values in the column to separate columns
mdf = pd.concat([tdf['Airline_Clean'],tdf['FlightNumber'],tdf['From'],tdf['To'],pd.DataFrame(tdf['RecentDelays'].values.tolist())], axis=1)

# compose dataframe with required columns
mdf.columns = ['Airline','FlightNumber','From','To','Delay_1','Delay_2','Delay_3']
print(mdf)