import numpy as np
#交叉验证的PCR函数
from PCA import PCA     #调用PCA文件  PCA.py

def PCR(X,C,x,c,k):  # X,C是训练集，x,c是被留下的一个样本，作为测试集合
#用train训练集XC建模，对test测试集xc预报
    pca=PCA(X)
    pca.SVDdecompose()
    T,P=pca.PCAdecompose(k)
    A=np.linalg.inv(T.T @ T) @ T.T @ C
    Alast=P.dot(A)
    err=(x.dot(Alast)-c)**2  #x.dot(Alast)即为Chat
    return err

S=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\S-Agilent.txt")
S=S.T
print("S=",S)

pca=PCA(S)       #用函数
print(pca.SVDdecompose())
k = int(input("组分数："))
T,P=pca.PCAdecompose(k)
C=np.loadtxt("D:\\学习\\barca\\化学信息学\\化学信息学\\混合色素案例\\C-Agilent.txt")
C=C.T
print("C=",C)
from sklearn.model_selection import KFold
Err=None
kf = KFold(n_splits=6) # 分10份交叉验证
for trainIndex, testIndex in kf.split(S): 
# 对X分割，每次循环得到的是训练集和测试集的矩阵
    X_train, x_test = S[trainIndex], S[testIndex]  # X的训练集与测试集
    Y_train, y_test = C[trainIndex], C[testIndex]   # Y的训练集与测试集
   # 用训练集建模，对测试集预报
    oneErr=PCR(X_train,Y_train,x_test,y_test,k)  # 一次交叉验证预报的误差
    if Err is None:   # 为完成矩阵堆叠，第一次直接用第一份的预测结果
        Err=oneErr
    else:
        Err=np.r_[Err,oneErr]    # 后续交叉验证  行堆叠
Err=np.sqrt(Err.sum(axis=0)/(C**2).sum(axis=0))*100
print("Err",Err)#   fenzi

A=(np.linalg.inv(T.T@T))@(T.T)@C
print("A=",A)
Alast=P@A
print("Alast=",Alast)
'''
Cunknown=T.T@(Alast.T)
Chat=Cunknown
'''
Chat=S@Alast
Chat=Chat.T
print("Chat=",Chat)
#计算相对误差
Chat=Chat.T
r=(Chat-C)/Chat*100
r=r.T
print("相对误差=",r,"%")


#计算RSE  residual standard error
fenmu=(C**2).sum(axis=0)      #axis=0按列加和  axis=1  按行加和
fenzi=((C-Chat)**2).sum(axis=0)
print("fenzi",fenzi)#   fenzi
print("Err=",Err)#   fenzi
answer=np.sqrt(fenzi/fenmu)*100
print("answer",answer)


#交叉验证    KFold
#LOO(Leave One Out)      留一法
'''问题：色素实验6个样本，是否可以用2份交叉验证实现？
可以  但误差太大  不可取
#
例子 
kf = KFold(n_splits=10) # 分10份交叉验证
for trainIndex, testIndex in kf.split(X): 
# 对X分割，每次循环得到的是训练集和测试集的矩阵
    X_train, X_test = X[trainIndex], X[testIndex]  # X的训练集与测试集
    y_train, y_test = y[trainIndex], y[testIndex]   # Y的训练集与测试集
   ……  # 用train训练集建模，对test测试集预报

'''



