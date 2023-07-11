a=1
b=4
def Sum(): # функция использует глобальные переменные!!! так нельзя!!
    global a
    global b
    print(a+b)

def Sum2(a,b): # функция использует локальные параметры!!! автономная функция 
    print(a+b)

def Mult(a,b):
    print(a*b)

def Min(a,b):
    print(a-b)

Sum2(12,4)
Mult(12,4)

