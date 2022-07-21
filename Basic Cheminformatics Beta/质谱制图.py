import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as matcoll


mz=np.arange(70,180)
X=np.loadtxt (r"D:\学习\barca\仪器分析实验\数据\LCMS\lc-ms-F\txt\195MS.txt")
x=X[:,0]
y=X
lines = []
for i, j in zip(x,y):
    pair = [(i, j[0]), (i, j[1])]
    lines.append(pair)
    linecoll = matcoll.LineCollection(lines, colors='k')

fig, ax = plt.subplots(dpi=500)

#plt.plot(x, [i for (i,j) in y],  markersize = 4)
plt.plot(x, [j for (i,j) in y], 'bo', markersize = 0)
ax.add_collection(linecoll)
plt.title("Figure5-279 Mass Chromatogram") #改名字和路径
plt.style.use("seaborn")
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.xlabel("质荷比m/z")
plt.ylabel("Intensity")

fig.tight_layout()  # 全局整理图片尺寸

plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as matcoll


mz=np.arange(70,180)
X=np.loadtxt (r"D:\学习\barca\仪器分析实验\数据\LCMS\lc-ms-F\txt\195MS.txt")
x=X[:,0]
y=X
print("x=",x)
print("y=",y)
lines = []
for i, j in zip(x,y):
    pair = [(i, j[0]), (i, j[1])]
    lines.append(pair)
    linecoll = matcoll.LineCollection(lines, colors='k')
fig, ax = plt.subplots(dpi=500)


#plt.plot(x, [i for (i,j) in y],  markersize = 4)
plt.plot(x, [j for (i,j) in y], 'bo', markersize = 0)
ax.add_collection(linecoll)
plt.title("Figure5-母离子195.1m/z Mass Chromatogram") #改名字和路径
plt.style.use("seaborn")
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.xlabel("质荷比m/z")
plt.ylabel("Intensity")
y=X[:,1]

plt.bar(x,y)
for x,y in zip(x, y):
         plt.text(x+1,y+10000,str(x) ,ha='center',va='bottom',color="red")
fig.tight_layout()  # 全局整理图片尺寸
plt.savefig(r'D:\Desk\Figure5-279 Mass Chromatogram.png')
plt.show()



