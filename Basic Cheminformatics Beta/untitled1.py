# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:23:17 2021

@author: Lenovo
"""

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
#PCA    如何预测
'''根据训练集空间
记住初始化时的均值和方差
对数据进行预处理的每列
将处理后的矩阵向原来的空间投影 T=XP
将T在原空间画散点图，判断其所属类别'''
'''把样本分割为训练集和测试集
使用train_test_split函数，使用方法如下'''
'''
from sklearn.model_selection import train_test_split
XTrain, XTest, yTrain, yTest = train_test_split(X, Y, test_size=.1) #抽出百分之十

test_size决定分割的尺寸
分割后 X 和Y 被分割成4个矩阵，train是训练，test是测试


X=XTrain
Y=yTrain
'''
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
'''k=input("输入主成分数:")
k=int(k)'''
T,P,R=pca.PCAdecompose(3)
#T,P=pca.SVDdecompose(3) 

#对T进行样本分离，分离没类样本到T1，T2， T3

#plt.scatter(T[:,0],T[:,1],color=(0.4,0.6,0.5),label='wucao')
cls1 = Y==0
cls2 = Y==1

T1=T[cls1]
T2=T[cls2]
'''
#分别第一、二主成分（第一和第二列），制作 T1、T2、T3的散点图，用不同颜色，不同形状
import matplotlib.pyplot as plt
plt.plot(T1[:,0],T1[:,1],'r+',label="T1")   #T1[:,1],T1[:,2]     !!!后面分不开  第零列最重要 
plt.plot(T2[:,0],T2[:,1],'g+',label="T2")
plt.plot(T3[:,0],T3[:,1],'b+',label="T3")
plt.title("PCA-鸢尾花(自标度化)",fontsize=20)
plt.xlabel("PC1",fontsize=14)
plt.ylabel("PC2",fontsize=14)
#fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.legend()




XTest=(XTest-aver)/std
Ttest=XTest @ P
T=Ttest
Y=yTest
cls1 = Y==0
cls2 = Y==1

T1=T[cls1]
T2=T[cls2]

#分别第一、二主成分（第一和第二列），制作 T1、T2、T3的散点图，用不同颜色，不同形状
import matplotlib.pyplot as plt
plt.plot(T1[:,0],T1[:,1],'r*',label="T1")   #T1[:,1],T1[:,2]     !!!后面分不开  第零列最重要 
plt.plot(T2[:,0],T2[:,1],'g*',label="T2")
plt.plot(T3[:,0],T3[:,1],'b*',label="T3")
plt.title("PCA-鸢尾花(自标度化)",fontsize=20)
plt.xlabel("PC1",fontsize=14)
plt.ylabel("PC2",fontsize=14)
#fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.legend()
plt.show()

'''


#   找关键变量

#变量与原点 线长 模长   影响大
'''思路：
设第1、2 主成分可以将类分开
获得载荷矩阵P
对P的每一行（两个数），将这两个数作为一个点的坐标p(x,y)
将点p和原点(0,0)，连线画出来。
matplotlib制图时，x坐标要放一起，y坐标放一起'''
import matplotlib.pyplot as plt
i=0
for row in P:
    x,y,z=row  #P是三维的  z凑数无效
    oneVariable=np.array([ [0,0] , [x,y]])
     # 构建坐标原点到P的一行(1、2主成分)组成的点
    plt.plot(oneVariable[:,0],oneVariable[:,1],label=str(i))
    plt.annotate(str(i), xy=(row[0], row[1]), xycoords='data', xytext=(+1, +1),#避免看不清重叠
             textcoords='offset points', fontsize=16)
     # annotate 在坐标图中写字，写的是字符串
    i = i+1
plt.show()


# 进行数据过滤
fil=[True,True,True,True,True,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,True,
     False,False,True,True]

#X=X[:,fil]
#或者直接切片
#sel=(P**2).sum(axis=1)


# 选变量 重新制作PCA投影图
sel=(P**2).sum(axis=1)  # 按行加和
index=np.argsort(sel) # 按值大小从小到大 把序号排序
index=index[-19:]      # 选取最大的19个变量的序号


X=X[:,index]        # 19个变量组成的子矩阵
pca=PCA(X)
pca.SVDdecompose()
T,P,R=pca.PCAdecompose(2)
plt.plot(T[cls1,0],T[cls1,1],'r+')
plt.plot(T[cls2,0],T[cls2,1],'g+')
plt.show()




