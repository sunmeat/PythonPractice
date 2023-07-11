# def Sum(a,b):
#     return a+b
#     print("Hello")
#4.	Написать функцию, реализующую алгоритм линейного поиска заданного ключа в одномерном массиве.

def LinerSearch(arr,a):
    for i in range(len(arr)):
        if arr[i] == a:
            return i
    return -1    
    
def main():
    # Rez = Sum(1,2) + Sum(3,4)
    # print(Rez)
    arr=[1,2,3,4,-5,-6,3,-9]
    i = LinerSearch(arr,30)
    if i>=0:
        print(f'Интекс найденного значения = {i}')
    else:
        print(f'Значение отсутствует в массиве')

main()