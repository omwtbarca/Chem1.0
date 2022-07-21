import matplotlib.pyplot as plt
import numpy as np
import cmath
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import cython
import os

L = 20
n = 300
nt = int(200*n/6)
alpha = 2
m = 1
h = 6.62607015 * (10**(-34))
hbar = 1

T = 2*L/(400)
print(T)

x =np.linspace(-L, L, n)
y =np.linspace(-L, L, n)
t =np.linspace(0, 60, nt)

dx = x[1] - x[0]
dy = y[1] - y[0]
dt = t[1] - t[0]

print(dt/(dx*dx))
input("")

X, Y = np.meshgrid(x, y)

def psi_0(x, y):
    S = []
    Sr = []
    Si = []
    for w in y:
        Sx = []
        Sxr = []
        Sxi = []
        for i in x:
            s = (1-1j) * ((np.exp(-((i-L/2)**2 + (w-L/2)**2)/alpha)) / (2*np.pi*alpha))
            Sx.append(s)
            Sxr.append(s.real)
            Sxi.append(s.imag)
        S.append(np.array(Sx))
        Sr.append(np.array(Sxr))
        Si.append(np.array(Sxi))
    return(Sr, Si, S)

psi0 = psi_0(x, y)
psi0r = np.array(psi0[0])
psi0i = np.array(psi0[1])
psi0N = np.array(psi0[2])

fig = plt.figure()

ax = fig.add_subplot(211, projection = '3d')
ax.plot_surface(X, Y, np.array(psi0r), cmap = cm.plasma, linewidth=0, antialiased=True)
ax.axes.set_xlim3d(left=0, right=L)
ax.axes.set_ylim3d(bottom=0, top=L)
ax.axes.set_zlim3d(bottom=-1, top=1)

def V(x, y):
    S = []
    for w in y:
        Sx = []
        for i in x:
            s = 10*np.exp(0.1*(w+i-L))
            Sx.append(s)
        S.append(np.array(Sx))
    return(S)

V = V(x, y)

ax = fig.add_subplot(121, projection = '3d')
ax.plot_surface(X, Y, np.array(V), cmap = cm.plasma, linewidth=0, antialiased=True)
ax.axes.set_xlim3d(left=0, right=L)
ax.axes.set_ylim3d(bottom=0, top=L)
ax.axes.set_zlim3d(bottom=-1.2, top=1.2)
plt.show()

PSI = []
PSIR = []
PSII = []
PSI.append(psi0N)
PSI.append(psi0N)
PSIR.append(psi0r)
PSIR.append(psi0r)
PSII.append(psi0i)
PSII.append(psi0i)
psix = []
psixR = []
psixI = []
psiy = []
psiyR = []
psiyI = []

psi = 0

def plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    plt.ion()

    for i in range(nt):
        plt.clf()
        ax = fig.add_subplot(111, projection = '3d')
        plt.title('Time = {} secondes'.format(t[i]))
        ax.plot_surface(X, Y, PSIR[i], cmap = cm.plasma, linewidth=0, antialiased=True)
        ax.axes.set_xlim3d(left=-L, right=L)
        ax.axes.set_ylim3d(bottom=-L, top=L)
        ax.axes.set_zlim3d(bottom=-0.2, top=0.4)
        if i%5 == 0:
            plt.savefig("{}.png".format(i))
        plt.pause(dt)

for i in range(1, nt - 2):
    os.system("clear")
    print(int(100*i/nt), " %")
    print(i, " / ", nt)
    psiy = []
    psiyR = []
    psiyI = []
    psiy.append(PSI[i][0])
    psiyR.append(PSIR[i][0])
    psiyI.append(PSII[i][0])
    for v in range(1, n-1):
        psix = []
        psixR = []
        psixI = []
        psix.append(PSI[i][0][0])
        psixR.append(PSIR[i][0][0])
        psixI.append(PSII[i][0][0])
        for u in range(1, n-1):
            try:
                psi = PSI[i-1][v][u] + ((1j/2*hbar) * ( ((hbar*hbar/(2*m)) * (0.5*(PSI[i][v][u+1] - 2*PSI[i][v][u] + PSI[i][v][u-1] + PSI[i-1][v][u+1] - 2*PSI[i-1][v][u] + PSI[i-1][v][u-1])/(2*dx*dx) + 0.5*(PSI[i][v+1][u] - 2*PSI[i][v][u] + PSI[i][v-1][u] + PSI[i-1][v+1][u] - 2*PSI[i-1][v][u] + PSI[i-1][v-1][u])/(2*dy*dy)) + V[v][u]*PSI[i][v][u]))*dt) 
                psix.append(psi)
                psixR.append(psi.real)
                psixI.append(psi.imag)
            except KeyboardInterrupt:
                plot()


        psix.append(psi)
        psixR.append(psi.real)
        psixI.append(psi.imag)

        psiy.append(np.array(psix))
        psiyR.append(np.array(psixR))
        psiyI.append(np.array(psixI))

    psiy.append(np.array(psix))
    psiyR.append(np.array(psixR))
    psiyI.append(np.array(psixI))

    PSI.append(np.array(psiy))
    PSIR.append(np.array(psiyR))
    PSII.append(np.array(psiyI))

input("")
plot()