#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   xgb.py
@Time    :   2020/07/03 18:38:51
@Author  :   sui mingyang 
@Version :   0.0.1
@Contact :   suimingyang123@gmail.com
@License :   (C)Copyright 2018-2019, weidian
@Desc    :   xgboost预测分析
'''

import pandas as pd
import numpy as np
import pickle
import math
data=pd.read_csv('./data/alldata.csv')

# 维度分析
## id,ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount,turnover_rate,turnover_rate_f,volume_ratio,pe,pe_ttm,pb,ps,ps_ttm,dv_ratio,dv_ttm,total_share,float_share,free_share,total_mv,circ_mv,created_at,updated_at,industry,name
from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder,OneHotEncoder
y=data['change'].astype('float')
encoder=LabelEncoder()#OneHotEncoder()
data['industry']=encoder.fit_transform(data['industry'])

data=data.drop(columns=['id','ts_code','trade_date','change','created_at','updated_at','name'])
xscaler = StandardScaler()
yscaler = MinMaxScaler()

data=xscaler.fit_transform(data)
y=yscaler.fit_transform(np.array(y).reshape(len(data),1))
pickle.dump(xscaler, open('./model/xscaler.pkl','wb'))
pickle.dump(yscaler, open('./model/yscaler.pkl','wb'))

data=pd.DataFrame(data=data,columns=['open','high','low','close','pre_close','pct_chg','vol','amount','turnover_rate','turnover_rate_f','volume_ratio','pe','pe_ttm','pb','ps','ps_ttm','dv_ratio','dv_ttm','total_share','float_share','free_share','total_mv','circ_mv','industry'])
data=data.fillna(0)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from xgboost import plot_importance

from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score

Xtrain, Xtest, Ytrain, Ytest = train_test_split(data,y,test_size=0.3)
model = xgb.XGBRegressor(max_depth=5, learning_rate=0.1, n_estimators=160, silent=False, objective='reg:gamma')
model.fit(Xtrain, Ytrain)

# 对测试集进行预测
ans = model.predict(Xtest)
evs=explained_variance_score(Ytest,ans)
print('explained_variance_score: ',evs)
mse=mean_squared_error(Ytest,ans)
print("mean_squared_error: ",mse)
mae=mean_absolute_error(Ytest,ans)
print("mean_absolute_error:",mae)
r2=r2_score(Ytest,ans)
print("r2_score:",r2)

model.save_model('./model/xgb.model')

# 调用
xscaler=pickle.load(open('xscaler.pkl', 'rb'))
yscaler=pickle.load(open('yscaler.pkl', 'rb'))
bst2 = xgb.Booster(model_file='./model/xgb.model')
pe = [[16.0,16.63,15.98,16.5,16.13,2.2939,1203100.0,1969890.0,0.62,1.3988,1.61,12.9018,11.4426,1.1942,2.7434000000000003,2.4073,0.7293000000000001,0.7776000000000001,1940591.875,1940575.25,860111.1875,32019766.0,32019492.0,120],[16.12,16.14,15.87,16.13,16.12,0.062,787952.0,1262800.0,0.406,0.9161,1.1,12.6125,11.186,1.1675,2.6819,2.3533,0.746,0.7954,1940591.875,1940575.25,860111.1875,31301746.0,31301480.0,3600]]
print('测试X',pe)
#pe=[[16.12,16.14,15.87,16.13,16.12,0.062,787952.0,1262800.0,0.406,0.9161,1.1,12.6125,11.186,1.1675,2.6819,2.3533,0.746,0.7954,1940591.875,1940575.25,860111.1875,31301746.0,31301480.0,3600]]
res = bst2.predict(xgb.DMatrix(np.array(xscaler.transform(pe))))
print(res)

print('测试Y',yscaler.inverse_transform(res.reshape(len(pe),1)))
