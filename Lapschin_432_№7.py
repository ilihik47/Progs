"Найти точкуминимума функции методом Ньютона-Рафсона. "
"Для одномерной минимизации использовать методквадратичной интерполяции. "
"Для поиска интервала унимодальности использовать алгоритм Свенна. "
"В окрестности точки минимума построить линии уровня и траекторию поиска. "

import numpy as np
import matplotlib.pyplot as plt

def func(x,y): #выдает значение функции в заданной точке
    f=x**3-3*x**2+y**2+4*y+9
    return f

def first_przv_x(x,y):
    f=3*x**2-6*x
    return f

def second_przv_x(x,y):
    f=6*x-6
    return f

def first_przv_y(x,y):
    f=2*y+4
    return f

def second_przv_y(x,y):
    return 2

def second_przv_xy(x,y):
    return 0

def ober_matr(c):
    det=c[0][0]*c[1][1]-c[0][1]*c[1][0]
    cc=c[0][0]
    c[0][0]=c[1][1]/det
    c[1][1]=cc/det
    cc=c[0][1]
    c[0][1]=-c[0][1]/det
    c[1][0]=-c[1][0]/det
    
def proizv(gessian,grad,p):
    p0=gessian[0][0]*grad[0]+gessian[0][1]*grad[1]
    p1=gessian[1][0]*grad[0]+gessian[1][1]*grad[1]
    return p0, p1 
    
def swenn_x(h,a,y):
    a[1]=a[0]+h
    if func(a[1],y)>func(a[0],y):
        h=-h
        a[1]=a[0]+h
    while func(a[1],y)<func(a[0],y):
        a[0]=a[1]
        a[1]=a[0]+h
        h=h*2     


def swenn_y(h,b,x):
    b[1]=b[0]+h
    if func(x,b[1])>func(x,b[0]):
        h=-h
        b[1]=b[0]+h
    while func(x,b[1])<func(x,b[0]):
        b[0]=b[1]
        b[1]=b[0]+h
        h=h*2

    
