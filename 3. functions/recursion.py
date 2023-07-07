# Задание 1

# Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел.

def nod(a, b):
    if b == 0:
        return a
    return nod(b, a % b)

# используется алгоритм Евклида для нахождения НОД.
# если одно из чисел равно 0, то НОД равен другому числу.
# в противном случае, функция рекурсивно вызывает себя, передавая в качестве
# аргументов второе число и остаток от деления первого числа на второе число.

#################################################################################################

# Задание 2

# Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное число и играющий должен
# угадать его. После ввода пользователем числа программа сообщает, сколько цифр числа угадано
# (быки) и сколько цифр угадано и стоит на нужном месте (коровы). После отгадывания числа на
# экран необходимо вывести количество сделанных пользователем попыток. В программе необходимо
# использовать рекурсию.

import random

def bulls_and_cows(secret_number, attempts):
    guess = input("Введите четырёхзначное число: ")
    
    if guess == secret_number:
        print("Поздравляем, вы угадали число!")
        print("Количество попыток:", attempts)
        return
    
    bulls = 0
    cows = 0
    
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    
    print("Быки:", bulls)
    print("Коровы:", cows)
    print("Попробуйте ещё раз.")
    
    attempts += 1
    bulls_and_cows(secret_number, attempts)

#################################################################################################

# Задание 3

# Дана шахматная доска размером 8×8 и шахматный конь. Программа должна запросить у пользователя
# координаты клетки поля и поставить туда коня. Задача программы найти и вывести путь коня,
# при котором он обойдет все клетки доски, становясь в каждую клетку.
# только один раз. (Так как процесс отыскания пути для разных начальных клеток может затянуться,
# то рекомендуется сначала опробовать задачу на поле размером 6×6). В программе необходимо
# использовать рекурсию.

def is_valid_move(board, row, col):
    # проверка, что клетка находится внутри доски
    if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]):
        # проверка, что клетка не посещена
        return board[row][col] == 0
    return False

def pony(board, row, col, move_count):
    # установка текущей клетки как посещенной
    board[row][col] = move_count
    
    # если все клетки посещены, выводим путь коня
    if move_count == len(board) * len(board[0]):
        print("Путь коня:")
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], end = "\t")
            print("\n")
        return True
    
    # возможные варианты ходов коня
    row_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    col_moves = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # перебор всех возможных ходов
    for i in range(8):
        next_row = row + row_moves[i]
        next_col = col + col_moves[i]
        
        if is_valid_move(board, next_row, next_col):
            # рекурсивный вызов для следующего хода
            if pony(board, next_row, next_col, move_count + 1):
                return True
    
    # если не удалось найти путь, снимаем отметку с клетки
    board[row][col] = 0
    return False

#################################################################################################

# Задание 4

# Написать игру «Пятнашки».

size = 4

def create_board():
    board = [[0] * size for _ in range(size)]
    numbers = random.sample(range(1, 16), 15)
    numbers.append(0)  # 0 - это пустая клетка
    k = 0
    for i in range(size):
        for j in range(size):
            board[i][j] = numbers[k]
            k += 1
    return board

def print_board(board):
    for i in range(size):
        for j in range(size):
            print(f'{board[i][j]:<3}', end = '') # спецификатор формата, указывает на выравнивание элемента слева и ширину поля вывода в 3 символа
        print()
    print()

def get_blank_position(board):
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                return i, j

def is_valid_move(move):
    return move in ['w', 's', 'a', 'd']

def make_move(board, move):
    blank_row, blank_col = get_blank_position(board)
    row, col = blank_row, blank_col

    if move == 'w':  # up
        row -= 1
    elif move == 's':  # down
        row += 1
    elif move == 'a':  # left
        col -= 1
    elif move == 'd':  # right
        col += 1
    if row < 0 or row >= size or col < 0 or col >= size:
        return False
    
    board[blank_row][blank_col] = board[row][col]
    board[row][col] = 0
    return True

def is_solved(board):
    numbers = []
    for i in range(4):
        for j in range(4):
            numbers.append(board[i][j])
    return numbers == list(range(1, size * size))

def fifteen():
    board = create_board()
    print("Добро пожаловать в игру Пятнашки!")
    print_board(board)
    
    while True:
        move = input("Введите направление (w - вверх, s - вниз, a - влево, d - вправо): ")
        if not is_valid_move(move):
            print("Некорректное направление! Попробуйте ещё раз.")
            continue
        
        if make_move(board, move):
            print_board(board)
            
            if is_solved(board):
                print("Вы победили! Ура! :)")
                break
        else:
            print("Некорректный ход! Попробуйте еще раз.")

#################################################################################################

def main():

    # print(nod(125, 575)) # 25

    # ----------------------------------------------------------------------

    # генерация числа для быков и коров
    # secret_number = str(random.randint(1000, 9999))
    # print("Добро пожаловать в игру 'Быки и коровы'!")
    # print("Попробуйте угадать четырёхзначное число.")
    # bulls_and_cows(secret_number, 1) # Введите четырёхзначное число: 2151
    #                                  # Поздравляем, вы угадали число!
    #                                  # Количество попыток: 17

    # ----------------------------------------------------------------------

    # создание шахматной доски размером 6x6
    # size = 6
    # board = [[0] * size for _ in range(size)]
    # # ввод пользователем начальных координат
    # start_row = int(input("Введите начальную координату (номер строки, 0-%d): " % (size - 1)))
    # start_col = int(input("Введите начальную координату (номер столбца, 0-%d): " % (size - 1)))
    # # запуск поиска пути коня
    # pony(board, start_row, start_col, 1)

    # ----------------------------------------------------------------------

    fifteen()

main()