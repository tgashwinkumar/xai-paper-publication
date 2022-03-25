import pandas as pd
def range_k(val) :
    if val == 0 :
        return 0
    elif val <= 30 :
        return 1
    elif val <= 60 :
        return 2
    elif val <= 120 :
        return 3
    elif val <= 200 :
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
        return 4
    
def range_t_k(val) :
    if val <=15 :
        return 1
    elif val<=25:
        return 2
    else :
        return 3   



def range_nc_k(val) :
    if val ==0 :
        return 0
    elif val<= 500 :
        return 1
    elif 501 <= val <= 1500:
        return 2
    elif 1501 <= val <= 2500 :
        return 3
    elif 2501 <= val <= 5000 :
        return 4
    elif val>5000:
        return 5


def ranging(t_df):
    tf_df = pd.DataFrame()

    for i in range(len(t_df)) :
        a = []
        a.append(range_t_k(t_df.iloc[i]['T']))
        a.append(range_h_k(t_df.iloc[i]['H']))
        a.append(range_k(t_df.iloc[i]['SL']))
        a.append(t_df.iloc[i]['Confirmed'])
        a.append(range_k(t_df.iloc[i]['DI']))
        a.append(range_k(t_df.iloc[i]['GA']))
        a.append(range_k(t_df.iloc[i]['MT']))
        a.append(range_nc_k(t_df.iloc[i]['New Cases']))
        a.append(range_k(t_df.iloc[i]['TJ']))
        a.append(t_df.iloc[i]['State'])
        a.append(t_df.iloc[i]['Date'])
        a.append(t_df.iloc[i]['Rt'])
        tf_df = tf_df.append([a])
        
    tf_df.rename(columns = {0 : 'T' , 1 : 'H' , 2 : 'SL' , 3 : 'Confirmed' , 4 : 'DI' , 5 : 'GA'
     , 6 : 'MT' , 7 : 'New Cases' , 8 : 'TJ' , 9 : 'State' , 10 : 'Date', 11 : 'Rt'}, inplace = True)
    return tf_df
t_df = pd.read_csv('Final\\tnfinal.csv')
k_df = pd.read_csv('Final\\klfinal.csv')
m_df = pd.read_csv('Final\\mfinal.csv')
tf_df = ranging(t_df)
kf_df = ranging(k_df)
mf_df = ranging(m_df)
tf_df.to_csv('E:\\XAI\\datasets\\final\\tnfinal1.csv' , index = False)
kf_df.to_csv('E:\\XAI\\datasets\\final\\klfinal1.csv' , index = False)
mf_df.to_csv('E:\\XAI\\datasets\\final\\mhfinal1.csv' , index = False)
