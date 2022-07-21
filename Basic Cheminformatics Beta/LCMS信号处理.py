#13信号处理   拉曼光谱
import numpy as np
def smooth(x,y,windowSize):  # 均线平滑
    m=windowSize  #一般奇数利于求中心    3 5 7
    result=[]
    pointsNum=len(y)-(m-1)  #少m-1个
    for k in range(pointsNum): 
        segment=y[k:m+k]
        onePoint=segment.sum()/m
        result.append(onePoint)
    ySmooth=np.array(result)
    # 根据峰位置对齐原则，应该前后各扔掉 (m-1)//2个点
    x=x[(m-1)//2:-(m-1)//2]
    return x,ySmooth
X1=np.loadtxt (r"D:\学习\barca\仪器分析实验\数据\LCMS\lc-ms-F\txt\195LC.txt")
x1=X1[:,0]
y1=X1[:,1]
X2=np.loadtxt (r"D:\学习\barca\仪器分析实验\数据\LCMS\lc-ms-F\txt\223LC.txt")
x2=X2[:,0]
y2=X2[:,1]
X3=np.loadtxt (r"D:\学习\barca\仪器分析实验\数据\LCMS\lc-ms-F\txt\279LC.txt")
x3=X3[:,0]
y3=X3[:,1]
x=np.arange(0,10,2)
y=y1+y2+y3


import matplotlib.pyplot as plt
fig=plt.figure(dpi=500)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure1-均线平滑")
plt.subplot(1, 2,  1)
plt.plot(x1,y,'g',label="before")
plt.xlabel("Time/min")
plt.ylabel("Intensity")
plt.legend()  


plt.subplot(1, 2,  2)
xhat,yhat=smooth(x1,y,15)
plt.plot(xhat,yhat,'r',label="after")
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
#plt.title("Figure1-均线平滑")
plt.savefig(r'D:\Desk\Figure5-all-Chromatogram平滑处理.png')#改名字和路径
plt.tight_layout()  
plt.xlabel("Time/min")
plt.ylabel("Intensity")
plt.legend()  
plt.show()
