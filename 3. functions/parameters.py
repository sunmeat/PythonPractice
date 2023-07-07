# функция, у которой аргументы со значением по умолчанию (справа налево, всё как обычно):
def print_odd_numbers(start = 1, end = 5):
    for number in range(start, end + 1, 2):
        if number % 2:
            print(number, end = ' ')
    print()

###############################################################################################

# функция, у которой все аргументы строго именованные (обратиться можно только по имени):
def display_line(*, length, direction, symbol):
    if direction == "горизонтально" or direction == True:
        print(symbol * length)
    else:
        for _ in range(length):
            print(symbol)

###############################################################################################

# функция, у которой один аргумент строго позиционный - первый, что до слеша (обратиться можно только по порядку, а не по имени):
# что интересно, Position-only argument separator not allowed as first parameter
def find_max(a, /, b, c, d):
    print("Максимальное число:", max(a, b, c, d), end = '\n')

###############################################################################################

# можно сделать так, что первый параметр будет строго позиционный, а второй - строго именованный:
def calculate_sum(start, /, *, end):
    print("Сумма чисел в диапазоне:", sum(range(start, end + 1)))

###############################################################################################

# пример функции с неограниченным количеством аргументов:
def summa(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"summa = {result}")
 
###############################################################################################

def main():

    print_odd_numbers(start = 1, end = 10) # так как есть значения по умолчанию, то можно передать от 0 до 2 параметров
    print_odd_numbers(start = 1)
    print_odd_numbers()

    # display_line(10, "горизонтально", '@') # TypeError: display_line() takes 0 positional arguments but 3 were given
    display_line(length = 10, direction = "горизонтально", symbol = '@') # теперь ок
    
    find_max(10, c = 40, d = 20, b = 30)
    # find_max(d=10, c=40, b=20, a=30) # TypeError: find_max() got some positional-only arguments passed as keyword arguments: 'a'

    summa(1, 2, 3, 4, 5)      # sum = 15
    summa(3, 4, 5, 6)         # sum = 18

    calculate_sum(1, end = 10)
    
main()