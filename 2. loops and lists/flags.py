import curses # работа с курсором в консоли
import os # для очистки экрана
from colorama import init, Fore

os.system('cls' if os.name == 'nt' else 'clear') 

count_of_flags = int(input("сколько нужно флагов (1-75)? "))

stdscr = curses.initscr() # инициализация экрана
curses.curs_set(0) # включение режима невидимого курсора75

# rows, cols = stdscr.getmaxyx() # получение размеров экрана

# os.system('cls' if os.name == 'nt' else 'clear') 

curses.start_color()
curses.use_default_colors()

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

x = 1
y = 1
flags_done = 0
pair_number = 1
for i in range(count_of_flags):
    
    stdscr.addstr(y + 0, x, "+____", curses.color_pair(pair_number)) # установка позиции курсора
    stdscr.addstr(y + 1, x, "|    /", curses.color_pair(pair_number)) 
    stdscr.addstr(y + 2, x, "|____\\", curses.color_pair(pair_number)) 
    stdscr.addstr(y + 3, x, "|", curses.color_pair(pair_number)) 

    stdscr.addstr(y + 1, x + 2, str(i + 1), curses.color_pair(pair_number)) 
    x += 8
    flags_done += 1
   
    if (flags_done % 15 == 0):
        x = 1
        y += 5

    pair_number += 1
    if (pair_number > 7):
        pair_number = 1

stdscr.getch() # ожидание ввода пользователя (иначе всё исчезает)
# curses.endwin() # завершение работы с экраном

# такая версия была в начале... но это скучно :)
# count_of_flags = int(input("сколько нужно флагов?"))
# for i in range(count_of_flags):
#     print("+___")
#     print("|   /")
#     print("|___\\")
#     print("|   ")