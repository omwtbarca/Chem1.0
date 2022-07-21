#单变量选择法归纳—算法的进一步归纳
import numpy as np
from UniVarSelector import UniVarSelector  #ctrl 可打开源文件
#读数据
X=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\中草药\\wheat_train_PCA_X.txt")
y=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\中草药\\wheat_train_PCA_Y.txt")
# 预处理
avg=X.mean(axis=0);std=X.std(axis=0);X=(X-avg)/std       
#构造对象
univar=UniVarSelector(X,y,30)  # 选择30%的变量
#获取变量的P值和索引
pvalues,indx=univar.fit()   # 返回p值及选择的变量
#制作变量得分图
univar.plot()    
print('输出重要变量',indx)  # 输出重要变量
from PCA import PCA
# 用重要变量进行PCA计算
pca=PCA(X[:,indx])
ans=pca.SVDdecompose()
print(ans[1])
pca.plotScore(y)  
pca.plotScore(y,xAxis=1,yAxis=2,inOne=1)  
pca.plotScore(y,xAxis=0,yAxis=1,inOne=1)  
pca.plotScore(y,xAxis=0,yAxis=2,inOne=1)  