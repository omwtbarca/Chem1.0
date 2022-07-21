import numpy as np
class PCA:
    def __init__(self, X):
        self.X=X
    def SVDdecompose(self):
        B = np.linalg.svd(self.X,full_matrices=False)
        self.lamda=lamda=B[1]**2
        self.P = B[2].T
        self.T = B[0]*B[1]
        compare=[lamda[i]/lamda[i+1]   for i in range(len(lamda)-1)]
        cum=lamda.cumsum()/lamda.sum()*100
        return compare ,cum,self.lamda
    def PCAdecompose(self,k):  
# 给定主成分数k，得到去处噪声后的得分T和载荷P
        T = self.T[:,:k]
        P = self.P[:,:k]
        R=self.X-T @ P.T
        return T,P,R

