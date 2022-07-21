#红外光谱  直接提取CSV


import numpy as np
import matplotlib.pyplot as plt
import csv
#X=np.loadcsv(r"D:\学习\barca\仪器分析实验\数据\自主实验\1951815\BACKGROUD.CSV")

X = np.array(list(csv.reader(open(r"D:\学习\barca\仪器分析实验\数据\FTIR红外\F-IR-10.25\F-IR-10.25\ganyou_atr.CSV", "rt"), delimiter=","))).astype("float")
#默认在py文件目录下
#加r在任意目录下"D:\学习\barca\仪器分析实验\数据\自主实验\1951815\PENJING1PUTU.CSV"
x=X[:,0]  #波数
y=X[:,1]  #信号
plt.style.use("seaborn")
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
fig=plt.figure(figsize=(12,6),dpi=700)#创建全局绘图区
plt.plot(x,y,'r',label="原始")
plt.gca().invert_xaxis()#   横轴倒序
plt.gca().invert_yaxis()#   纵轴倒序
plt.title("Figure-Malcom X")
plt.legend()
plt.xlabel("波数")
plt.ylabel("透过率T/%")
plt.show()

X = np.array(list(csv.reader(open(r"D:\学习\barca\仪器分析实验\数据\自主实验\1951815\BACKGROUD.CSV", "rt"), delimiter=","))).astype("float")
#默认在py文件目录下
#加r在任意目录下"D:\学习\barca\仪器分析实验\数据\自主实验\1951815\PENJING1PUTU.CSV"
x=X[:,0]  #波数
y=X[:,1]  #信号
fig=plt.figure(figsize=(12,6),dpi=700)#创建全局绘图区
plt.plot(x,y,'r',label="原始")
plt.gca().invert_xaxis()#   横轴倒序
plt.gca().invert_yaxis()#   纵轴倒序
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.title("Figure-背景")
plt.legend()
plt.xlabel("波数")
plt.ylabel("透过率T/%")
plt.show()

X = np.array(list(csv.reader(open(r"D:\学习\barca\仪器分析实验\数据\自主实验\1951815\PENJING1.CSV", "rt"), delimiter=","))).astype("float")
#默认在py文件目录下
#加r在任意目录下"D:\学习\barca\仪器分析实验\数据\自主实验\1951815\PENJING1PUTU.CSV"
x=X[:,0]  #波数
y=X[:,1]  #信号
fig=plt.figure(figsize=(12,6),dpi=700)#创建全局绘图区
plt.plot(x,y,'r',label="原始")
plt.gca().invert_xaxis()#   横轴倒序
plt.gca().invert_yaxis()#   纵轴倒序
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.title("Figure-盆景")
plt.legend()
plt.xlabel("波数")
plt.ylabel("透过率T/%")
plt.show()

X = np.array(list(csv.reader(open(r"D:\学习\barca\仪器分析实验\数据\自主实验\1951815\PENJING1PUTU.CSV", "rt"), delimiter=","))).astype("float")
#默认在py文件目录下
#加r在任意目录下"D:\学习\barca\仪器分析实验\数据\自主实验\1951815\PENJING1PUTU.CSV"
x=X[:,0]  #波数
y=X[:,1]  #信号
fig=plt.figure(figsize=(12,6),dpi=700)#创建全局绘图区
plt.plot(x,y,'r',label="原始")
plt.gca().invert_xaxis()#   横轴倒序
plt.gca().invert_yaxis()#   纵轴倒序
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.title("Figure-盆景")
plt.legend()
plt.xlabel("波数")
plt.ylabel("透过率T/%")
plt.show()