import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#открываем файл и заносим значения в двумерный массив
with open('08_Красноярск.csv','r') as f:    
        content=csv.reader(f,delimiter=',')
        content = list(content)
        ff=np.array(content[1:][:],dtype=float)
        
#print('введите исследуемый месяц (от 1 до 12)')
#k=int(input())
#print('введите первую исследуемую строчку из 12(от 0 до 170)')
#uio=int(input())
t=0.1 #шаг по сетке Х
k=6
uio=60
'                             ПЕРВОЕ ЗАДАНИЕ                      '

def first(): #функция для интерполяции Лагранжа
    i=uio 
    def y12(k,i): # столбец состоящий из 12 строчек
        st=[]
        j=i
        while j<i+12:
            st.append(ff[j,k])
            j=j+1
        return st
    def x12(i): # номера этих 12 строчек 
        x=[]
        j=i
        while j<i+12:
            x.append(j)
            j=j+1
        return x
    
    
    y1=y12(k, i)
    x1=x12(i)
    
    # выброс недостоверных данных
    c=0
    y=[]
    x=[]
    while c<12:
        if y1[c]!=999.9:
            y.append(y1[c])
            x.append(x1[c])
        c=c+1
    
    print('x12:',x)
    print('y12:',y)
    #функция, считает значение полинома в определенной точке
    def lagranz(peremen):
             Px=0
             for j in range(len(y)):
                 l1=1; l2=1
                 for i in range(len(x)):
                     if i==j:
                         l1=l1*1; l2=l2*1   
                     else: 
                         l1=l1*(peremen-x[i])
                         l2=l2*(x[j]-x[i])
                 Px=Px+y[j]*l1/l2
             return Px
    #цикл, считающий значения полинома в точках Х с указанным шагом t     
    x1=[]
    y1=[]
    if len(x)>0:
        l=x[0]
        while l<x[len(x)-1]+0.1:
            x1.append(l)
            y1.append(lagranz(l))
            l=l+t
                
        #построение графика
        fig, ax = plt.subplots()
        ax.plot(x1,y1,'.',color='black') #выделение значений, полученных при интерполяции
        ax.plot(x,y,'o',x1,y1,color='#8B008B') #исходные точки, и график через точки интерполяции
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) #шаг основной сетки
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1)) #шаг дополнительной сетки
        ax.grid(which='major',color = 'black') #цвет основной сетки
        ax.grid(which='minor',color = 'gray',linestyle = ':') #цвет и вид дополнительной сетки
        plt.title("ПОЛИНОМ ЛАГРАНЖА")
        plt.grid(True)
        plt.show()
    else:
        print('на данном отрезке[',uio,',',uio+11,' нет достоверных значений')
    
    
    
'                                       ЗАДАНИЕ ВТОРОЕ                      '
def second():
    i=uio
    def y6(k,i): # столбец состоящий из 6 строчек
        st=[]
        j=i
        while j<i+6:
            st.append(ff[j,k])
            j=j+1
        return st
    def x6(i): #номера первых 6 строчек
        x=[]
        j=i
        while j<i+6:
            x.append(j)
            j=j+1
        return x
        
    Y=y6(k,i)
    X=x6(i)
    # выброс недостоверных данных    
    c=0
    y=[]
    x=[]
    while c<6:
        if Y[c]!=999.9:
            y.append(Y[c])
            x.append(X[c])
        c=c+1
    print('x6(1):',x)
    print('y6(1):',y)
    #считаем разделенные разности    
    d1=[]
    for i in range(len(y)):
        if i==len(y)-1:
            break
        else:
            d1.append(y[i+1]-y[i])
                
    d2=[]
    for i in range(len(d1)):
        if i==len(d1)-1:
            break
        else:
            d2.append((d1[i+1]-d1[i])/2)
                
    d3=[]
    for i in range(len(d2)):
        if i==len(d2)-1:    
            break
        else:
            d3.append((d2[i+1]-d2[i])/3)
        
    d4=[]
    for i in range(len(d3)):
        if i==len(d3)-1:
            break
        else:
            d4.append((d3[i+1]-d3[i])/4)
                
    d5=[]
    for i in range(len(d4)):
        if i==len(d4)-1:
            break
        else:
            d5.append((d4[i+1]-d4[i])/5)
    #выбор разностей нужного порядка (нулевого)
    if len(d1)>0:
        d1=d1[0]
    else:
        d1=0
    
    if len(d2)>0:
        d2=d2[0]
    else:
        d2=0
    
    if len(d3)>0:
        d3=d3[0]
    else:
        d3=0
    
    if len(d4)>0:
        d4=d4[0]
    else:
        d4=0
        
    if len(d5)>0:
        d5=d5[0]
    else:
        d5=0
    #функция, считает значение полинома в определенной точке 
    def firstnt(q):
        Px=y[0]+(q-x[0])*d1+(q-x[0])*(q-x[1])*d2+(q-x[0])*(q-x[1])*(q-x[2])*d3+(q-x[0])*(q-x[1])*(q-x[2])*(q-x[3])*d4+(q-x[0])*(q-x[1])*(q-x[2])*(q-x[3])*(q-x[4])*d5
        return Px
    #цикл, считающий значения полинома в точках Х с указанным шагом t     
    x1=[]
    y1=[]
    if len(x)>0:
        l=x[0]
        while l<x[len(x)-1]+0.1:
            x1.append(l)
            y1.append(firstnt(l))
            l=l+t
                
        #построение графика
        fig, ax = plt.subplots()
        ax.plot(x1,y1,'.',color='black') #выделение значений, полученных при интерполяции
        ax.plot(x,y,'o',x1,y1,color='#8B008B') #исходные точки, и график через точки интерполяции
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) #шаг основной сетки
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1)) #шаг дополнительной сетки
        ax.grid(which='major',color = 'black') #цвет основной сетки
        ax.grid(which='minor',color = 'gray',linestyle = ':') #цвет и вид дополнительной сетки
        plt.title("ПЕРВАЯ ИНТЕРПОЛЯЦИОННАЯ ФОРМУЛА НЬЮТОНА")
        plt.grid(True)
        plt.show()
    else:
        print('на данном отрезке[',uio,',',uio+5,' нет достоверных значений')
    
