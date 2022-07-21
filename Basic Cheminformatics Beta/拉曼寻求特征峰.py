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
#frame = plt.gca()
# y 轴不可见
# frame.axes.get_yaxis().set_visible(False)
plt.yticks([])


X = np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\自主实验\weilizhen\1.txt")
x = X[:, 0]  # 波数
y = X[:, 1]  # 信号
# xhat,yhat=smooth(x,y,7)
# yhat=polyFit(xhat,yhat)
plt.plot(x, y, 'r', label="甲醇")
plt.xlabel("波数")
plt.ylabel("拉曼相对强度")

plt.title("Figure-各样品的拉曼谱图")
plt.show()
from scipy.signal import find_peaks
# 已导入需要处理的数据(x,y)
plt.plot(x,y)
plt.xlabel('freq/Hz')
plt.ylabel('amp')
####   寻求特征峰！！！
peak_id,peak_property = find_peaks(y, height=1000, distance=20)
peak_freq = x[peak_id]
peak_height = peak_property['peak_heights']
print('peak_freq',peak_freq)
print('peak_height',peak_height)


#k = scipy.signal.find_peaks()

plt.legend()


# plt.savefig(r"D:\学习\barca\仪器分析实验\数据\raman\raman的单图.png")

plt.show()
