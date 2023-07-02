# В списке целых, заполненном случайными числами вычислить:

# Сумму отрицательных чисел;
# Сумму четных чисел;
# Сумму нечетных чисел;
# Произведение элементов с индексами кратными 3;
# Произведение элементов между минимальным и максимальным элементом;
# Сумму элементов, находящихся между первым и последним поло­житель­ными элементами.

import random

# Задаем размер списка
size = 10

# Создаем список и заполняем его случайными числами от -100 до 100
numbers = [random.randint(-100, 100) for _ in range(size)] # символ _ используется вместо переменной, поскольку мы не используем значение переменной внутри цикла
# numbers = []
# for i in range(size):
#     numbers.append(random.randint(-100, 100))

print("Список случайных чисел:", numbers)

# Вычисляем сумму отрицательных чисел
negative_sum = sum(num for num in numbers if num < 0) # генератор списка (list comprehension), который проходит по каждому элементу num в списке numbers и формирует новый список из этих элементов
print("Сумма отрицательных чисел:", negative_sum)

# Вычисляем сумму чётных чисел
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Сумма чётных чисел:", even_sum)

# Вычисляем сумму нечётных чисел
odd_sum = sum(num for num in numbers if num % 2 != 0)
print("Сумма нечётных чисел:", odd_sum)

# Вычисляем произведение элементов с индексами, кратными 3
index_product = 1
index = 0
for num in numbers:
    if index % 3 == 0:
        index_product *= num
    index += 1
print("Произведение элементов с индексами, кратными 3:", index_product)

# Вычисляем произведение элементов между минимальным и максимальным элементом
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
start_index = min(min_index, max_index)
end_index = max(min_index, max_index)
product = 1
for num in numbers[start_index:end_index]:
    product *= num
print("Произведение элементов между минимальным и максимальным элементом:", product)

# Вычисляем сумму элементов, находящихся между первым и последним положительными элементами
start_index = -1
for i in range(len(numbers)):
    if (numbers[i] > 0):
        start_index = i
        break
print(numbers[start_index])

end_index = -1
for i in range(len(numbers) - 1, -1, -1): # Цикл for от 10 до 0 с шагом -1
    if (numbers[i] > 0):
        end_index = i
        break
print(numbers[end_index])

sum_between = sum(numbers[start_index:end_index])
print("Сумма элементов, находящихся между первым и последним положительными элементами:", sum_between)

###################################################################################################################

# Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:

# Создать список целых, содержащий только четные числа из первого списка;
# Создать список целых, содержащий только нечетные числа из первого списка;
# Создать список целых, содержащий только отрицательные числа из первого списка;
# Создать список целых, содержащий только положительные числа из первого списка.

# Создаем список четных чисел
even_numbers = [num for num in numbers if num % 2 == 0]
print("Список чётных чисел:", even_numbers)

# Создаем список нечетных чисел
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Список нечётных чисел:", odd_numbers)

# Создаем список отрицательных чисел
negative_numbers = [num for num in numbers if num < 0]
print("Список отрицательных чисел:", negative_numbers)

# Создаем список положительных чисел
positive_numbers = [num for num in numbers if num > 0]
print("Список положительных чисел:", positive_numbers)