import numpy as np
import math
class ITTFA:

    T=P=X=None
    recordX=None
    def __init__(self,X):
        self.X=X
        self.recordX=np.arange(X.shape[0])
    def getEigenValueInfo(self):
        B = np.linalg.svd(self.X,full_matrices=False)
        self.lamda=lamda = B[1]
        self.T=B[0]*B[1]
        self.P=B[2].T

        lam=[]
        for i in range(len(lamda)-1):
            lam.append(lamda[i]/lamda[i+1])
        return lam
            
    def PCAdecompose(self,pcs):
        self.T=self.T[:,:pcs]  # 取pcs主成分
        self.P=self.P[:,:pcs]
        self.lamda=self.lamda[:pcs]
        self.pcs=pcs  # 系统的组分数
        
    def needleSearch(self):
        kk=self.T.shape[0]  # 色谱保留时间  采样点数
        nsresult =np.zeros(kk)
        #根据公式   ci = T * ri   ; ri = (T'T).inverse() * T' * ci;
        # 所以  下一个迭代出来的  ci =  T * (T'T).inverse() * T' *  ci;
        # 因此 先求出  T * (T'T).inverse() * T' 可以大大的加快计算的速度
        #让 temp = T * (T'T).inverse() * T';
        
        # 构造 T'T的逆矩阵 temp1,是奇异值的平方  再倒数，再对角化
        
        temp1 =np.diag(1 / self.lamda**2) 
        temp = self.T @ temp1 @ self.T.T
        
        
        colMax=temp.max(axis=0)
        temp=temp/colMax
        I=np.eye(kk)
        temp=temp-I
        error=(temp**2).sum(axis=0)
        nsresult=np.sqrt(error)/np.sqrt(kk-1.0)
        '''
        for i in range(kk):
            c_begin=np.zeros(kk)
            c_begin[i]=1
            c_end = temp.dot(c_begin)
            maxValue=max(c_end)
            c_end = c_end / maxValue
            error =sum( (c_end - c_begin)**2)
            nsresult[i] = math.sqrt(error)/ math.sqrt(kk - 1.0)
        '''    
        minLocation = self.findMinLocation(nsresult)
        return nsresult,minLocation
        
    def findMinLocation(self,nsresult):
        kk=len(nsresult)
        min_time = []
        if nsresult[0] < nsresult[1]:  #判断开始
            min_time.append(self.recordX[0])
        
        
        
        # 以求二阶导数的方法求
        a=nsresult[:-1]
        b=nsresult[1:]
        c=b-a  # 一阶导数
        c[c>0]=1
        c[c<0]=-1
        b=c[1:]
        a=c[:-1]
        c=b-a  # 二阶导数
        ans=np.where(c==2)[0]+1
        min_time.extend(list(ans))
        
        '''
        
        # for 判断中间的极小点
                
        for i in range(1,kk-1):
            if nsresult[i] < nsresult[i - 1] and nsresult[i] < nsresult[i + 1]:
                min_time[j] = self.recordX[i]
                j+=1
        '''       
        if (nsresult[kk-1] < nsresult[kk-2]):  #判断尾部的极小点
            min_time.append(self.recordX[kk-1])
        
        minList = min_time[:self.pcs]   # 找到j个最小点，应该等于组分数啊 
        '''
        for i in range(j):
            minList[i] = min_time[i]
        '''
        return np.array(minList)
            
    def getR(self,minList):
        kk=len(minList)  # 组分数
        if self.T.shape[1] != kk:
            return False
        self.R = np.zeros((kk,kk))
        self.C=np.zeros((self.T.shape[0],kk))
        row = self.T.shape[0]
        c_begin=c_end=error=r=None
        # 求临时矩阵　　T'T的逆　* T'
        temp1 =np.diag(1 / self.lamda**2)  # 这是逆
        temp = temp1.dot(self.T.T)
        for i in range(kk):
            c_begin = np.zeros(row)
            c_begin[int(minList[i])] = 1
            maxPos=int(minList[i])
            count = 0
            while True:
                r = temp.dot(c_begin)
                c_end = self.T.dot(r)
                maxValue =np.max(c_end)
                maxPos=np.argmax(c_end)
                c_end = c_end / maxValue
                c_end[c_end<0]=0 # 不允许负数

                for  k in range(maxPos,0,-1): #从最大点向左,如果发现左边点的值大于右边点的值,强行将其变成和右边一样的值
                    if c_end[k] < c_end[k - 1]:
                        c_end[k - 1] = c_end[k] * 0.99
                        
                for k in range(maxPos,len(c_end)-1,1):  # 从最大点向右,如果发现右边点的值大于左边点的值,强行将其变成和左边一样的值
                    if c_end[k] < c_end[k + 1]:
                        c_end[k + 1] = c_end[k] * 0.99
                        
                error = math.sqrt(np.sum((c_end - c_begin)**2)/row)
                c_begin = c_end
                
               
                count+=1
                if count > 50: 
                    break
                if error<1e-10:
                    break
                
            self.R[:,i]= r
            self.C[:,i]=c_end
                # 得到一列r后,可以计算得到物质的纯色谱, 如果纯光谱也知道,就可以得到一组分的纯2维谱
        return True
    def getCS(self,minList):
        self.getR(minList)
        C = self.T.dot(self.R)
        #C=self.C
        S = np.linalg.inv(self.R).dot(self.P.T)
        #S= np.linalg.inv(C.T @ C) @ C.T @  self.X
        S=S.T
        return C,S
        
