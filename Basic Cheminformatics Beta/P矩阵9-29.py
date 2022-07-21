
#混合色素
import numpy as np

x = np.arange(300,600,5)#光谱仪扫描范围300-600nm，分辨率5nm
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\S-09927.txt")

C1=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\S.txt")
A=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1951894李鑫璇S.txt")
A1 = np.exp(-((x-390)/(10))**2)  # 纯谱
A2 = np.exp(-((x-500)/(10))**2)  # 纯谱
sa1=0.1*A1+1.2*A2      
sa2=2.8*A1 + 0.2*A2   
sa3=10.0*A1 + 3.0*A2   #这样的话秩为2         有意义的化学组分
X = np.vstack([sa1,sa2,sa3])   # 3个纯组分样本矩阵
U,s,V= np.linalg.svd(C,full_matrices=False) # 求特征值s和特征向量v
print(U.T@U)
print(V@V.T)

print(s*s)     #学长
U,s,V= np.linalg.svd(A,full_matrices=False) # 求特征值s和特征向量v


print(s*s)   #
U,s,V= np.linalg.svd(C1,full_matrices=False) # 求特征值s和特征向量v

#   de mio
print('lamda=',s*s) 
lamda=s*s
#size=V.shape      看维度 
#print (size[0])
UU=U[:,3:]
VV=V[3:]
ss=s[3:]
E=UU*ss@VV   #残差矩阵
res=np.sqrt((E**2).sum()/((6-3)*19))
print(res)

fenzi =lamda[0:-1]    #左闭右开
fenmu=lamda[1:]
ans=fenzi/fenmu         #奇异值分解
print(ans)
import matplotlib.pyplot as plt
plt.plot(ans,label='svd qiyizhifenjie') 
plt.legend()
plt.show()
'''
lamda=s*s.shape(1,6) plt.plot(A1/max(A1),'r-',label='pure')  #  归一化：  Xi/max(X)
plt.plot(A2/max(A1),'b-',label='pure')
plt.plot(-V[0]/max(-V[0]),'g^',label='eigenvector1')
plt.plot(V[1]/max(V[1]),'bv',label='eigenvector2')
plt.plot(V[2],'rv',label='eigenvector3')

'''

import numpy as np
x=np.arange(300,600,5)    #横坐标  波长  等差序列的实数采样 
A1 = np.exp(-((x-390)/(10))**2)
sa1=0.1*A1
sa2=2.8*A1
sa3=10.0*A1           # g^   用符号画出坐标曲线
X=np.vstack([sa1,sa2,sa3])
U,S,V=np.linalg.svd(X,full_matrices=False)
print(S*S)      
rank=np.linalg.matrix_rank(X)
print(X)
import matplotlib.pyplot as plt 
plt.plot(x,A1/max(A1),'r-',label='pure')
#plt.plot(x,A2/max(A1),'b-',label='pure')AA