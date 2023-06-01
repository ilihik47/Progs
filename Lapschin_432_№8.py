'Решить неявным методом Адамса при k=1 задачу Коши'
import math
import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt



def func(x,y,dy,d2y):
    return math.sin(x)+4*y-4*dy+5*d2y


def main():
    p=256
    h=0.1/p 
    x=[]
    y=[]
    dy=[]
    d2y=[]
    
    x.append(0)
    y.append(1)
    dy.append(0)
    d2y.append(0)
    i=0
    while x[i]<=2:
        x.append(x[i]+h)
        i=i+1
        
    for i in range(len(x)-1):
        y.append(y[i]+h*dy[i])
        dy.append(dy[i]+h*d2y[i])
        d2y.append(d2y[i] + h * func(x[i], y[i], dy[i], d2y[i]))
        y[i+1] = y[i] + (h/2.0) * (dy[i] + dy[i+1]);
        dy[i+1] = dy[i] + (h/2.0) * (d2y[i] + d2y[i+1]);
        d2y[i+1] = d2y[i] + (h/2.0) * (func(x[i], y[i], dy[i], d2y[i]) + func(x[i+1], y[i+1], dy[i+1], d2y[i+1]))
        
    return(x,y,dy,d2y)

O=main()
fig1, ax=plt.subplots()
plt.title('Графики y(x) и dy(x) при методе Адамса') 
ax.plot(O[0],O[1],color='red',label='y')
ax.plot(O[0],O[2],color='black',label='dy') 
plt.grid()
ax.legend(fontsize=15)


fig2, ax1=plt.subplots()
plt.title('График фазовых траекторий при методе Адамса')
ax1.plot(O[1],O[2])
plt.grid()



def f(z, x):
    z1, z2, z3 = z
    return [z2, z3, math.sin(x) + 5.0*z3 - 4.0*z2 + 4.0*z1]

x = np.linspace(0.0, 2.0, len(O[0]))
y0 = [1.0, 0.0, 0.0]

sol = scipy.integrate.odeint(f, y0, x)


fig3,ax2=plt.subplots()
plt.title('Графики y(x) и dy(x) при помощи встроенных функций') 
ax2.plot(x, sol[:, 1], 'black', label='d_y')
ax2.plot(x, sol[:, 0], 'red', label='y')
ax2.legend(fontsize=15)
plt.grid()

fig4, ax3=plt.subplots()
plt.title('График фазовых траекторий при помощи встроенных функций')
ax3.plot(sol[:, 0],sol[:, 1])
plt.grid()

fig5, ax4=plt.subplots()
plt.title('Расзностные графики')
ax4.plot(x,O[1]-sol[:,0],color='red',label='y')
ax4.plot(x,O[2]-sol[:,1],color='black',label='dy')
ax4.legend(fontsize=15)
plt.grid()






    
    