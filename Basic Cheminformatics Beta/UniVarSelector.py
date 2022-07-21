"""
@author: pshcong
"""
from sklearn.feature_selection import SelectPercentile,f_classif
import numpy as np
import matplotlib.pyplot as plt

class UniVarSelector:
    def __init__(self,X,Y,percent=50):
        self.X=X
        self.Y=Y
        self.percent=percent
    def fit(self):
        selector= SelectPercentile(f_classif, self.percent)  # 选择50的变量
        selector.fit_transform(self.X, self.Y)
        self.pvalues=selector.pvalues_
        self.indx=np.argwhere(selector.get_support())[:,0]
        scores = -np.log10(self.pvalues)  #得到每个变量重要性p值的对数
        scores /= scores.max()
        self.scores=scores
        
        return self.pvalues,self.indx
    
    def plot(self):
        plt.figure()
        plt.title("Feature importances")
        X_indices = np.arange(self.X.shape[-1])
        indices = np.argsort(self.scores)[::-1]
        plt.bar(X_indices, self.scores[indices], width=.5,
                label=r'Univariate score ($-Log(p_{value})$)', color='0.5')
        plt.xticks(range(self.X.shape[1]), indices)
        plt.show()
    
