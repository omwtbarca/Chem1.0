import matplotlib.pyplot as plt
import numpy as np
#散点图
x=np.arange(2004,2022,1)
print(x)
y1=[7,21,33,55,48,64,64,70,69,47,66,61,62,64,54,58,48,44] 

y2=[0,3,12,31,22,41,60,59,91,45,58,52,59,54,51,50,27,37]
plt.figure(figsize=(6,13))    #   顺序很重要
y3=[0,4,3,12,18,15,17,36,22,16,22,26,31,16,26,18,19,14]
if len(y1)==len(y2)==len(y3):
    print('GOOD JOB!!!','\n','Date that you input was absolutely correct')
else:
    print("Sorry to inform you that there're some problems with ur data")
#plt.legend(loc='upper right')#绘制曲线图例，信息来自类型label
#plt.legend(labels=['up','down'],loc='best') #best表示自动分配最佳位置

'''
fig=plt.figure(figsize=(11,3),dpi=200)#创建全局绘图区  dpi分辨率200
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplots_adjust(wspace=0.5) #调整子绘图区间隔
fig.add_subplot(131) #绘制纯物质1的光谱图
'''
plt.scatter(x,y1,s=50,color=(0,0.5,0.5),edgecolor='none',label='Appearances')    
plt.scatter(x,y2,s=50,color=(0.5,0,0.5),edgecolor='none',label='Goals')    
plt.scatter(x,y3,s=50,color=(0.5,0.5,0),edgecolor='none',label='Assists') 
y=x**2  #[x**2 for x in x]    both okay
plt.legend()   
#plt.plot(squares,'y',linewidth=5,label="data")
plt.title("El argentino",fontsize=20)

plt.xlabel("Year",fontsize=14)
plt.ylabel("number of total goals",fontsize=14)
#plt.xaxis([2004,2021,1])
plt.tick_params(axis='both',labelsize=14)

plt.savefig('D:\\学习\\barca\\化学信息学\\化学信息学\\jk3.png')
plt.show()

#曲线图示
x=np.arange(2004,2022,1)
print(x)
y1=[7,21,33,55,48,64,64,70,69,47,66,61,62,64,54,58,48,44] 

y2=[0,3,12,31,22,41,60,59,91,45,58,52,59,54,51,50,27,37]
plt.figure(figsize=(6,13))
#plt.legend(loc='upper right')#绘制曲线图例，信息来自类型label
y3=[0,4,3,12,18,15,17,36,22,16,22,26,31,16,26,18,19,14]
if len(y1)==len(y2)==len(y3):
    print('GOOD JOB!!!','\n','Date that you input was absolutely correct')
else:
    print("Sorry to inform you that there're some problems with ur data")
plt.plot(x,y1,linewidth=2,color=(0,0.5,0.5),label='Appearances')    
plt.plot(x,y2,linewidth=2,color=(0.5,0,0.5),label='Goals')    
plt.plot(x,y3,linewidth=2,color=(0.5,0.5,0),label='Assists') 
#plt.legend(title='Appearences',title='Goals',title='Asists')
plt.title("El argentino",fontsize=20)

plt.xlabel("Year",fontsize=14)
plt.ylabel("number of total goals",fontsize=14)
#plt.xaxis([2004,2021,1])
plt.tick_params(axis='both',labelsize=14)

plt.legend()   
plt.savefig("D:\\学习\\barca\\化学信息学\\化学信息学\\jk4.png")
plt.show()
