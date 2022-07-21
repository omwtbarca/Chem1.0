
'''
#线性插值程序
import numpy as np
from scipy.interpolate import interp1d
x=np.array([190,194,198,202,206,210])
y=np.array([2.64,2.88,2.61,1.35,0.949,0.851])
fl=interp1d(x,y,kind='linear')  # 线性插值函数   #两点法
xin=np.array([204,208]) # 插值点在204,208
yin=fl(xin) # 由线性插值得到的函数值
print(yin)

#连续函数的积分求解 ——————————scipy提供的integrate包中的quad类！！！

#计算函数f(x) =x2在[0，1.8]区间的积分。

from scipy.integrate import quad
def func(x):
    return x **2
ans=quad(func,0,1.8)
print(ans)

#离散积分求解——合成氨
from scipy.integrate import trapz,simps
import math
import numpy as np
data=np.loadtxt(r"F:\teach\programTeach\InfoTeach\氨合成反应.txt")
T=data[0]
y=data[1]
y=y/T**2
s=trapz(y,T)   #  也可以用simps(y,T)     函数在前 自变量在后
R = 8.314/1000; #//单位差异，△rHm为千J
p2 = math.exp(s / R)
kp1 = 2644
kp2 = kp1 * p2;
print(kp2)
'''

#离散积分求解——习题相变标准熵
from scipy.integrate import trapz,simps
import math
import numpy as np
data=np.loadtxt(r"D:\学习\barca\化学信息学\化学信息学\积分插值\T(K)-Cp, m.txt")
T=data[0] 
print("T=",T)
C=data[1]
print("C=",C)
y=C/T
Sm=trapz(y,T)   #  也可以用simps(y,T)     函数在前 自变量在后
ST1=2.4
ST2=Sm+ST1 
print("铅在500K下的标准熵为",ST2,'$J.K^(-1).mol^(-1)$')  #单位不知道为什么不能这样表达。。。
