#LCMS
# 色谱图-质谱图
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
fig=plt.figure(figsize=(8,10),dpi=500)#创建全局绘图区
fig.text(1,0.15,'Plot Descriptor: 195.0>50.0:200.0 [-30.0V]',
             fontsize=4,color='b',ha='right',va='top',alpha=0.4,rotation=0)


plt.subplot( 2, 2, 2)
X1=np.loadtxt (r"D:\学习\barca\仪器分析实验\数据\LCMS\lc-ms-F\txt\195LC.txt")
x1=X1[:,0]
y1=X1[:,1]
plt.plot(x1,y1,'r')
plt.title("图6-母离子195m/z结果色谱图")

plt.xlabel("Time/min")
plt.ylabel("Intensity")



plt.subplot(2, 2,  3)

X2=np.loadtxt (r"D:\学习\barca\仪器分析实验\数据\LCMS\lc-ms-F\txt\223LC.txt")
x2=X2[:,0]
y2=X2[:,1]
plt.plot(x2,y2,'g')
plt.title("图7-母离子223m/z结果色谱图")
plt.xlabel("Time/min")
plt.ylabel("Intensity")




plt.subplot( 2, 2,4)
X3=np.loadtxt (r"D:\学习\barca\仪器分析实验\数据\LCMS\lc-ms-F\txt\279LC.txt")
x3=X3[:,0]
y3=X3[:,1]
plt.plot(x3,y3,'b')
plt.title("图8-母离子279m/z结果色谱图")
plt.xlabel("Time/min")
plt.ylabel("Intensity")


plt.subplot( 2, 2, 1)
x4=np.arange(0,10,2)
y4=y1+y2+y3
plt.plot(x1,y4,'black',label="195")
'''
plt.plot(x1,y1,'r',label="195")
plt.plot(x2,y2,'g',label="223")
plt.plot(x3,y3,'b',label="279")
'''
plt.title("图5-Product Scan结果色谱图")
plt.xlabel("Time/min")
plt.ylabel("Intensity")

plt.savefig(r'D:\Desk\Figure5-all-Chromatogram.png')#改名字和路径
plt.tight_layout()   
plt.legend()  
plt.show()






'''
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
#平滑后效果图
fig=plt.figure(figsize=(8,10),dpi=500)#创建全局绘图区
plt.subplot( 3, 2, 1)
fig.text(1,0.15,'Plot Descriptor: 195.0>50.0:200.0 [-30.0V]',
             fontsize=4,color='b',ha='right',va='bottom',alpha=0.4,rotation=0)

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

import matplotlib.pyplot as plt

#plt.plot(x,y,'g',label="before")
xhat,yhat=smooth(x,y,7)
plt.plot(xhat,yhat,'r',label="after")
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure1-均线平滑")
plt.legend()
plt.show()


'''



