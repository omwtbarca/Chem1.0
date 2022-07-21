#13信号处理   拉曼光谱   单图多样品
import numpy as np
from BaselineRemoval import BaselineRemoval
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
def polyFit(x,y,n=3,baseLine=0): # 默认3次方拟合
    X=np.ones(len(x))
    print(n,"次方拟合")
    for i in range(1,n+1):     
        X=np.c_[X,x**i]     
    temp=X @ np.linalg.inv(X.T @ X ) @ X.T
    y0=y
    count=0
    while True:
        yn=temp @ y0  # 迭代公式     迭代求解 原信号为初始值
        err=((y0-yn)**2).sum()/(yn**2).sum()
        if err <1e-6:
            break
        count +=1

        if count >60:
            break   #迭代次数最多60  
        for i in range(len(y0)):
            if yn[i] >y0[i]:
                yn[i]=y0[i]
        y0=yn     #不能比实测信号还大，不得为负值
    s=y-yn  # 原始信号  减基线
    s[s<baseLine]=baseLine  # 去基线后的信号
    return s
import matplotlib.pyplot as plt
plt.style.use("seaborn")
#制作针式搜索结果曲线
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
fig=plt.figure(figsize=(12,10),dpi=700)#创建全局绘图区
#frame = plt.gca()
# y 轴不可见
#frame.axes.get_yaxis().set_visible(False)
plt.yticks([])


X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\CH3OH.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat,'r',label="甲醇")
plt.xlabel("波数")
plt.ylabel("拉曼相对强度")

X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\beike.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
#xhat,yhat=smooth(x,y,19)
#yhat=polyFit(xhat,yhat)
#plt.plot(xhat,yhat,'r')
x,y=smooth(x,y,7)
baseObj = BaselineRemoval(y)
Y_Modpoly_output=baseObj.ModPoly()
plt.plot(x,Y_Modpoly_output+40000,'y',label="贝壳")


X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\benjiasuan.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+60000,'b',label="苯甲酸")


X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\boli.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
#xhat,yhat=smooth(x,y,19)
#yhat=polyFit(xhat,yhat)
#plt.plot(xhat,yhat,'r')
x,y=smooth(x,y,7)
baseObj = BaselineRemoval(y)
Y_Modpoly_output=baseObj.ModPoly()
plt.plot(x,Y_Modpoly_output+70000,'g',label="玻璃")

X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\CaSO4.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+80000,'c',label="硫酸钙")


X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\ccl4.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+110000,'m',label="四氯化碳")


X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\DCM.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+130000,'k',label="二氯甲烷")


X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\erjiajibiluo.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+185000,'r',label="二甲基吡咯")

X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\erlvyiwan.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+200000,'g',label="二氯乙烷")




X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\huoshanyan1-1.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+240000,'C0',label="火山岩样1")

X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\huoshanyan2-1.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+260000,'C1',label="火山岩样2")

X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\Li2CO3.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+273000,'C4',label="碳酸锂")

X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\manao.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+286000,'C5',label="玛瑙")

X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\PE.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+296000,'C6',label="石油醚")

X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\yisuanyizhi.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+309000,'C7',label="乙酸乙酯")

plt.title("Figure-各样品的拉曼谱图")


plt.legend()


plt.savefig(r"D:\学习\barca\仪器分析实验\数据\raman\raman的单图.png")

plt.show()


'''
plt.style.use("seaborn")
#制作针式搜索结果曲线
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
fig=plt.figure(figsize=(12,6),dpi=700)#创建全局绘图区
plt.subplot(2,3, 1)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\huoshanyan1-1.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat,'r')
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure10-火山岩样1")
plt.xlabel("波数")
plt.ylabel("强度")


plt.subplot(2,3, 2)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\huoshanyan2-1.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
#xhat,yhat=smooth(x,y,19)
#yhat=polyFit(xhat,yhat)
#plt.plot(xhat,yhat,'r')
x,y=smooth(x,y,7)
baseObj = BaselineRemoval(y)
Y_Modpoly_output=baseObj.ModPoly()
plt.plot(x,Y_Modpoly_output,'y')
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure11-火山岩样2")
plt.xlabel("波数")
plt.ylabel("强度")

plt.subplot(2,3, 3)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\Li2CO3.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat,'b')
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure12-碳酸锂")
plt.xlabel("波数")
plt.ylabel("强度")

plt.subplot(2,3, 4)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\manao.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
#xhat,yhat=smooth(x,y,19)
#yhat=polyFit(xhat,yhat)
#plt.plot(xhat,yhat,'r')
x,y=smooth(x,y,7)
baseObj = BaselineRemoval(y)
Y_Modpoly_output=baseObj.ModPoly()
plt.plot(x,Y_Modpoly_output,'g')
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure13-玛瑙")
plt.xlabel("波数")
plt.ylabel("强度")

plt.subplot(2,3, 5)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\PE.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat,'c')
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure14-石油醚")
plt.xlabel("波数")
plt.ylabel("强度")

plt.subplot(2,3, 6)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\yisuanyizhi.txt")
x=X[:,0]  #波数
y=X[:,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat,'m')
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure15-乙酸乙酯")
plt.xlabel("波数")
plt.ylabel("强度")

plt.legend()
plt.tight_layout()     # 调整子图间距

plt.savefig(r"D:\学习\barca\仪器分析实验\数据\raman\raman的图2.png")

plt.show()'''
