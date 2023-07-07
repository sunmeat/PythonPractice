
def Sum(a,b):
    print(f'{a} + {b} = {a+b}')

def Mult(a,b):
    print(f'{a} x {b} = {a*b}')

def Min(a,b):
    print(f'{a} - {b} = {a-b}')

def Div(a,b):
    if b!=0:
       print(f'{a} / {b} = {a/b}')
    else:
       print('На 0 делить нельзя !!!')

###-----------------------------------------------
def main():
    a = int(input("Введите левый операнд: "))
    znak = input("Введите оператор: ")
    b = int(input("Введите правый операнд: "))

    match znak:
     case "+":
        Sum(a,b)
     case "-":
        Min(a,b)
     case "*":
        Mult(a,b)
     case "/":
        Div(a,b)
     case _:
        print("error!!!")



main()


