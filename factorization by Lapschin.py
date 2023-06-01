from datetime import datetime #расчет времени выполнения программы
st=datetime.now() #начало отсчета времени
import pickle
import math
# найти факторизацию числа 
print('Введите число')
x=int(input())
def fact(x):
    s=[]
    i=0
    ff=open('erat.data','rb')
    pp=pickle.load(ff)
    while i<=len(pp)-1:
        if x%pp[i]==0:
            s.append(pp[i])
        i=i+1
    return s

print(fact(x))
ed=datetime.now() #конец расчета времени
print("Время выполнения программы:",ed-st)