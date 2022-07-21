"""
@author: 丛培盛
"""
import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt

class PLSDA:
    def __init__(self,X,Y,n_components,n_splits,pattern=None):
        self.X=X
        self.Y=Y
        self.n_components=n_components
        self.n_splits=n_splits
        self.pattern=pattern
    def fitcv(self):
        pls = PLSRegression(n_components=self.n_components,scale=False)
        kf = KFold(n_splits=self.n_splits)
        yTrue=None
        yHat=None
        # 判断Y 是几维的
        dimensiony=len(self.Y.shape)

        for train_index, test_index in kf.split(self.X):
            X_train, X_test = self.X[train_index], self.X[test_index]
            y_train, y_test = self.Y[train_index], self.Y[test_index]
            pls.fit(X_train, y_train)
            if dimensiony==1:
                ypred = pls.predict(X_test)[:,0]
            else:
                ypred = pls.predict(X_test)
            ypred[ypred>0]=1
            ypred[ypred<0]=-1
            if yTrue is None:
                yTrue=y_test  # 真值
                yHat=ypred  #预测值
            else:
        
                yTrue=np.r_[yTrue,y_test]
                yHat=np.r_[yHat, ypred]
        err=yTrue-yHat
        errSampleNo=np.where(err!=0)
        err=err[err!=0]
        
        return len(err)/len(self.X)*100,errSampleNo  #返回误判率
    def fit(self):
        self.pls = PLSRegression(n_components=self.n_components,scale=False)
        self.pls.fit(self.X,self.Y)
        
    def plotScore(self,xAxis=0,yAxis=1,inOne=False):
        
        T=self.pls.x_scores_
        if self.pattern==None:
            plt.plot(T[self.Y==1.0,xAxis],T[self.Y==1.0,yAxis],'r^')
            plt.plot(T[self.Y!=1.0,xAxis],T[self.Y!=1.0,yAxis],'g+')
        else:
            plt.plot(T[self.Y==1.0,xAxis],T[self.Y==1.0,yAxis],'r^',label=self.pattern[0])
            plt.plot(T[self.Y!=1.0,xAxis],T[self.Y!=1.0,yAxis],'g+',label=self.pattern[1])
            plt.legend(loc="upper left")
        plt.xlabel('PC'+str(xAxis))
        plt.ylabel('PC'+str(yAxis))
        W=self.pls.x_weights_
        if not inOne:
            plt.figure(2)
        maxScoreX=max(abs(T[:,xAxis]))
        maxScoreY=max(abs(T[:,yAxis]))
        maxLoadingX=max(abs(W[:,yAxis]))
        maxLoadingY=max(abs(W[:,yAxis]))
        # 画载荷的贡献图
        ratioInX= maxScoreX/maxLoadingX
        ratioInY=maxScoreY/maxLoadingY
        if (ratioInX>ratioInY):
            arfa=ratioInY
        else:
            arfa=ratioInX
        
        i=0
        for row in W:
            x=row[0]*arfa
            y=row[1]*arfa
            oneVariable=np.array([[0.0,0.0],[x,y]])
            plt.plot(oneVariable[:,0],oneVariable[:,1],label=str(i))
            plt.annotate(str(i), xy=(x, y), xycoords='data', xytext=(+1, +1),
                     textcoords='offset points', fontsize=16)
            i = i+1
        
        plt.show()
        
    def predict(self,Xnew): # 一列函数y，2类问题，+1和-1 
        ypred = self.pls.predict(Xnew)[:,0]
        ypred[ypred>0]=1
        ypred[ypred<0]=-1
        return ypred


        

