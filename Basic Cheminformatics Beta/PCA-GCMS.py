#  class        PCA类  放在程序目录下  
#2121-10-9
import numpy as np


S=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\S-Agilent.txt")
S=S.T
from PCA import PCA     #调用PCA文件  PCA.py
pca=PCA(S)       #用函数
compare=pca.SVDdecompose()
import matplotlib.pyplot as plt
plt.plot(np.arange(len(compare))+1,compare)

plt.show()

print(pca.SVDdecompose())
k = int(input("组分数："))
T,P,R=pca.PCAdecompose(k)
print(np.max(np.abs(R)))
colStd=R.std(axis=0)
print(colStd)












import numpy.random as npr
import matplotlib.pyplot as plt
x = np.arange(300,600,5)#光谱仪扫描范围300-600nm，分辨率5nm
A1 = np.exp(-((x-390)/(50))**2)  # 纯谱
n=len(A1)
sa1=0.1*A1+(npr.random(n)-0.5)*2/200      # 样本1   浓度 0.1
sa2=2.8*A1 +(npr.random(n)-0.5)*2/200    # 样本1   浓度 2.8
sa3=10.0*A1 +(npr.random(n)-0.5)*2/200   # 样本1   浓度 10.0
X = np.vstack([sa1,sa2,sa3])                          # 3个纯组分样本矩阵
U,s,V= np.linalg.svd(X,full_matrices=False)    # 求特征值s和特征向量v
plt.plot(A1/max(A1),'r-',label='pure')              # 画纯光谱，归一了
plt.plot(-V[0]/max(-V[0]),'go',label='eigenvector')    # 画特征向量 ,归一了
plt.legend()   
plt.show()
print("特征值为：",s*s)
