import math
def decay(t, x):  # 常微分方程函数定义
    rate=2.33*1e-5*3600 * (7.0 - x) * math.sqrt(x)  # dy/dx的计算公式
    return rate
from scipy.integrate import solve_ivp
sol = solve_ivp(decay, [0,  14],(0.16,),t_eval=[0, 2, 4, 6, 8,10,14])
#[0,14]是x取值范围，(0.16,)是y的初值，t_eval是期望的观测点
print(sol.t.T)
print(sol.y.T)



# -*- coding: utf-8 -*-
import time
import matplotlib.pyplot as plt

def showResult(xList, yList, title, xLabel, yLabel):
    plt.plot(xList, yList, 'g*-')
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    for x, y in zip(xList, yList):
        plt.text(x, y+1, str(y), ha='center', va='bottom', fontsize=10.5)
    plt.savefig('fig'+str(int(time.time()))+'.jpg')
    plt.show()

x_arr = [1, 2, 3, 4, 5, 6]
y_arr = [1, 4, 9, 16, 25, 36]
showResult(x_arr, y_arr, 'title', 'x', 'y')