def third():
    i=uio+6
    def y6(k,i): # столбец состоящий из 6 строчек
        st=[]
        j=i
        while j<i+6:
            st.append(ff[j,k])
            j=j+1
        return st
    def x6(i): #номера последних 6 строчек
        x=[]
        j=i
        while j<i+6:
            x.append(j)
            j=j+1
        return x
        
    Y=y6(k,i)
    X=x6(i)
    # выброс недостоверных данных    
    c=0
    y=[]
    x=[]
    while c<6:
        if Y[c]!=999.9:
            y.append(Y[c])
            x.append(X[c])
        c=c+1
    print('x6(2):',x)
    print('y6(2):',y)
    #считаем разделенные разности    
    d1=[]
    for i in range(len(y)):
        if i==len(y)-1:
            break
        else:
            d1.append(y[i+1]-y[i])
                
    d2=[]
    for i in range(len(d1)):
        if i==len(d1)-1:
            break
        else:
            d2.append((d1[i+1]-d1[i])/2)
                
    d3=[]
    for i in range(len(d2)):
        if i==len(d2)-1:    
            break
        else:
            d3.append((d2[i+1]-d2[i])/3)
        
    d4=[]
    for i in range(len(d3)):
        if i==len(d3)-1:
            break
        else:
            d4.append((d3[i+1]-d3[i])/4)
                
    d5=[]
    for i in range(len(d4)):
        if i==len(d4)-1:
            break
        else:
            d5.append((d4[i+1]-d4[i])/5)
    #выбор разностей нужного порядка (последнего для каждой из разностей)
    if len(d1)>0:
        d1=d1[len(d1)-1]
    else:
        d1=0
    
    if len(d2)>0:
        d2=d2[len(d2)-1]
    else:
        d2=0
    
    if len(d3)>0:
        d3=d3[len(d3)-1]
    else:
        d3=0
    
    if len(d4)>0:
        d4=d4[len(d4)-1]
    else:
        d4=0
        
    if len(d5)>0:
        d5=d5[len(d5)-1]
    else:
        d5=0
    c=len(x)-1
    c1=len(y)-1
    #функция, считает значение полинома в определенной точке
    def secondnt(q):
        Px=y[c1]+(q-x[c])*d1+(q-x[c])*(q-x[c-1])*d2+(q-x[c])*(q-x[c-1])*(q-x[c-2])*d3+(q-x[c])*(q-x[c-1])*(q-x[c-2])*(q-x[c-3])*d4+(q-x[c])*(q-x[c-1])*(q-x[c-2])*(q-x[c-3])*(q-x[c-4])*d5
        return Px
    #цикл, считающий значения полинома в точках Х с указанным шагом t     
    x1=[]
    y1=[]
    if len(x)>0:
        l=x[0]
        while l<x[len(x)-1]+0.1:
            x1.append(l)
            y1.append(secondnt(l))
            l=l+t
                
        #построение графика
        fig, ax = plt.subplots()
        ax.plot(x1,y1,'.',color='black') #выделение значений, полученных при интерполяции
        ax.plot(x,y,'o',x1,y1,color='#8B008B') #исходные точки, и график через точки интерполяции
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) #шаг основной сетки
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1)) #шаг дополнительной сетки
        ax.grid(which='major',color = 'black') #цвет основной сетки
        ax.grid(which='minor',color = 'gray',linestyle = ':') #цвет и вид дополнительной сетки
        plt.title("ВТОРАЯ ИНТЕРПОЛЯЦИОННАЯ ФОРМУЛА НЬЮТОНА")
        plt.grid(True)
        plt.show()
    else:
        print('на данном отрезке[',uio+5,',',uio+11,' нет достоверных значений')
first()
second()
third()