def alfa_x(alfa,a0,a1,y_const,p,x_const):
    x_min=0
    if a1<a0:
        c=a1
        a1=a0
        a0=c
    dx=0.01
    e=0.001
    x1=a0
    ff=True
    while ff==True:
        x2=x1+dx
        f1=func(x1,y_const)
        f2=func(x2,y_const)
        if f1>f2:
            x3=x1+2*dx
        else:   
            x3=x1-dx
        f3=func(x3,y_const)
        f_min=min(f1,f2)
        f_min=min(f_min,f3)
        if f_min==f1: 
            x_min=x1
        else:
            if f_min==f2: 
                x_min=x2
            else:                
                if f_min==f3: 
                    x_min=x3
        x_=((x2 * x2 - x3 * x3) * f1 + (x3 * x3 - x1 * x1) * f2 + (x1 * x1 - x2 * x2) * f3) /(((x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3) * 2)
        f_=func(x_,y_const)
        if ((((x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3) * 2) == 0):
            x1=x_min
        if abs(f_min-f_)>=e or abs(x_min-x_) >=e:
            if x_<x1 or x_>x3:
                x1=x_
            else: 
                if x_>=x1 and x_<=x3:
                    F=min(f_min,f_)
                    if F==f_min:
                        x1=x_min
                    else:
                        if F==f_:
                            x1=x_
        ff=abs(f_min-f_)>=e and abs(x_min-x_)>=e
        alfa=x_



def alfa_y(alfa,b0,b1,y_const,p,x_const):
    y_min=0
    if b1<b0:
        c=b1
        b1=b0
        b0=c
    dy=0.01
    ee=0.0001
    y1=b0
    ff=True
    while ff==True:
        y2=y1+dy
        f1=func(x_const,y1)
        f2=func(x_const,y2)
        if f1>f2:
            y3=y1+2*dy
        else:   
            y3=y1-dy
        f3=func(x_const,y3)
        f_min=min(f1,f2)
        f_min=min(f_min,f3)
        if f_min==f1: y_min=y1
        if f_min==f2: y_min=y2
        if f_min==f3: y_min=y3
        y_=((y2 * y2 - y3 * y3) * f1 + (y3 * y3 - y1 * y1) * f2 + (y1 * y1 - y2 * y2) * f3) /(((y2 - y3) * f1 + (y3 - y1) * f2 + (y1 - y2) * f3) * 2)
        f_=func(x_const,y_)
        if ((((y2 - y3) * f1 + (y3 - y1) * f2 + (y1 - y2) * f3) * 2) == 0):
            y1=y_min
            continue
        if abs(f_min-f_)>=ee or abs(y_min-y_) >=ee:
            if y_<y1 or y_>y3:
                y1=y_
                continue
            else: 
                if y_>=y1 and y_<=y3:
                    F=min(f_min,f_)
                    if F==f_min:
                        y1=y_min
                        continue
                    else:
                        if F==f_:
                            y1=y_
                            continue
        ff=abs(f_min-f_)>=ee and abs(y_min-y_)>=ee
        alfa=y_

    

def main():
    alfa1=0
    alfa2=0
    p=[0,0]
    a=[0,0]
    b=[0,0]
    count=0
    gessian=np.zeros((2,2))
    grad=np.zeros(2)
    alfa=1
    h=0.1
    X=[]
    Y=[]
    X.append(1.5)
    Y.append(5)
    x=X[0]
    y=Y[0]
    
    gessian[0][0]=second_przv_x(x,y)
    gessian[0][1]=second_przv_xy(x,y)
    gessian[1][0]=gessian[0][1]
    gessian[1][1]=second_przv_y(x,y)
    
    ober_matr(gessian)
    
    grad[0]=first_przv_x(x,y)
    grad[1]=first_przv_y(x,y)
    
    det_grad=(grad[0]*grad[0]+grad[1]*grad[1])**(1/2)
    
    p=proizv(gessian,grad,p)
    e=0.25
    u=0.5
    proizv_grad_p=first_przv_x(x,y)*p[0]+first_przv_y(x,y)*p[1]
    f1=func(x+alfa*p[0],y+alfa*p[1])
    f2=func(x,y)+e*alfa*proizv_grad_p
    
    while det_grad>0.0001:
        alfa=1
        h=0.1
        a[0]=x
        b[0]=y
        swenn_x(h,a,y)
        swenn_y(h,b,x) 
        gessian[0][0]=second_przv_x(x,y)
        gessian[0][1]=second_przv_xy(x,y)
        gessian[1][0]=gessian[0][1]
        gessian[1][1]=second_przv_y(x,y)

        ober_matr(gessian)
        
        grad[0]=first_przv_x(x,y)
        grad[1]=first_przv_y(x,y)
        
        det_grad=(grad[0]*grad[0]+grad[1]*grad[1])**(1/2)
        
        p=proizv(gessian,grad,p)
        
        
        
        while(f1>f2):
            alfa=alfa*u
            f1=func(x+alfa*p[0],y+alfa*p[1])
            f2=func(x,y)+e*alfa*proizv_grad_p
            break
        
        a0=a[0]
        a1=a[1]
        alfa_x(alfa1,a0,a1,y,p,x)
        x11=x-alfa*p[0]
        
        
        b0=b[0]
        b1=b[1]
        alfa_y(alfa2,b0,b1,y,p,x)
        y22=y-alfa*p[1]
        ff=y22-y22==0
        if ff==False:
            break
        x=x11
        y=y22
        
        X.append(x11)
        Y.append(y22)
        
        count=count+1
        
    return X, Y, count

d1=main()[0]
d2=main()[1]
d3=main()[2]

print('_________________________________________________')
print('Координаты искомой точки:','[',d1[d3],',',d2[d3],']')
print('Количество итерраций:',d3)

xx=main()[0]
yy=main()[1]
x=np.arange(-5,5,0.01)
y=np.arange(-3,5,0.01)
X,Y=np.meshgrid(x,y)
z=X**3-3*X**2+Y**2+4*Y+9
plt.grid()
plt.contour(X,Y,z,levels = 5)
plt.plot(xx,yy,'o',xx,yy,color='red')
plt.show()















