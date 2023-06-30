# пример на вайл: 

# start = 0
# end = 10
# while start <= end:
#     print(start, end = ' ')
#     start += 1
# # элс лучше вообще не показывать, он бесполезный :)
# else: # else, примененное в цикле for или while, проверяет, был ли произведен выход из цикла инструкцией break, или же "естественным" образом. 
#     print("good bye")

############################################################################

# пример на else с циклом:

# num = int(input("Введите число: "))
# divisor = 2
# while divisor * divisor <= num:
#     if num % divisor == 0:
#         print("число не простое!")
#         break
#     divisor += 1
# else:
#     print("число простое")

############################################################################

# вложенные циклы (на вайле):

# width = 20
# height = 10
# x = 0
# y = 0
# while y < height:
#     x = 0
#     while x < width:
#         if x == 0 or x == width - 1 or y == 0 or y == height - 1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#         x += 1
#     y += 1
#     print()
   
############################################################################

# списки (они же массивы) - способ хранения данных в памяти
# дать определение массива, объяснить в чём концепт
# проблемы: необходимость придумывать идентификаторы для множества переменных,
# перебор этих переменных, производительность (пример с почтальоном, который разносит почту по частным домам)
# индекс - это смещение от начала массива
# https://metanit.com/python/tutorial/3.1.php

# В Python элементы списка хранятся последовательно в памяти,
# но сам список содержит ссылки на эти элементы. Таким образом, список
# представляет собой непрерывный блок памяти, в котором каждый элемент является
# ссылкой на фактический объект данных.
# Когда вы создаете список и добавляете элементы в него, каждый элемент
# представляет собой отдельный объект, и ссылки на эти объекты сохраняются в памяти.
# Сами объекты могут быть разного размера и типа.

# ar = [1,2,3,4]
# i = 0
# while i < len(ar):
#     print(ar[i], end = ' ')
#     i += 1

# for a in ar:
#     print(a, end = ' ') 
# print(ar)

# https://metanit.com/python/tutorial/3.5.php

# таблица умножения:
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")

import random

br = list()
for i in range(0, 10):
    br.append(random.randrange(0, 100))
    print(br[i], end = ' ')
