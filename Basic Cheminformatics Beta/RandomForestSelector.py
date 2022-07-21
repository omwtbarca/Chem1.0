"""
@author: 丛培盛
"""
import numpy as np
from sklearn.ensemble import RandomForestClassifier #导入分类器
import matplotlib.pyplot as plt
class RandomForestSelector:
    def __init__(self,X,Y,trees=11):
        self.X=X
        self.Y=Y
        self.trees=trees
    def fit(self):
        dtree = RandomForestClassifier(self.trees,random_state=0)
        dtree.fit(self.X, self.Y) #建模
        self.importances = dtree.feature_importances_  #特征的重要性值
        self.indices = np.argsort(self.importances)[::-1]
        self.std = np.std([tree.feature_importances_ for tree in dtree.estimators_], axis=0)
        return self.indices
    def plot(self):
        plt.figure()
        plt.title("Feature importances")
        plt.bar(range(self.X.shape[1]), self.importances[self.indices],
           color="r", yerr=self.std[self.indices], align="center")
        plt.xticks(range(self.X.shape[1]), self.indices)
        plt.xlim([-1, self.X.shape[1]])
        plt.show()
