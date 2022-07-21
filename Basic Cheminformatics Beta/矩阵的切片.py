import numpy as np  
a=np.random.standard_normal((9,4))
print(a)
xSel=[0,5,7]
ySel=[1,3]
b=a[xSel]#选择指定行
b=b[:ySel]#再选择指定列
print(b)  '''
b=a[xSel,ySel]  #不允许同时选择


x=np.random.rand(4,4)
print(x)
v=x[:,0]
d=x[:,1]
z=x[:,0:1]
c=x[:,1:]
print ('\n',v,'\n','\n',d,'\n','\n',z,'\n','\n',c)