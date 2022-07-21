#全自动滴定
#全自动滴定  V体积   E电位
#1.NaOH标定   一阶微商  二阶微商

import numpy as np
from numpy import diff
import matplotlib.pyplot as plt
S=np.loadtxt("D:\\学习\\barca\\仪器分析实验\\数据\\全自动电位滴定\\滴定.txt")
V=S[:,0:1]
#V=float(V)
V= np.round(V, 3)
E=S[:,1:2]
#E= float(np.array(E))
E= np.round(E,1)
#dE=S[:,2]
dEdV=np.array(diff(E.T)/diff(V.T)).T
dEdV= np.round(dEdV,1)
print("V=",V,'\n')
print("E=",E,'\n')

print("dEdV=",dEdV,'\n')

fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区  dpi分辨率200
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplots_adjust(wspace=0.5) #调整子绘图区间隔
fig.add_subplot(131) #绘制纯物质1的光谱图
plt.plot(V,E,color=(0.3,0.8,0.3))
plt.title("E-V Titration curve of mixed acid.",fontsize=10)
plt.xlabel("Volume/mL")
plt.ylabel("Potential/V")

#一阶微商
fig.add_subplot(132) 
plt.plot(V[1:],(dEdV),color=(0.8,0.3,0.3))
plt.title("一阶微商曲线 dE/dV-V ",fontsize=10)
plt.xlabel("Volume/mL")
plt.ylabel("Potential/V")
a = min(dEdV) #最大值
for i in range (0,len(dEdV)):
      if dEdV[i]==a:
           print("对应体积:",'%.3f' %V[i],"mL")


print("图中的最小值:",'%.1f' % a,"V")  # 默认保留6位小数

#二阶微商
dEdV2=np.array(diff(dEdV.T)/diff(V[:-1].T)).T
a = min(dEdV2) #最大值
for i in range (0,len(dEdV2)):
    if dEdV2[i]==a:
        print("对应体积:",'%.3f' %V[i],"mL")
print("图中的最小值:",'%.1f' % a,"V")  # 默认保留6位小数

print("dEdV2=",dEdV2,'\n')
print(len(V),"两个维度",len(E),len(dEdV),len(dEdV2),len(V[:-1]))
fig.add_subplot(133) 
plt.title("二阶微商曲线 d2E/dV2-V ",fontsize=10)
plt.xlabel("Volume/mL")
plt.ylabel("Potential/V")
plt.plot(V[:-2],(dEdV2),color=(0.8,0.3,0.8))
#plt.savefig('D:\\学习\\barca\\仪器分析实验\\数据\\全自动电位滴定\\标定.png')
plt.legend()
plt.show()

    



