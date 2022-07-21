"""
@author: pshcong
"""
import numpy as np
import matplotlib.pyplot as plt
class PCA:
    def __init__(self, X):
        self.X=X
    def SVDdecompose(self):
        U,S,V = np.linalg.svd(self.X,full_matrices=False)
        self.lamda=lamda=S **2
        self.P = V.T
        self.T = U*S
        compare=[lamda[i]/lamda[i+1]   for i in range(len(lamda)-1)]
        cumsum=lamda.cumsum()
        fenmu=lamda.sum()
        cumsum=cumsum/fenmu*100
        return compare,cumsum
    def PCAdecompose(self,k):  
# 给定主成分数k，得到去处噪声后的得分T和载荷P
        T = self.T[:,:k]
        P = self.P[:,:k]
        return T,P
    def plotScore(self,types,xAxis=0,yAxis=1,inOne=False,syms=['r^','g+','b*','k-','md']):
        
        classIds=[]
        for i in types:
            if not i in classIds:
               classIds.append(i)
        
        for i,oneId in enumerate(classIds):
            plt.plot(self.T[types==oneId,xAxis],self.T[types==oneId,yAxis], syms[i],label='c'+str(i))

        plt.legend(loc="upper left")
        if not inOne:
            plt.figure(2)
        maxScoreX=max(abs(self.T[:,xAxis]))
        maxScoreY=max(abs(self.T[:,yAxis]))
        maxLoadingX=max(abs(self.P[:,yAxis]))
        maxLoadingY=max(abs(self.P[:,yAxis]))
        # 画载荷的贡献图
        ratioInX= maxScoreX/maxLoadingX
        ratioInY=maxScoreY/maxLoadingY
        if (ratioInX>ratioInY):
            arfa=ratioInY
        else:
            arfa=ratioInX
        
        i=0
        for row in self.P:
            x=row[0]*arfa
            y=row[1]*arfa
            oneVariable=np.array([[0.0,0.0],[x,y]])
            plt.plot(oneVariable[:,0],oneVariable[:,1],label=str(i))
            plt.annotate(str(i), xy=(x, y), xycoords='data', xytext=(+1, +1),
                     textcoords='offset points', fontsize=16)
            i = i+1
        
        
        plt.show()

       
        

