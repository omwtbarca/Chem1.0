#随机森林选择法--例子
import numpy as np
X=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\中草药\\wheat_train_PCA_X.txt")
y=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\中草药\\wheat_train_PCA_Y.txt")
avg=X.mean(axis=0)
std=X.std(axis=0)
X=(X-avg)/std
from RandomForestSelector import RandomForestSelector     #随机森林选择器
rf=RandomForestSelector(X,y,trees=20)

indices=rf.fit()
rf.plot()
indices=indices[:10] # 重要的变量=====选择前10个变量
print(' 重要的变量',indices)

# 随机森林选择法—PLS结果
X=X[:,indices]
from PLSDA import PLSDA
print('PLS结果')
pls=PLSDA(X,y,6,10,['w','y'])    #取6个主成分  10个交叉验证
# 6 个主成分，10份cv
cvErr=pls.fitcv()   #交叉验证  多少样本被错误判定
print(cvErr)
# 再 用所有样本建模，画得分图
pls.fit()
pls.plotScore()      
'''
PLS优于PCA结果
'''

from PCA import PCA
# 用重要变量进行PCA计算
print('PCA结果')
pca=PCA(X)  #该处 X=X[:,indices]  
ans=pca.SVDdecompose()
print(ans[1])
pca.plotScore(y)  
pca.plotScore(y,xAxis=1,yAxis=2,inOne=1)  
pca.plotScore(y,xAxis=0,yAxis=1,inOne=1)  
pca.plotScore(y,xAxis=0,yAxis=2,inOne=1)  