def obeyOnePeak(C,minLocation):
    for i in range(C.shape[-1]):
        c_end = C[:,i]
        maxPos=int(minLocation[i])
        for  k in range(maxPos,0,-1): #从最大点向左,如果发现左边点的值大于右边点的值,强行将其变成和右边一样的值
            if c_end[k] < c_end[k - 1]:
                c_end[k - 1] = c_end[k] * 0.99
                
        for k in range(maxPos,len(c_end)-1,1):  # 从最大点向右,如果发现右边点的值大于左边点的值,强行将其变成和左边一样的值
            if c_end[k] < c_end[k + 1]:
                c_end[k + 1] = c_end[k] * 0.99
    

#X=np.loadtxt (r"F:\teach\programTeach\InfoTeach\shuijie.txt")  #读混合物光谱矩阵


'''
X=np.loadtxt (r"gcms模拟.txt")  #读混合物光谱矩阵
X=X[0:60]
ittfa=ITTFA(X)
lamdaInfo=ittfa.getEigenValueInfo()
print("特征值",lamdaInfo)
k=np.argmax(lamdaInfo)+1
#k=int(input('请确定主成分数='))
ittfa.PCAdecompose(k)
nsresult,minLocation=ittfa.needleSearch()
recordX = np.arange(len(X))



import matplotlib.pyplot as plt

plt.plot(recordX,nsresult)
plt.xlabel("position")
plt.ylabel("height ")

plt.show()
print(minLocation)
#minLocation[0]=25
C,S=ittfa.getCS(minLocation)  # ITTFA 计算的结果

print(C.argmax(axis=0))

# X=CS  迭代ALS
size=C.size
Cnew=C
i=0
E=np.eye(C.shape[-1])
while True:
    C=Cnew
    S= np.linalg.inv(C.T @ C+0.01*E) @ C.T @ X
    S[S<0]=0
    Cnew=X @ S.T @ (np.linalg.inv( S @ S.T)+0.01*E)
    Cnew[Cnew<0]=0
#    obeyOnePeak(Cnew,minLocation)
    #err=np.sqrt(np.sum((C-Cnew)**2)/size)
    err=X-C @ S
    err=np.sqrt((err**2).sum()/X.size)
    #print(err)
    if err<1e-6:
        break
    
    i +=1
    if i>2000:
        break

S=S.T
ma=S.max(axis=0)
S =S/ma *1000

C =C*ma  /1000 

x=np.arange(len(C))
for i in range(C.shape[1]):
    plt.plot(x,C[:,i])

plt.xlabel("time")
plt.ylabel("height ")    
plt.show()    

print(C.argmax(axis=0))



x=np.arange(len(S))
# S 归一化
#S=S/S.max(axis=0)
for i in range(S.shape[1]):
    plt.bar(x,S[:,i])
    plt.xlabel("wavelegth")
    plt.ylabel("height ")     

    plt.show()

err=X-C @ S.T
err=np.sqrt((err**2).sum(axis=0)/X.shape[0])
print(err)
'''



'''
orig=np.sqrt((X**2).sum(axis=0)/X.shape[0])
print(orig)
'''
