import numpy as np
import random as rand 
import matplotlib.pyplot as plt
import math
import matplotlib.ticker as ticker
print('введите количество точек')
N=int(input()) 
nnn=0
x = np.linspace(0,2,30)
y=math.e**x
fig, ax = plt.subplots()
plt.title('График нахождения экспененты методом Монте-Карло')
ax.plot(x,y,color='green')
ax.plot([0.0,0.0],[0.0,3.0],color='blue')
ax.plot([1.0,1.0],[0.0,3.0],color='blue')
ax.plot([0.0,1.0],[3.0,3.0],color='blue')
ax.plot([0.0,1.0],[0.0,0.0],color='blue')
ax.grid()
i=0
while i<N+1:
    b=np.random.random()
    p=np.random.random()
    a=3*p
    y1=math.exp(b)
    i=1+i
    from pylab import *
    ax.plot(b, a,'.',color='red')
    if y1>a:
        nnn=nnn+1
w=(3*nnn)/(N)+1 
print(w) 




E=math.exp(1)

z=np.zeros((3,10))
print(E)
for i in range(10):
    z[0][i]=i
c=0
j=len(str(E))-1    
for i in range(j):
    E=E*10
    k=int(E//10)
    E=E-k*10
    z[1][k]=z[1][k]+1

j=len(str(w))-1
for i in range(j):
    w=w*10
    k=int(w//10)
    w=w-k*10
    z[2][k]=z[2][k]+1

    



fig1, ax = subplots()
plt.title('Гистограмма экспоненты из math')
ax.bar(z[0]-0.2,z[1],0.5,color='black')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))



fig2,ax1=subplots()
plt.title('Гистограмма экспоненты найденной самостоятельно')
ax1.bar(z[0],z[2],0.5,color='red')
ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.show()


    
    
    
    
    