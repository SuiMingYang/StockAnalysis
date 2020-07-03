import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn import metrics

data=pd.read_csv('./data/change.csv')
industry=data['industry']
name=data['name']
data=data.drop(columns=['industry','name'])


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
# # 1 数据可视化
# cluster1 = np.random.uniform(0, 1, (2, 100))
# cluster2 = np.random.uniform(2, 3, (2, 100))
# cluster3 = np.random.uniform(4, 5, (2, 100))
# X = np.hstack((cluster1, cluster2,cluster3)).T
# plt.figure()
# plt.axis([0, 5, 0, 5])
# plt.grid(True)
# plt.plot(X[:, 0], X[:, 1], 'k.')
# plt.show()
 
# 2 肘部法求最佳K值
K = range(1, 10,1)
mean_distortions = []
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    mean_distortions.append(
        sum(
            np.min(
                cdist(data, kmeans.cluster_centers_, metric='euclidean'), axis=1))
        / data.shape[0])
plt.plot(K, mean_distortions, 'bx-')
plt.xlabel('k')
plt.ylabel(u'平均畸变程度')
plt.title(u'用肘部法确定最佳的K值')
#plt.show()

# 降维
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
# pca = PCA(n_components=3)
# pca.fit(data)
# data=pca.transform(data)


# # 3 网格搜索
# kmeans = KMeans()
# param = {
#     'n_clusters':range(1,10,1)
#     }
# model = GridSearchCV(kmeans,param_grid = param, cv=5)
# model.fit(X)
# print(model.best_params_['n_clusters'])
# #sns.lineplot(x=range(2,11),y=score_list)


from sklearn.cluster import KMeans
y_pred = KMeans(n_clusters=7, random_state=9)
y=y_pred.fit_predict(data)

data['name']=name
data['industry']=industry
data['class']=[0]*len(name)

result=pd.DataFrame()
for i in range(0,7,1):
    res = data[(y_pred.labels_ ==i)]
    res['class']=[i]*len(res) 
    result=result.append(res,sort=False)
    print(i,len(res))

result.to_csv('./data/kmeans.csv',index=None)

# from sklearn.preprocessing import StandardScaler
# scaler=StandardScaler()
# data=scaler.fit_transform(data)
# fig = plt.figure()
# ax = Axes3D(fig)
# # ax = fig.add_subplot(111, projection='3d')
# plt.scatter(data[:,0], data[:, 1], data[:, 2],c=y)
# # plt.plot([-20,0,20],[-20,0,20],[-0.02,0,0.02])
# plt.show()




# plt.scatter(data[:,0], data[:,1], c=y_pred)
# plt.show()
