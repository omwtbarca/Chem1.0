import numpy as np
a=np.random .rand(5,5)      #随机产生5X5矩阵
b=np.savetxt('omwtbarca1.txt',a,fmt='%5.2f')  #文件名单引号 文件地址加文件名双引号加双左斜杠，所存变量,（逗号）
#fmt（数据格式） 宽度5位 保留两位小数
# delimiter='\t',newline'\r\n'    列分隔符 换行符
Z=np.loadtxt('omwtbarca1.txt')   #D:\\学习\\西班牙语\\题\\
print(Z)
x=np.array([[2,3],[6,8],[9,1],[5,2]])   #array矩阵双方括号
print(x)    #输出全部
print(x[0])  #单个行索引
print(x[2][0])  #元素索引
#矩阵加法   C=A+B
A=np.array([[1,2,3,4],[2,1,2,3]])
B=np.array([[4,2,5,4],[2,7,7,3]])
C=A+B
print(C)
#矩阵的行和列数 维数
size=A.shape
print(size[0],size[1])  #size[0]行数,size[1]列数
#矩阵相乘(矩阵乘矩阵）   前提是A的列数B的行数要相同方法一： D=np.dot(A,B)
#           方法二：D=A.dot(B)
A1=np.array([[1,2,3,4],[2,1,2,3]])
B1=np.array([[4,2,],[7,3],[7,3],[7,3]])
H=np.dot(A1,B1)
print(H)
E=A1.dot(B1)
print(E)
#矩阵相乘(矩阵乘常数）用*
F=2*A1
print(F)
#矩阵转置    B=A.T   或者B=np.transpose(A)
G=(A1).T
print(G)
#方阵求逆     要求原矩阵是满秩方阵   B=np.linalg.inv(A)
A=np.array([[1,2,3,4],[2,1,2,3]])
B=np.array([[4,2,],[7,3]])
C=A.T#转置
print(C)
#求逆矩阵
D=np.linalg.inv(B)
print(D)
F=D.dot(B)
print(F)
#求矩阵的秩
x=np.arange(200,600,2)
y1=0.8*np.exp(-((x-200)/(10))**2)
y2=0.3*np.exp(-((x-210)/(10))**2)
C=0.1*y1+0.4*y2
Y=np.c_[y1,y2,C]

U,S,V=np.linalg.svd(Y)     #inv求逆   svd求rank of the matrix
print('\n',S**2)
#求矩阵的秩
import numpy as np
P=np.mat([[1,2,3],[2,4,6],[7,8,9]],int)
print(P)    #,{:.5f}
rank=np.linalg.matrix_rank(P)
print (rank) 