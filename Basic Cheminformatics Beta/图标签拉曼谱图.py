# -*- coding: utf-8 -*-    scipy.signal.find_peaks
"""
Created on Fri Dec 24 18:45:45 2021

@author: Lenovo
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt
plt.style.use("seaborn")
# 制作针式搜索结果曲线
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
fig = plt.figure(figsize=(12, 10), dpi=700)  # 创建全局绘图区
X = np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\raman\F-Raman\benjiasuan.txt")
x = X[:, 0]  # 波数
y = X[:, 1]  # 信号

# 已导入需要处理的数据(x,y)
from BaselineRemoval import BaselineRemoval
baseObj = BaselineRemoval(y)
y=baseObj.ModPoly()
plt.plot(x, y, 'r', label="苯甲酸")

# y 轴不可见
####   寻求特征峰！！！
from scipy.signal import find_peaks
peak_id,peak_property = find_peaks(y, height=1500, distance=100)     #更改高度强度间距 
peak_freq = x[peak_id]
peak_height = peak_property['peak_heights']
print('peak_freq',peak_freq)
print('peak_height',peak_height)
plt.bar(peak_freq,peak_height)
for peak_freq,peak_height  in zip(peak_freq,peak_height):
         plt.text(peak_freq,peak_height+300,str(peak_freq) ,ha='center',va='bottom',color="red")

#k = scipy.signal.find_peaks()

plt.xlabel("波数")
plt.ylabel("拉曼相对强度")

plt.title("苯甲酸的拉曼谱图")


plt.legend()


# plt.savefig(r"D:\学习\barca\仪器分析实验\数据\raman\raman的单图.png")

plt.show()
