#交叉验证法
import numpy as np
def PCR (X,C,x,c):
    B=np.linalg.svd(X,full_matrices=False)
    Ta=B[0]*B[1]
    Pa=B[2].T
    T=Ta[:,:3]
    P=Pa[:,:3]
    Tt=T.T
    TtT=Tt.dot(T)
    inv=np.linalg.inv(TtT)
    temp=inv.dot(Tt)
    A=temp.dot(C)
    Alast=P.dot(A)
    err=(x.dot(Alast)-c)**2
    
    return err
S=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\S.txt")
S=S.T
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\C.txt")
C=np.transpose(C)
Err=np.zeros((6,3))


for i in range(0,S.shape[0]):
    x=S[i]
    c=C[i]
    X=np.delete(S,i,axis=0)
    Y=np.delete(C,i,axis=0)
    err=PCR(X,Y,x,c)
    Err[i]=err
print ("样本误差平方和")
print(Err)

sumErr=np.sum(Err,axis=0)
sumc=np.sum(c,axis=0)

Err=sumErr/sumc*100
print ("组分误差%")
print(Err)
x=np.arange(1,len(Err)+1)
import matplotlib.pyplot as plt 
plt.plot(x,sumErr)
plt.xlabel("sesu")
plt.ylabel("err%")
plt.show()
