from colorama import init, Fore
import os

# Инициализация модуля colorama
init()
print(Fore.RED)

width = 21
height = 11
y = 0
while y < height:
    x = 0
    while x < width:
        if x == 0 or x == width - 1 or y == 0 or y == height - 1 or x == y * 2:
            print("#", end = '')
        else:
            print(" ", end = '')
        x += 1
    y += 1
    print()

################################################################################

print(Fore.GREEN)

y = 0
while y < height:
    x = 0
    while x < width: # пример как разбить условие на несколько строк
        if x == 0 and y < height / 2 or \
            x == width - 1 and y > height / 2 \
            or y == 0 and x < width / 2 \
            or y == height - 1 and x > width / 2 \
            or x == y * 2:
            print("#", end = '')
        else:
            print(" ", end = '')
        x += 1
    y += 1
    print()

################################################################################

os.system('cls' if os.name == 'nt' else 'clear') # Очистить консоль
print(Fore.BLUE)

y = 0
while y < height:
    x = 0
    while x < width:
        if x == 0 or x == width - 1 or y == 0 or y == height - 1 or x > y * 2:
            print("#", end = '')
        else:
            print(" ", end = '')
        x += 1
    y += 1
    print()