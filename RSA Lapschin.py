"""
RSA шифрование
на вход: текстовый файл
на выход: текст в зашифрованном виде(последовательность цифр и после его расшифровка(в панель) 

Метод генерации RSA:
    В шифровании используются два простых числа, необходимые для вычисления Функции Эйлера(e=(q-1)*(p-1))/
    Также необходимо вычислить произведение этих простых чисел. Результат произведения понадобится, для создания ключей.
    n=p*q.
    Далее выбирается открытая экспонента(Е). Обычно это простое число, двоичное разлоение которых, содержит только две единицы. 
    Вычисляется закрытая экспонента(D).
    Создаются два ключа: открытый и закрытый. Открытый ключ публикуется, а закрытый остается у вас( ну или у вашего собеседника, которому вы отправили зашифрованный текст) 
    С помощью открытого ключа файл шифруется, а с помощью закрытого - дешифруется.
Автор: Лапшин И.В. 
"""
import random
from datetime import datetime
start_time=datetime.now()
#функция перевода в двоичный код
def encode(s):
    return list(map(lambda x: "{0:b}".format(ord(x)).zfill(16), s))

#функция перевода из двоичного кода
def decode(lst):
    return ''.join(map(lambda x: chr(int(x,2)), lst))

#Функция находит НОК(a,b) и раскладывает на ax + by = gcd(a,b)
def Advenced_Evklid(a,b):
    U = [ a , 1 , 0]
    V = [ b , 0 , 1]
    T = []
    while V[0] != 0:
        q = U[0] // V[0]
        T = [ U[0] % V[0], U[1] - q * V[1], U[2] - q * V[2]]
        U = V
        V = T
    return U    

#функция генерирует простое число в 100 знаков по методу Миллера Рабина
def generation():
    q = random.randint(0.5 * (10 ** 99) , 5 * (10 ** 99) )
    a = random.randint(2, 2 * q )
    while pow(a, q, 2*q + 1 ) != 1:
        q = random.randint(0.5 * (10 ** 99) , 5 * (10 ** 99))
    if len(str(q)) != 100:
        return generation()
    return 2*q + 1

#функция создания РАЗНЫХ простых чисел 
def creat_q_and_p():
    SN1 = generation()
    SN2 = generation()
    while SN1 == SN2:
        SN1 = generation()
    return [SN1, SN2]    

QP = creat_q_and_p()
q = QP[0] #простое
p = QP[1] #простое

n = (p * q) #вычисление произведения простых чисел
e = (p-1)*(q-1) #функция Эйлера

E = 65537 #открытая экспонента

D = Advenced_Evklid(E,e)[1] #Закрытая экспонента

Open_Key = {E,n} #открытый ключ
Close_Key = {D,n} #закртытый ключ

st=datetime.now()

#тестовый текст
file= []
f = open(r'E:\\progs\\progs.txt' ,'r', encoding="utf-8")  
for line in f: 
    file.append(line)
    
#print(file)

S1 = []
#находим зашифрованный текст в виде последовательности цифр
for j in range(len(file)):
    M = encode(file[j])
    i = 0
    for i in range(len(M)):
        S = pow(int(M[i]),E,n)
        S1.append(S)
print()        
print("Зашифрованный текст в виде чисел", S1)
print()

et=datetime.now()

stt=datetime.now()

#находим исходный текст путем дешифрации 
i = 0
j = 0
m2 = [] 
for i in range(len(S1)):
    M1 = str((pow(S1[i],D,n)))        
    if len(M1) < 16:
        M1 = '0' * (16 - len(M1)) + M1
        m2.append(M1)     
    M2 = decode(m2)
print()    
print('Расшифрованный текст (должен быть такойже как и исходный)')   
print()
print(M2)
edt=datetime.now()

end_time=datetime.now()
print()
print('Время выполнения шифрования:',format(et-st))
print()
print('Время выполнения дешифрования:',format(edt-stt))
print()
print('Время выполнения полной программы:',format(end_time-start_time))