import pandas as pd

data = pd.read_csv('D:\\Studies\\xai-paper-publication\\Data\\covid_19_india.csv')

data = data.set_index(['State/UnionTerritory']) #Column wise taken csv
tn_data = (data.loc['Tamil Nadu'])
tn_data.to_csv('D:\\Studies\\xai-paper-publication\\Data\\Statewise\\tn-covid.csv')

kl_data = (data.loc['Kerala'])
kl_data.to_csv('D:\\Studies\\xai-paper-publication\\Data\\Statewise\\kl-covid.csv')

mh_data = (data.loc['Maharashtra'])
mh_data.to_csv('D:\\Studies\\xai-paper-publication\\Data\\Statewise\\mh-covid.csv')