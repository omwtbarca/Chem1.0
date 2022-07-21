

#混合色素
import numpy as np
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\C.txt")
A=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\S.txt")
Ct=np.transpose(C)
CCt=np.dot(C,Ct)
CCt1=np.linalg.inv(CCt)
ACt=A.dot(Ct)
K=np.dot(ACt,CCt1)
print("K矩阵为：")
print(K)
size=K.shape
print("K矩阵的行数和列数分别为：")
print(size[0],size[1])
print("C矩阵（实验值）为：")
print(C)
#D=np.savetxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\K.txt",K,fmt='%5.3f')
Kt=K.T
KtA=np.dot(Kt,A)
KtK=Kt.dot(K)
KtK1=np.linalg.inv(KtK)
Chat=KtK1.dot(KtA)
print("浓度矩阵（预测值）为")
print(Chat)
print("实验值与预测值偏差为")
err=abs((C-Chat)/C)
print(err)
import matplotlib.pyplot as plt 
wl=np.arange(380,560,10)    #横坐标  波长  等差序列的实数采样 
plt.plot(K)  #不给横坐标默认其中的序号
plt.show()