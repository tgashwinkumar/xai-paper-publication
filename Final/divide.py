import pandas as pd
import numpy as np

k_df = pd.read_csv('Final\\klfinal.csv')

t_df = pd.read_csv('Final\\tnfinal.csv')

m_df = pd.read_csv('Final\\mhfinal.csv')

def range_cle_k(val) :
    if val == 0 :
        return 0
    elif 1 <= val <= 40 :
        return 1
    elif 41 <= val <= 80 :
        return 2
    elif 81 <= val <= 120 :
        return 3
    elif 121 <= val <= 160 :
        return 4
    else :
        return 5

def range_h_k(val) :
    if val < 33 :
        return 0
    elif 33 <= val <= 45 :
        return 1
    elif 46 <= val <= 60 :
        return 2 
    elif 61 <= val <= 75 :
        return 3
    else :
        return 1

def range_cf_k(val) :
    if val == 0 :
        return 0
    elif 1 <= val <= 50000 :
        return 1
    elif 50001 <= val <= 100000 :
        return 2
    elif 100001 <= val <= 250000 :
        return 3
    elif 250001 <= val <= 500000 :
        return 4
    elif 500001 <= val <= 800000 :
        return 5
    else :
        return 6

def range_di_k(val) :
    if val == 0 :
        return 0
    elif 1 <= val <= 10 :
        return 1
    elif 11 <= val <= 25 :
        return 2
    elif 26 <= val <= 40 :
        return 3
    else :
        return 4

def range_ga_k(val) :
    if val == 0 :
        return 0
    elif 1 <= val <= 50 :    
        return 1
    elif 51 <= val <= 100 :
        return 2
    elif 101 <= val <= 200 :
        return 3
    else :
        return 4

def range_mt_k(val) :
    if val == 0 :
        return 0
    elif 1 <= val <= 50 :
        return 1
    elif 51 <= val <= 150 :
        return 2
    elif 151 <= val <= 251 :
        return 3
    else :
        return 4

def range_nc_k(val) :
    if val == 0 :
        return 0
    elif 1 <= val <= 500 :
        return 1
    elif 501 <= val <= 1500:
        return 2
    elif 1501 <= val <= 2500 :
        return 3
    elif 2501 <= val <= 5000 :
        return 4
    else :
        return 5

def range_tj_k(val) :
    if val == 0:
        return 0
    elif 1 <= val <= 50 :
        return 1
    elif 51 <= val <= 150 :
        return 2
    elif 151 <= val <= 200 :
        return 3
    else :
        return 4



def tn():
    tf_df = pd.DataFrame()

    for i in range(len(t_df)) :
        a = []
        a.append(t_df.iloc[i]['T'])
        a.append(range_h_k(t_df.iloc[i]['H']))
        a.append(range_cle_k(t_df.iloc[i]['CLE']))
        a.append(range_cf_k(t_df.iloc[i]['Confirmed']))
        a.append(range_di_k(t_df.iloc[i]['DI']))
        a.append(range_ga_k(t_df.iloc[i]['GA']))
        a.append(range_mt_k(t_df.iloc[i]['MT']))
        a.append(range_nc_k(t_df.iloc[i]['New Cases']))
        a.append(range_tj_k(t_df.iloc[i]['TJ']))
        a.append(t_df.iloc[i]['State'])
        a.append(t_df.iloc[i]['Date'])
        a.append(t_df.iloc[i]['ON'])
        a.append(t_df.iloc[i]['Rt'])
        tf_df = tf_df.append([a])
        # print(a)
    tf_df.rename(columns = {0 : 'T' , 1 : 'H' , 2 : 'CLE' , 3 : 'Confirmed' , 4 : 'DI' , 5 : 'GA'
     , 6 : 'MT' , 7 : 'New Cases' , 8 : 'TJ' , 9 : 'State' , 10 : 'Date' , 11 : 'ON' , 12 : 'Rt'}, inplace = True)
    return tf_df
tf_df = tn()
tf_df.to_csv('Final\\tnfinal1.csv' , index = False)
# print(set(tf_df['CLE']))