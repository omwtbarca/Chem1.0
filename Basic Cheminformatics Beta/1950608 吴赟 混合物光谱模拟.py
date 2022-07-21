# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:03:02 2021

@author: 86187
"""

'''
配置一个混合物，此混合物共有两个组分，两个组分纯物质时的光谱已知，如下A1、A2
'''
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(300,600,5)#光谱仪扫描范围300-600nm，分辨率5nm
A1 = 0.75*np.exp(-((x-320)/(80))**2)
A2 = 0.92*np.exp(-((x-390)/(50))**2)
S = np.vstack([A1,A2])
'''
老师在上课时使用的是np.c_([A1,A2])，形成了一个n行2列的矩阵后再进行转置，
其结果与直接使用np.vstack([A1,A2])将两个数组进行垂直拼接是一样的，
这样可以减少转置的那一步
'''
c = np.array([0.5,0.5])#配置的混合物中两个组分的浓度
A = c.dot(S)#得到混合物光谱
#下面绘图
fig=plt.figure(figsize=(11,3),dpi=100)#创建全局绘图区
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.subplots_adjust(wspace=0.3) #调整子绘图区间隔
fig.add_subplot(131) #绘制纯物质1的光谱图
plt.plot(x,A1,"g")
plt.xlabel("波长/nm")
plt.ylabel("A")
plt.yticks(np.arange(0,1.2,0.2))
plt.title("纯物质1的光谱图")
fig.add_subplot(132) #绘制纯物质2的光谱图
plt.plot(x,A2,"c")
plt.xlabel("波长/nm")
plt.ylabel("A")
plt.yticks(np.arange(0,1.2,0.2))
plt.title("纯物质2的光谱图")
fig.add_subplot(133) #绘制混合物光谱图
plt.plot(x,A,"r")
plt.xlabel("波长/nm")
plt.ylabel("A")
plt.yticks(np.arange(0,1.2,0.2))
plt.title("混合物的光谱图")
plt.show()
'''
这两个物质混合后,峰重叠在一起，无法区分
'''