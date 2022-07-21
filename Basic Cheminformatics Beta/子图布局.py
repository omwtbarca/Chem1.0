
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
 
fig = plt.figure()
gs = GridSpec(3, 3, figure=fig)
 
ax1 = fig.add_subplot(gs[0,:])
ax2 = fig.add_subplot(gs[1:3,0])
ax3 = fig.add_subplot(gs[1,1:])
ax4 = fig.add_subplot(gs[2,1])
ax5 = fig.add_subplot(gs[2,-1])
for i,ax in enumerate(fig.axes):
    ax.text(0.5,0.5,"ax%d" % (i+1),va="center", ha="center")
plt.show()
import numpy as np  
import matplotlib.pyplot as plt
x = np.arange(0, 100)  
#划分子图
fig,axes=plt.subplots(2,2)
ax1=axes[0,0]
ax2=axes[0,1]
ax3=axes[1,0]
ax4=axes[1,1]

#作图1
ax1.plot(x, x)  
#作图2
ax2.plot(x, -x)
 #作图3
ax3.plot(x, x ** 2)
ax3.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
#作图4
ax4.plot(x, np.log(x))  
plt.show() 