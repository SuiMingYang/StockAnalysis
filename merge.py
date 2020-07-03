import pandas as pd
import os
data=pd.read_csv('./data/name/namecode.csv')
result=pd.DataFrame()
re=0
for i,d in enumerate(zip(data['ts_code'],data['name'],data['industry'])):
    temp=pd.DataFrame()
    try:
        temp=pd.read_csv('./data/stock/'+d[0]+'_'+d[1]+'_'+d[2]+'.csv')
        if len(temp)!=0:
            temp['industry']=[d[2]]*len(temp)
            temp['name']=[d[1]]*len(temp)
            result=result.append(temp,sort=False)
            print(re)
        re+=len(temp)
    except Exception as e:
        print(e)
    if i%200==0:
        result.to_csv('data{}.csv'.format(i),index=None)
        result=pd.DataFrame()

result.to_csv('data4000.csv',index=None)

dt=pd.DataFrame()
for i in range(0,4200,200):
    data=pd.read_csv('data{}.csv'.format(str(i)))
    dt=dt.append(data,sort=False)
    os.remove('data{}.csv'.format(str(i)))


dt.to_csv('./data/alldata.csv',index=None)