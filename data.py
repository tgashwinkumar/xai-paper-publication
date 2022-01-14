import pandas as pd

data = pd.read_csv('Data\\covid_19_india.csv')

data = data.set_index(['State/UnionTerritory']) #Column wise taken csv
tn_data = (data.loc['Tamil Nadu'])
tn_data.to_csv('Data\\Statewise\\tn-covid.csv')

kl_data = (data.loc['Kerala'])
kl_data.to_csv('Data\\Statewise\\kl-covid.csv')

mh_data = (data.loc['Maharashtra'])
mh_data.to_csv('Data\\Statewise\\mh-covid.csv')