#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   group.py
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
res=data.groupby(['industry','name'])

industry=[]
start=[]
end=[]
name=[]
change=[]
max_change=[]
min_change=[]
up=[]
down=[]
turn=[]
amount=[]

for i,r in res:
    industry.append(i[0])
    name.append(i[1])
    change.append('%3f' % np.sum(r['change']))
    max_change.append(np.max(r['change']))
    min_change.append(np.min(r['change']))
    start.append(np.max(r['open']))
    end.append(np.max(r['close']))
    up.append(len(r[r['change']>=0]))
    down.append(len(r[r['change']<0]))
    turn.append(np.mean(r['turnover_rate']))
    amount.append(np.mean(r['amount']))
        
result=pd.DataFrame({
    'industry':industry,
    'name':name,
    'max_change':max_change,
    'min_change':min_change,
    'start':start,
    'end':end,
    'amount':amount,
    'turn':turn,
    'change':change,
    'up_count':up,
    'down_count':down
})
result['change']=result['change'].astype('float')
result.sort_values(by='change',ascending=False,inplace=True)

result.to_csv('./data/change.csv',index=None)
