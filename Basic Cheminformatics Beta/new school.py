from numpy import diff
x = [.1, .2, .5, .6, .7, .8, .9]
y = [1, 2, 3, 4, 7, 5, 6]
'''dydx = diff(y)/diff(x)
print( dydx )
[10., 3.33333,  10. ,   0. , 10. ,  10.]
lst = [1,2,3]
'''
a = max(y) #最大值
b = y.index(max(y)) #最大值的位置
print("列表的最大值:{}".format(a),"位置:{}".format(x[b]))
