#过滤噪声

import numpy as np
x = np.arange(380,570,10)#光谱仪扫描范围300-600nm，分辨率5nm
S=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\S-Agilent.txt")
S=S.T
U,s,V=np.linalg.svd(S,)
ld=s**2
print('特征值=',ld)
n,m=S.shape   #波长 样本
print("RSD值依次为")
for i  in range(n-1,0,-1):
    temp=(ld[i:]**2).sum()/((n-i)*m)
    print("rsd%d=%8.3e"%(i,np.sqrt(temp)))
print("特征值比值为：")
print(ld[0:-1]/ld[1:])  #lamda3/lamda4处有突跃值！
k=int(input('请输入组分数：'))
T=U*s
T=T[:,0:k]
P=V.T
P=P[:,0:k]
R=S-T@P.T
import matplotlib.pyplot as plt
print('Digram S','\n')
plt.plot(x,S.T)
print('\n')
plt.show()
print('Digram R','\n')
plt.plot(x,R.T)
print('\n')
plt.show()
print("残差矩阵的最大绝对值为：")
print(np.max(np.abs(R)))