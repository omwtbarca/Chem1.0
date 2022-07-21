import numpy as np
t=np.arange(10,60,0.05)                 #时间10-60///5-70min ，间隔0.05min
c1=0.8*np.exp(-((t-15)/(5))**2)         #色谱 单峰
c2=0.8*np.exp(-((t-45)/(8))**2)
import matplotlib.pyplot as plt    
wl=np.arange(200,600,2)                #波长200-600nm ，间隔2
p1=0.8*np.exp(-((wl-250)/(30))**2)     #wl=wave length
p2=0.4*np.exp(-((wl-350)/(20))**2) 
p3=0.2*np.exp(-((wl-450)/(10))**2) 
s=p1+p2+p3 #组分1的光谱  3个峰
sMAX=max(s)
print("初始模拟峰值为：",sMAX)
x=np.random.random(200)           #采样点数（600-200）/2
x=(x-0.5)*(3/5)/10                #plus3% 
s=p1+p2+p3+x                      #组分1的光谱  3个峰
sMAX=max(s)
print("加噪声后峰值为：",sMAX)
p1=0.4*np.exp(-((wl-220)/(30))**2)     #wl=wave length
p2=0.5*np.exp(-((wl-480)/(20))**2) 
s2=p1+p2
plt.plot(wl,s)
plt.show()
C_DAD1=np.outer(c1,s) 
C_DAD2=np.outer(c2,s2) 
C_DAD=C_DAD1+C_DAD2                #外积  浓度向量X  光谱   
X,Y=np.meshgrid(wl,t)
 #3D引用函数库
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import cm
fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(X,Y,C_DAD,cmap=cm.jet)
plt.show()
'''
u,s,v=np.linalg.svd(C_DAD)     #特征值函数
print(s**2)
rank=np.linalg.matrix_rank(C_DAD)
print(rank)
#DAD   二极管阵列检测器'''