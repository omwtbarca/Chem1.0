#"D:\\学习\\barca\\化学信息学\\化学信息学\\中草药\\wheat_train_PCA_Y.txt")#读分类矩阵Y

import numpy as np   #  引入数值计算库
'''X=np.loadtxt( )   # 读文件
aver=X.mean(axis=0)   # 求每列的均值
std=X.std(axis=0)    # 求没列的标准差
Y=(X-aver)/std  '''   # Y 是X的转换，Y的每列均值为0，标准差为1
                  #接下去，后续的模式识别算法处理Y
#欧式距离   欧几里得距离  sqrt(x^2+y^2+z^2)   空间中到原点的距离
#    三个特征 三维空间确定三个特征  
#  无监督的模式识别方法  ——PCA 
# 多个特征无法想象    PCA降维

X=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\中草药\\wheat_train_PCA_X.txt")#读特征矩阵X
#X=X.T
print("X=",X)
Y=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\中草药\\wheat_train_PCA_Y.txt")#读分类矩阵Y
aver=X.mean(axis=0)
std=X.std(axis=0)
#自标度化
X1=(X-aver)/std
#对X作预处理，如 自标度化，处理后记录在X1中
#对X1作特征值分析
from PCA import PCA
pca = PCA(X1)
compare=pca.SVDdecompose() 
cum=pca.SVDdecompose()    #累计百分比
print(compare,cum)
#对X1作PCA分解，得到得分矩阵T
k=input("输入主成分数:")
k=int(k)
T,P,R=pca.PCAdecompose(k)
#T,P=pca.SVDdecompose(3) 

#对T进行样本分离，分离没类样本到T1，T2， T3

#plt.scatter(T[:,0],T[:,1],color=(0.4,0.6,0.5),label='wucao')
cls1 = Y==0
cls2 = Y==1
cls3 = Y==2
T1=T[cls1]
T2=T[cls2]
T3=T[cls3]
#分别第一、二主成分（第一和第二列），制作 T1、T2、T3的散点图，用不同颜色，不同形状
import matplotlib.pyplot as plt
plt.scatter(T1[:,0],T1[:,1],color=(0.8,0.8,0),s=10,label="T1")   #T1[:,1],T1[:,2]     !!!后面分不开  第零列最重要 
plt.scatter(T2[:,0],T2[:,1],color=(0,0.8,0.8),s=10,label="T2")
plt.scatter(T3[:,0],T3[:,1],color=(0.8,0,0.8),s=10,label="T3")
plt.title("PCA-wheat(自标度化)",fontsize=20)
plt.xlabel("PC1",fontsize=14)
plt.ylabel("PC2",fontsize=14)
#fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.legend()
plt.show()
print("\n")
plt.plot(T1[:,0],T1[:,1],'r+',label="T1")   #T1[:,1],T1[:,2]     !!!后面分不开  第零列最重要 
plt.plot(T2[:,0],T2[:,1],'go',label="T2")
plt.plot(T3[:,0],T3[:,1],'b*',label="T3")
plt.title("PCA-wheat(自标度化)",fontsize=20)
plt.xlabel("PC1",fontsize=14)
plt.ylabel("PC2",fontsize=14)
#fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.legend()
plt.show()

#中心化
X2=X-aver
from PCA import PCA
pca = PCA(X2)
compare=pca.SVDdecompose() 
cum=pca.SVDdecompose()    #累计百分比
print(compare,cum)
#对X1作PCA分解，得到得分矩阵T
'''k=input("输入主成分数:")
k=int(k)'''
T,P,R=pca.PCAdecompose(k)
#T,P=pca.SVDdecompose(3) 

#对T进行样本分离，分离没类样本到T1，T2， T3

#plt.scatter(T[:,0],T[:,1],color=(0.4,0.6,0.5),label='wucao')
cls1 = Y==0
cls2 = Y==1
cls3 = Y==2
T1=T[cls1]
T2=T[cls2]
T3=T[cls3]
#分别第一、二主成分（第一和第二列），制作 T1、T2、T3的散点图，用不同颜色，不同形状
import matplotlib.pyplot as plt
plt.scatter(T1[:,0],T1[:,1],color=(0.8,0.8,0),s=10,label="T1")   #T1[:,1],T1[:,2]     !!!后面分不开  第零列最重要 
plt.scatter(T2[:,0],T2[:,1],color=(0,0.8,0.8),s=10,label="T2")
plt.scatter(T3[:,0],T3[:,1],color=(0.8,0,0.8),s=10,label="T3")
plt.title("PCA-wheat(中心化)",fontsize=20)
plt.xlabel("PC1",fontsize=14)
plt.ylabel("PC2",fontsize=14)
#fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.legend()
plt.show()
print("\n")
plt.plot(T1[:,0],T1[:,1],'r+',label="T1")   #T1[:,1],T1[:,2]     !!!后面分不开  第零列最重要 
plt.plot(T2[:,0],T2[:,1],'go',label="T2")
plt.plot(T3[:,0],T3[:,1],'b*',label="T3")
plt.title("PCA-wheat(中心化)",fontsize=20)
plt.xlabel("PC1",fontsize=14)
plt.ylabel("PC2",fontsize=14)
#fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.legend()
plt.show()
#标准化-色谱面积归一化
X3=X.T
S=X3.sum(axis=0)
X3=X3/S
X3=X3.T
from PCA import PCA
pca = PCA(X3)
compare=pca.SVDdecompose() 
cum=pca.SVDdecompose()    #累计百分比
print(compare,cum)
#对X1作PCA分解，得到得分矩阵T
'''k=input("输入主成分数:")
k=int(k)'''
T,P,R=pca.PCAdecompose(k)
#T,P=pca.SVDdecompose(3) 

