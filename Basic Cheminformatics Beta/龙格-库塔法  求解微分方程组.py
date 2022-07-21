#龙格-库塔法  求解微分方程组

import numpy as np
def func(t, y):
    #//定义每种组分的微分方程，注意y是数组，对应四种组分  y[0]--A
    k1 = 0.189;k2 = 0.00572;k3 = 0.090
    y1 = -k1 * y[0] - k3 * y[0]
    y2 = k1 * y[0] - k2 * y[1]
    y3 = k2 * y[1] + k3 * y[0]
    y4 = k1 * y[0] + k3 * y[0]
    ans=np.array([y1,y2,y3,y4])
    return ans
from scipy.integrate import RK45
sol = RK45(func, 0,  (1,0,0,0),360,max_step=0.1)
#0开始时间，,  (1,0,0,0)4个组分的起始浓度，360终止时间
sol._step_impl() #执行一步，第一次是初始点
b=[sol.t]  # 起步时间
a=sol.y    # 起步函数值，就是(1,0,0,0)
for i in range(3600):   #3600步
    sol._step_impl() #执行一步，指从当前点到下一点
    b.append(sol.t) #下一点的时间值
    a=np.c_[a,sol.y] # 下一点的y值，有4种组分，y是数组，在sol.y中，每4个数作为一列，堆叠
a=a.T # 原来是按列存放每个步骤的值，转置为行，便于制图

t=b  # 时间
track1=a  # 浓度轨迹
import matplotlib.pyplot as plt 
fig=plt.figure(dpi=1000)
plt.style.use("seaborn")
plt.plot(t,track1[:,0], 'r',label='A')
plt.plot(t,track1[:,1],'g',label='B')
plt.plot(t,track1[:,2], 'b',label='C')
plt.plot(t,track1[:,3], 'c',label='D')
plt.legend()
plt.show()
