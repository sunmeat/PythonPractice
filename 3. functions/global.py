a=10  #глобальная переменная 
def Func1():
    a=1 # локальная переменная !!!
    print(f"Func1 a = {a}") # вывод локальной переменной а=1

def Func2():
    global a
    a=1
    print("Func2")

def main():    
#Func1()
 Func2()
 print(f"main a = {a}") # вывод глобальной переменной а=1


main()