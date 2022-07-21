import numpy as np
import matplotlib.pyplot as plt
from BaselineRemoval import BaselineRemoval
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\yisuanyizhi.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号

plt.plot(x,y,'r',label="原始")
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure2-贝壳")
plt.legend()
baseObj = BaselineRemoval(y)

Y_Modpoly_output=baseObj.ModPoly()
plt.plot(x,Y_Modpoly_output,'y',label="去基线后")
plt.legend()
plt.show()