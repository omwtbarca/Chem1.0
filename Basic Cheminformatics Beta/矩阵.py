import numpy as np

Z=np.loadtxt("1874942711.txt")   #D:\\学习\\西班牙语\\题\\

print(Z)

'''
求矩阵的秩   equals to 独立信号源个数   组分数


c=np.array([[0.31,0.76],[4.41,3.46][50,53][0.36,6.18]])    #多个浓度
M=c@S
import matplotlib.pyplot as plt
plt.plot(x,M.T,'r')                      #'r/g/b'矩阵颜色？？？     
plt.show()
print(M)