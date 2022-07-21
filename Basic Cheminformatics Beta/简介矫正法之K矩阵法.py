

#混合色素
import numpy as np
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\C.txt")
A=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\S.txt")
Ct=np.transpose(C)
CCt=np.dot(C,Ct)
CCt1=np.linalg.inv(CCt)
ACt=A.dot(Ct)
K=np.dot(ACt,CCt1)
print(K)
D=np.savetxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\K.txt",K,fmt='%5.3f')
import matplotlib.pyplot as plt 
wl=np.arange(380,560,10)    #横坐标  波长  等差序列的实数采样 
plt.plot(wl,K)  #不给横坐标默认其中的序号
plt.show()