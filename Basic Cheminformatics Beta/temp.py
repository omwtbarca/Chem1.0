
#混合色素
import numpy as np
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\C.txt")
S=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\S.txt")
S=np.transpose(S)
M=np.dot(C,S)
import matplotlib.pyplot as plt 
wl=np.arange(380,560,10)    #横坐标  波长  等差序列的实数采样 
plt.plot(wl,M.T)  #不给横坐标默认其中的序号
plt.show()



'''

np.savetxt("D:\\学习\\barca\\化学信息学\\化学信息学\\画图M.txt",M,fmt='%5.3f')  #宽度为五   浮点数位数3
#VV型数据模拟
#荧光激光发射  色谱DAD分离   二极管   质谱（分子打成粒子碎片  测电荷和质量）
import numpy as py
t=np.arange(10,60,0.05)'''