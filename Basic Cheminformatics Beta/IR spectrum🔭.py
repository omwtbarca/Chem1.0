import numpy as np
x=np.arange(400,4000,1)
x1=-0.8*np.exp(-3.2/(1244-x)**2)
x2=-0.8*np.exp(-3.4/(3168-x)**2)
import matplotlib.pyplot as plt
plt.plot(x,x1,'r-')
plt.plot(x,x2,'g-')
plt.title('IR spectrum🔭')
plt.xlabel('number of wave  /cm^(-1)')
plt.ylabel('intensity')
plt.legend()
plt.show()