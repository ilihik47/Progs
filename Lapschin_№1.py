# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:08:50 2021

@author: Ilya Lapschin
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import pylab 
a=[]
M2=[]
i=-2
e=10**(-16) # ошибка машины
pi=math.pi
#найдем максимальное значение второй производной
#вторая производная от арктангенса имеет вид: y=(-2x)/(1+x^2)^2
while i<=2:
    M2.append((-2*i/1+i**2)**2)
    i=i+0.1
m2=np.max(M2) # максимум второй производной
#найдем оптимальный шаг
h=2*(((pi/2)*e)/m2)**0.5
#зададим массив, который будет содержать координату х у точек на графиках
x=np.linspace(-4,4,100)
    #вычислим значение функции F(x) в точках найденных ранее
k=0
F1=[]
while k< len(x):
    c=x[k]+h
    F1.append(math.atan(c))
    k=k+1
k=0
F2=[]
while k< len(x):
    c=x[k]-h
    F2.append(math.atan(c))
    k=k+1  
f=[] #точечные значения производной
k=0
#вычислим численно значение производной f(x)
while k<len(F1):
    c=((F1[k]-F2[k])/(2*h))    
    f.append(c)
    k=k+1

#теперь посччитаем значения производной, подставляя Х-ы в уравнение производной
#выведенное аналитически: y=1/(1+x^2)
fa=[]
k=0
while k<len(x):
    c=1/(1+x[k]**2)
    fa.append(c)
    k=k+1
    
fig, ax = plt.subplots()
ax.plot(x,f,color='red',label='численный метод')
ax.scatter(x,fa,color='black',marker='.',label='аналитический метод')
plt.legend(loc='upper left', prop={'size':8})

#разностный график
k=0
ff=[]
while k<len(f):
    ff.append(f[k]-fa[k])
    k=k+1
fig2, aa = plt.subplots()
aa.plot(x,ff,color='red',label='численный метод')

    