import numpy as np
S=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1951894李鑫璇S.txt")
S=S.T
print("S=",S)
from PCA import PCA
pca = PCA(S)
compare=pca.SVDdecompose()
k=input("输入主成分数:")
k=int(k)
T,P,R=pca.PCAdecompose(k)
print(np.max(np.abs(R))) ;colStd=R.std(axis=0)
print(colStd)
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\1951894李鑫璇C.txt")
C=C.T
print("C=",C)
#建立浓度与得分T的回归C=TA
Tt=T.T
TtT=Tt @ T
inv=np.linalg.inv(TtT)
temp=inv @ Tt
A=temp @ C
Alast=P @ A
S2=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\S2-Agilent.txt")
S2=S2.T
Chat=S2@ Alast   
print("Chat=",Chat)
#计算相对误差
#Chat=Chat.T
r=(Chat-C)/Chat
r=r.T
print("相对误差=",r)


#计算RSE  residual standard error
fenmu=(C**2).sum(axis=0)      #axis=0按列加和  axis=1  按行加和
fenzi=((C-Chat)**2).sum(axis=0)
print("fenzi",fenzi)#   fenzi
#print("Err=",Err)#   fenzi
answer=np.sqrt(fenzi/fenmu)*100
print("answer",answer,"%")