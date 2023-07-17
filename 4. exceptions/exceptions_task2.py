# Задание 1
# Напишите программу, которая запрашивает у пользователя число и вычисляет
# его факториал. Обработайте исключение, возникающее при вводе отрицательного
# числа, и выведите сообщение об ошибке. 

# def factorial(n): # рекурсивная версия (получилось автоматически)))
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# try:
#     num = int(input("Введите положительное число для вычисления факториала: "))
#     if num < 0:
#         raise ValueError("Отрицательное число не имеет факториала!")
#     result = factorial(num)
#     print(f"Факториал числа {num} равен {result}")
# except ValueError as e:
#     print(e)

###########################################################################

# Задание 2
# Реализуйте первое задание через функцию. Функция должна принимать число
# в качестве параметра и возвращать его факториал. Проверка корректности,
# полученных данных должна быть внутри функции. Создайте две версии реализации
# функции:
# Первая версия не обрабатывает исключение внутри функции. Вся обработка
# находится снаружи;
# Вторая версия обрабатывает исключение внутри функции.

# def factorial(num):
#     if num < 0:
#         raise ValueError("Отрицательное число не имеет факториала!")
#     result = 1
#     for i in range(1, num + 1): # итеративная версия факториала
#         result *= i
#     return result

# # без обработки исключения внутри функции
# try:
#     num = int(input("Введите число для вычисления факториала: "))
#     result = factorial(num)
#     print(f"Факториал числа {num} равен {result}")
# except ValueError as e:
#     print(e)

###########################################################################

# def factorial(num):
#     try:
#         if num < 0:
#             raise ValueError("Отрицательное число не имеет факториала!")
#         result = 1
#         for i in range(1, num + 1):  # итеративная версия
#             result *= i
#         return result
#     except ValueError as e:
#         print(e)

# num = int(input("Введите число для вычисления факториала: "))
# result = factorial(num)
# if result is not None: # числовой результат может и не вернуться
#     print(f"Факториал числа {num} равен {result}")

###########################################################################

# Задание 3
# Напишите программу, которая позволяет заполнить пользователю список
# с клавиатуры числами. После получения данных отобразите на экран меню,
# которое позволяет выполнить следующие операции:
# Отображение списка;
# Получение максимального значения в списке;
# Получение минимального значения в списке;
# Отображение значения элемента по индексу, введённому пользователем;
# Удаление элемента по индексу, введенному пользователем.
# Обработайте исключение, возникающее при выходе за пределы списка
# (пользователь ввел неверное значение для индекса элемента в списке),
# и выведите сообщение об ошибке. 

# numbers = []

# while True:
#     try:
#         choice = int(input("Меню:\n\
# 1. Добавить число в список\n\
# 2. Отображение списка\n\
# 3. Получение максимального значения\n\
# 4. Получение минимального значения\n\
# 5. Отображение значения элемента по индексу\n\
# 6. Удаление элемента по индексу\n\
# 0. Выход из программы\n\
# Выберите операцию (введите номер 0-6): "))
        
#         if choice == 0:
#             exit(0)
#         if choice == 1:
#             num = int(input("Введите число для добавления: "))
#             numbers.append(num)
#         elif choice == 2:
#             print("Список чисел:", numbers)
#         elif choice == 3:
#             if numbers:
#                 print("Максимальное значение:", max(numbers))
#             else:
#                 print("Список пуст!")
#         elif choice == 4:
#             if numbers:
#                 print("Минимальное значение:", min(numbers))
#             else:
#                 print("Список пуст!")
#         elif choice == 5:
#             try:
#                 index = int(input("Введите индекс элемента: "))
#                 print("Значение по индексу", index, ":", numbers[index])
#             except IndexError:
#                 print("Ошибка: введён некорректный индекс!")
#         elif choice == 6:
#             try:
#                 index = int(input("Введите индекс элемента для удаления: "))
#                 del numbers[index]
#                 print("Элемент удалён!")
#             except IndexError:
#                 print("Ошибка: введен некорректный индекс!")
#         else:
#             print("Ошибка: некорректный выбор операции!")

#     except ValueError:
#         print("Ошибка: введено некорректное значение для операции!")

###########################################################################

# Задание 4
# Реализуйте третье задание через функции. Создайте две версии реализации функций:
# Первая версия не обрабатывает исключения внутри функций.
# Вся обработка находится снаружи;
# Вторая версия обрабатывает исключения внутри функций.

# def add_number(numbers, num):
#     numbers.append(num)

# def display_numbers(numbers):
#     print("Список чисел:", numbers)

