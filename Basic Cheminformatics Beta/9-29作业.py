
import numpy as np
#未归一
# 李同学
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1951894-C.txt")
S=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1951894-S.txt")
C=C.T
S=S.T
X=np.linalg.inv(C.T @ C) @ C.T @ S   # 纯光谱
wl= np.arange(380,570,10)
import matplotlib.pyplot as plt
plt.plot(wl,X[0],'r-')
plt.plot(wl,X[1],'g-')
plt.plot(wl,X[2],'b-')



Chat=S @ X.T @ np.linalg.inv(X@X.T)   

err=np.abs(C-Chat)/C *100
print(err)


#苏同学 

S=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1950964-S.txt")
S=S.T
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1950964-C.txt")
#C=np.c_[C[2],C[1],C[0]]
C=C.T

X1=np.linalg.inv(C.T @ C) @ C.T @ S   # 纯光谱
plt.plot(wl,X1[0],'r-')
plt.plot(wl,X1[1],'g-')
plt.plot(wl,X1[2],'b-')
plt.xlabel("波长/nm")
plt.ylabel("A")
plt.title("未归一的纯谱图")
plt.show()

Chat=S @ X1.T @ np.linalg.inv(X1@X1.T)   

err=np.abs(C-Chat)/C *100
print(err)


#归一后
# 李同学
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1951894-C.txt")
S=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1951894-S.txt")
C=C.T
S=S.T
X=np.linalg.inv(C.T @ C) @ C.T @ S   # 纯光谱
'''for i in range(len(X[0])):
  X0MAX=max(X[i])

print(X0MAX)
for i in range(len(X[1])):
  X1MAX=max(X[i])

print(X1MAX)
for i in range(len(X[2])):
  X2MAX=max(X[i])

print(X2MAX)'''
wl= np.arange(380,570,10)
import matplotlib.pyplot as plt
plt.plot(wl,X[0]/max(X[0]),'r-')
plt.plot(wl,X[1]/max(X[1]),'g-')
plt.plot(wl,X[2]/max(X[2]),'b-')

#苏同学 

S=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1950964-S.txt")
S=S.T
'''for i in range(len(S)):
  S2MAX=(max(S[i]))

print(S2MAX)'''
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1950964-C.txt")
C=C.T
#C=np.c_[C[2],C[1],C[0]]
X1=np.linalg.inv(C.T @ C) @ C.T @ S   # 纯光谱
plt.plot(wl,X1[0]/max(X1[0]),'r-')
plt.plot(wl,X1[1]/max(X1[1]),'g-')
plt.plot(wl,X1[2]/max(X1[2]),'b-')
plt.xlabel("波长/nm")
plt.ylabel("A")
plt.title("归一后的纯谱图")
plt.show()
'''
浓度单位不一致'''





