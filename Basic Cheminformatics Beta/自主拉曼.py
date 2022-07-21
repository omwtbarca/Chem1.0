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
fig=plt.figure(figsize=(12,6),dpi=700)#创建全局绘图区
#frame = plt.gca()
# y 轴不可见
#frame.axes.get_yaxis().set_visible(False)
plt.yticks([])


X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\1.txt")
x=X[:-100,0]  #波数
y=X[:-100,1]  #信号

xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)

plt.plot(xhat,yhat,'r',label="样品A第一次")
from scipy.signal import find_peaks
peak_id,peak_property = find_peaks(yhat, height=430, distance=150)     #更改高度强度间距 
peak_freq = xhat[peak_id]
peak_height = peak_property['peak_heights']
print('peak_freq',peak_freq)
print('peak_height',peak_height)
plt.bar(peak_freq,peak_height)
for peak_freq,peak_height  in zip(peak_freq,peak_height):
         plt.text(peak_freq,peak_height+4800,str(peak_freq) ,ha='center',va='bottom',color="red")

plt.xlabel("波数")
plt.ylabel("拉曼相对强度")

X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\2.txt")
x=X[:-100,0]  #波数
y=X[:-100,1]  #信号
#xhat,yhat=smooth(x,y,19)
#yhat=polyFit(xhat,yhat)
#plt.plot(xhat,yhat,'r')
x,y=smooth(x,y,7)
baseObj = BaselineRemoval(y)
Y_Modpoly_output=baseObj.ModPoly()
plt.plot(x,Y_Modpoly_output+1700,'y',label="样品A第二次")
from scipy.signal import find_peaks
peak_id,peak_property = find_peaks(Y_Modpoly_output, height=900, distance=400)     #更改高度强度间距 
peak_freq = x[peak_id]
peak_height = peak_property['peak_heights']
print('peak_freq',peak_freq)
print('peak_height',peak_height)
plt.bar(peak_freq,peak_height)
for peak_freq,peak_height  in zip(peak_freq,peak_height):
         plt.text(peak_freq,peak_height+3000,str(peak_freq) ,ha='center',va='bottom',color="red")



X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\3.txt")
x=X[:-100,0]  #波数
y=X[:-100,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(xhat,yhat+5000,'b',label="样品B第一次")



plt.title("火山岩拉曼谱图")


plt.legend()


#plt.savefig(r"D:\学习\barca\仪器分析实验\数据\raman\raman的单图.png")

plt.show()


plt.style.use("seaborn")
#制作针式搜索结果曲线
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
fig=plt.figure(figsize=(12,4),dpi=700)#创建全局绘图区
plt.subplot(1,3, 1)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\1.txt")
x=X[:-10,0]  #波数
y=X[:-10,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
K=[xhat,yhat]
k=np.savetxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\xy1.txt",K)
plt.plot(xhat,yhat,'r')
'''

from scipy.signal import find_peaks
peak_id,peak_property = find_peaks(y, height=6000, distance=1000)     #更改高度强度间距 
peak_freq = x[peak_id]
peak_height = peak_property['peak_heights']
print('peak_freq',peak_freq)
print('peak_height',peak_height)
plt.bar(peak_freq,peak_height)
for peak_freq,peak_height  in zip(peak_freq,peak_height):
         plt.text(peak_freq,peak_height+300,str(peak_freq) ,ha='center',va='bottom',color="red")
'''
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("样品A第一次")
plt.xlabel("波数")
plt.ylabel("强度")


plt.subplot(1,3, 2)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\2.txt")
x=X[:-10,0]  #波数
y=X[:-10,1]  #信号
#xhat,yhat=smooth(x,y,19)
#yhat=polyFit(xhat,yhat)
#plt.plot(xhat,yhat,'r')
xhat,yhat=smooth(x,y,3)
yhat=polyFit(xhat,yhat)
K=[xhat,yhat]
k=np.savetxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\xy2.txt",K)
x,y=smooth(x,y,7)
baseObj = BaselineRemoval(y)
Y_Modpoly_output=baseObj.ModPoly()
plt.plot(x,Y_Modpoly_output,'y')
'''
from scipy.signal import find_peaks
peak_id,peak_property = find_peaks(y, height=6000, distance=1000)     #更改高度强度间距 
peak_freq = x[peak_id]
peak_height = peak_property['peak_heights']
print('peak_freq',peak_freq)
print('peak_height',peak_height)
plt.bar(peak_freq,peak_height)
for peak_freq,peak_height  in zip(peak_freq,peak_height):
         plt.text(peak_freq,peak_height+300,str(peak_freq) ,ha='center',va='bottom',color="red")
'''
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("样品A第二次")
plt.xlabel("波数")
plt.ylabel("强度")

plt.subplot(1,3, 3)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\3.txt")
x=X[:-10,0]  #波数
y=X[:-10,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)

K=[xhat,yhat]

k=np.savetxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\xy3.txt",K)
plt.plot(xhat,yhat,'b')
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("样品B第一次")
plt.xlabel("波数")
plt.ylabel("强度")



plt.legend()
plt.tight_layout()     # 调整子图间距
#plt.savefig(r"D:\学习\barca\仪器分析实验\数据\raman\raman的图2.png")
plt.show()

plt.style.use("seaborn")
#制作针式搜索结果曲线
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
fig=plt.figure(figsize=(12,4),dpi=700)#创建全局绘图区
plt.subplot(1,3, 1)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\1.txt")
x=X[:-10,0]  #波数
y=X[:-10,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(x,y,'r')
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure10-火山岩样1")
plt.xlabel("波数")
plt.ylabel("强度")


plt.subplot(1,3, 2)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\2.txt")
x=X[:-10,0]  #波数
y=X[:-10,1]  #信号
#xhat,yhat=smooth(x,y,19)
#yhat=polyFit(xhat,yhat)
#plt.plot(xhat,yhat,'r')
#x,y=smooth(x,y,7)
baseObj = BaselineRemoval(y)
Y_Modpoly_output=baseObj.ModPoly()
plt.plot(x,y,'y')
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure11-火山岩样2")
plt.xlabel("波数")
plt.ylabel("强度")

plt.subplot(1,3, 3)
X=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\3.txt")
x=X[:-10,0]  #波数
y=X[:-10,1]  #信号
xhat,yhat=smooth(x,y,7)
yhat=polyFit(xhat,yhat)
plt.plot(x,y,'b')
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.title("Figure12-碳酸锂")
plt.xlabel("波数")
plt.ylabel("强度")



plt.legend()
plt.tight_layout()     # 调整子图间距
#plt.savefig(r"D:\学习\barca\仪器分析实验\数据\raman\raman的图2.png")
plt.show()