# def get_max(numbers):
#     if numbers:
#         return max(numbers)
#     else:
#         raise ValueError("Список пуст!")

# def get_min(numbers):
#     if numbers:
#         return min(numbers)
#     else:
#         raise ValueError("Список пуст!")

# def display_element(numbers, index):
#     try:
#         return numbers[index]
#     except IndexError:
#         raise IndexError("Ошибка: введён некорректный индекс!")

# def delete_element(numbers, index):
#     try:
#         del numbers[index]
#         print("Элемент удалён!")
#     except IndexError:
#         raise IndexError("Ошибка: введён некорректный индекс!")

# def main():
#     numbers = []

#     while True:
#         try:
#             choice = int(input("Меню:\n\
# 1. Добавить число в список\n\
# 2. Отображение списка\n\
# 3. Получение максимального значения\n\
# 4. Получение минимального значения\n\
# 5. Отображение значения элемента по индексу\n\
# 6. Удаление элемента по индексу\n\
# 0. Выход из программы\n\
# Выберите операцию (введите номер 0-6): "))

#             if choice == 0:
#                 break
#             elif choice == 1:
#                 num = int(input("Введите число для добавления: "))
#                 add_number(numbers, num)
#             elif choice == 2:
#                 display_numbers(numbers)
#             elif choice == 3:
#                 try:
#                     max_value = get_max(numbers)
#                     print("Максимальное значение:", max_value)
#                 except ValueError as e:
#                     print(e)
#             elif choice == 4:
#                 try:
#                     min_value = get_min(numbers)
#                     print("Минимальное значение:", min_value)
#                 except ValueError as e:
#                     print(e)
#             elif choice == 5:
#                 try:
#                     index = int(input("Введите индекс элемента: "))
#                     element = display_element(numbers, index)
#                     print("Значение по индексу", index, ":", element)
#                 except IndexError as e:
#                     print(e)
#             elif choice == 6:
#                 try:
#                     index = int(input("Введите индекс элемента для удаления: "))
#                     delete_element(numbers, index)
#                 except IndexError as e:
#                     print(e)
#             else:
#                 print("Ошибка: некорректный выбор операции!")

#         except ValueError as e:
#             print(e)

# main()

###########################################################################

def add_number(numbers, num):
    try:
        numbers.append(num)
    except Exception as e:
        print("Ошибка при добавлении числа:", e)

def display_numbers(numbers):
    try:
        print("Список чисел:", numbers)
    except Exception as e:
        print("Ошибка при отображении списка:", e)

def get_max(numbers):
    try:
        if numbers:
            return max(numbers)
        else:
            raise ValueError("Список пуст!")
    except Exception as e:
        print("Ошибка при получении максимального значения:", e)

def get_min(numbers):
    try:
        if numbers:
            return min(numbers)
        else:
            raise ValueError("Список пуст!")
    except Exception as e:
        print("Ошибка при получении минимального значения:", e)

def display_element(numbers, index):
    try:
        return numbers[index]
    except IndexError as e:
        print("Ошибка: введён некорректный индекс!", e)

def delete_element(numbers, index):
    try:
        del numbers[index]
        print("Элемент удалён!")
    except IndexError as e:
        print("Ошибка: введён некорректный индекс!", e)

def main():
    numbers = []

    while True:
        try:
            choice = int(input("Меню:\n\
1. Добавить число в список\n\
2. Отображение списка\n\
3. Получение максимального значения\n\
4. Получение минимального значения\n\
5. Отображение значения элемента по индексу\n\
6. Удаление элемента по индексу\n\
0. Выход из программы\n\
Выберите операцию (введите номер 0-6): "))

            if choice == 0:
                break
            elif choice == 1:
                num = int(input("Введите число для добавления: "))
                add_number(numbers, num)
            elif choice == 2:
                display_numbers(numbers)
            elif choice == 3:
                max_value = get_max(numbers)
                if max_value is not None:
                    print("Максимальное значение:", max_value)
            elif choice == 4:
                min_value = get_min(numbers)
                if min_value is not None:
                    print("Минимальное значение:", min_value)
            elif choice == 5:
                try:
                    index = int(input("Введите индекс элемента: "))
                    element = display_element(numbers, index)
                    if element is not None:
                        print("Значение по индексу", index, ":", element)
                except Exception as e:
                    print(e)
            elif choice == 6:
                try:
                    index = int(input("Введите индекс элемента для удаления: "))
                    delete_element(numbers, index)
                except Exception as e:
                    print(e)
            else:
                print("Ошибка: некорректный выбор операции!")

        except ValueError as e:
            print(e)

main()