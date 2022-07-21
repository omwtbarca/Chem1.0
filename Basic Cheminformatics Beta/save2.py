
#混合色素
import numpy as np
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1951894李鑫璇C.txt")
A=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1951894李鑫璇S.txt")
C=np.transpose(C)
A=A.T
X=np.linalg.inv(C.T@C)@C.T@A

print(X)
D=np.savetxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\K1951894李鑫璇.txt",X,fmt='%5.3f')
import matplotlib.pyplot as plt 
wl=np.arange(380,560,10)    #横坐标  波长  等差序列的实数采样 
plt.plot(X.T)  #不给横坐标默认其中的序号
plt.show()