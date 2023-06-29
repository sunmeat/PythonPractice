# Задание 1

# Пользователь вводит с клавиатуры три числа.
# В зависимости от выбора пользователя программа выводит на экран
# сумму трёх чисел или произведение трёх чисел.

# Считываем три числа с клавиатуры
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

# Выводим меню выбора операции
print("Выберите операцию:")
print("1. Сумма")
print("2. Произведение")
choice = int(input("Введите номер операции: "))

# Выполняем выбранную операцию и выводим результат
if choice == 1:
    result = num1 + num2 + num3
    print("Сумма чисел:", result)
elif choice == 2:
    result = num1 * num2 * num3
    print("Произведение чисел:", result)
else:
    print("Некорректный выбор операции")

########################################################################################

# Задание 3 (второе не делал :))

# Пользователь вводит с клавиатуры количество метров.
# В зависимости от выбора пользователя программа переводит метры
# в мили, дюймы или ярды.

# Считываем количество метров с клавиатуры
meters = float(input("Введите количество метров: "))

# Выводим меню выбора единицы измерения
print("Выберите единицу измерения:")
print("1. Мили")
print("2. Дюймы")
print("3. Ярды")
choice = int(input("Введите номер единицы измерения: "))

# Выполняем выбранный перевод и выводим результат
if choice == 1:
    miles = meters / 1609.34
    print("Количество миль:", miles)
elif choice == 2:
    inches = meters * 39.37
    print("Количество дюймов:", inches)
elif choice == 3:
    yards = meters * 1.09361
    print("Количество ярдов:", yards)
else:
    print("Некорректный выбор единицы измерения")

########################################################################################

# Задание 3

# Пользователь вводит с клавиатуры номер дня недели (1-7).
# Необходимо вывести на экран названия дня недели.
# Например, если 1, то на экране надпись понедельник, 2 — вторник и т.д.

# Считываем номер дня недели с клавиатуры
day_number = int(input("Введите номер дня недели (1-7): "))

# Проверяем введенное значение и выводим название дня недели
if day_number == 1:
    print("Понедельник")
elif day_number == 2:
    print("Вторник")
elif day_number == 3:
    print("Среда")
elif day_number == 4:
    print("Четверг")
elif day_number == 5:
    print("Пятница")
elif day_number == 6:
    print("Суббота")
elif day_number == 7:
    print("Воскресенье")
else:
    print("Некорректный номер дня недели")

########################################################################################

# Потом стало интересно, как сделать это на массиве :)

# Создаем массив с названиями дней недели
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

# Считываем номер дня недели с клавиатуры
day_number = int(input("Введите номер дня недели (1-7): "))

# Проверяем введенное значение и выводим название дня недели
if day_number >= 1 and day_number <= 7:
    day_name = days_of_week[day_number - 1]
    print(day_name)
else:
    print("Некорректный номер дня недели")

########################################################################################

# Задание 4

# Пользователь вводит с клавиатуры число. Необходимо проверить его на четность
# и нечетность. Если число четное требуется вывести на экран число и надпись
# Even number. Если число нечетное выведите на экран число и надпись Odd number.

# Считываем число с клавиатуры
number = int(input("Введите число: "))

# Проверяем четность числа и выводим результат
if number % 2 == 0:
    print(number, "Even number")
else:
    print(number, "Odd number")

########################################################################################

# Задание 5

# Пользователь вводит с клавиатуры два числа.
# Необходимо найти максимум из двух чисел и показать его на экран.

# Ввод чисел с клавиатуры
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

# Нахождение максимума
maximum = max(number1, number2) # ну ифом понятно, как сделать :)

# Вывод результата
print("Максимум из двух чисел:", maximum)

########################################################################################

# Задание 6

# Пользователь вводит с клавиатуры время в секундах, прошедшее с начала дня.
# В зависимости от выбора пользователя посчитать, сколько часов, минут и секунд
# осталось до полуночи.

# Ввод времени в секундах
time_seconds = int(input("Введите время в секундах: "))

print("Выберите вариант расcчёта:")
print("1. Осталось до полуночи в секундах.")
print("2. Осталось до полуночи в минутах.")
print("3. Осталось до полуночи в часах.")
choice = int(input("Введите номер варианта: "))

# Расчет времени
remaining_seconds = 24 * 60 * 60 - time_seconds

if choice == 2:
    remaining_minutes = remaining_seconds // 60
    print("Осталось до полуночи в минутах:", remaining_minutes)
elif choice == 3:
    remaining_hours = remaining_seconds // 3600
    print("Осталось до полуночи в часах:", remaining_hours)
else:
    print("Осталось до полуночи в секундах:", remaining_seconds)

########################################################################################

# Задание 7

# Пользователь вводит с клавиатуры размер файла в гигабайтах и скорость
# интернет-соединения в битах в секунду. В зависимости от выбора пользователя
# посчитать, за сколько часов или минут, или секунд скачается файл.

file_size_gb = float(input("Введите размер файла в гигабайтах: "))
internet_speed_bps = float(input("Введите скорость интернет-соединения в битах в секунду: "))

print("Выберите вариант расчета:")
print("1. Время скачивания файла в секундах.")
print("2. Время скачивания файла в минутах.")
print("3. Время скачивания файла в часах.")
choice = int(input("Введите номер варианта: "))

# Рассчёт времени
file_size_bits = file_size_gb * 8 * 1024 * 1024 * 1024
download_time_seconds = file_size_bits / internet_speed_bps

if choice == 2:
    download_time_minutes = download_time_seconds / 60
    print("Время скачивания файла в минутах:", download_time_minutes)
elif choice == 3:
    download_time_hours = download_time_seconds / 3600
    print("Время скачивания файла в часах:", download_time_hours)
else:
    print("Время скачивания файла в секундах:", download_time_seconds)