#对T进行样本分离，分离没类样本到T1，T2， T3

#plt.scatter(T[:,0],T[:,1],color=(0.4,0.6,0.5),label='wucao')
cls1 = Y==0
cls2 = Y==1
cls3 = Y==2
T1=T[cls1]
T2=T[cls2]
T3=T[cls3]
#分别第一、二主成分（第一和第二列），制作 T1、T2、T3的散点图，用不同颜色，不同形状
import matplotlib.pyplot as plt
plt.scatter(T1[:,0],T1[:,1],color=(0.8,0.8,0),s=10,label="T1")   #T1[:,1],T1[:,2]     !!!后面分不开  第零列最重要 
plt.scatter(T2[:,0],T2[:,1],color=(0,0.8,0.8),s=10,label="T2")
plt.scatter(T3[:,0],T3[:,1],color=(0.8,0,0.8),s=10,label="T3")
plt.title("PCA-wheat(标准化-色谱面积归一化)",fontsize=20)
plt.xlabel("PC1",fontsize=14)
plt.ylabel("PC2",fontsize=14)
#fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.legend()
plt.show()
print("\n")
plt.plot(T1[:,0],T1[:,1],'r+',label="T1")   #T1[:,1],T1[:,2]     !!!后面分不开  第零列最重要 
plt.plot(T2[:,0],T2[:,1],'go',label="T2")
plt.plot(T3[:,0],T3[:,1],'b*',label="T3")
plt.title("PCA-wheat(标准化-色谱面积归一化)",fontsize=20)
plt.xlabel("PC1",fontsize=14)
plt.ylabel("PC2",fontsize=14)
#fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.legend()
plt.show()
#标准化-质谱最大归一化
X4=X.T
ma=X4.max(axis=0)
X4=X4/ma
X4=X4.T
from PCA import PCA
pca = PCA(X4)
compare=pca.SVDdecompose() 
cum=pca.SVDdecompose()    #累计百分比
print(compare,cum)
#对X1作PCA分解，得到得分矩阵T
'''k=input("输入主成分数:")
k=int(k)'''
T,P,R=pca.PCAdecompose(k)
#T,P=pca.SVDdecompose(3) 

#对T进行样本分离，分离没类样本到T1，T2， T3

#plt.scatter(T[:,0],T[:,1],color=(0.4,0.6,0.5),label='wucao')
cls1 = Y==0
cls2 = Y==1
cls3 = Y==2
T1=T[cls1]
T2=T[cls2]
T3=T[cls3]
#分别第一、二主成分（第一和第二列），制作 T1、T2、T3的散点图，用不同颜色，不同形状
import matplotlib.pyplot as plt
plt.scatter(T1[:,0],T1[:,1],color=(0.8,0.8,0),s=10,label="T1")   #T1[:,1],T1[:,2]     !!!后面分不开  第零列最重要 
plt.scatter(T2[:,0],T2[:,1],color=(0,0.8,0.8),s=10,label="T2")
plt.scatter(T3[:,0],T3[:,1],color=(0.8,0,0.8),s=10,label="T3")
plt.title("PCA-wheat(标准化-质谱最大归一化)",fontsize=20)
plt.xlabel("PC1",fontsize=14)
plt.ylabel("PC2",fontsize=14)
#fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.legend()
plt.show()
print("\n")
plt.plot(T1[:,0],T1[:,1],'r+',label="T1")   #T1[:,1],T1[:,2]     !!!后面分不开  第零列最重要 
plt.plot(T2[:,0],T2[:,1],'go',label="T2")
plt.plot(T3[:,0],T3[:,1],'b*',label="T3")
plt.title("PCA-wheat(标准化-质谱最大归一化)",fontsize=20)
plt.xlabel("PC1",fontsize=14)
plt.ylabel("PC2",fontsize=14)
#fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.legend()
plt.show()
