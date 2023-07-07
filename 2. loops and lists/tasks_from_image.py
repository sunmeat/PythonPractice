# последовательность фибоначчи образуется так: первый и второй члены последовательности равны 1,
# каждый следующий равен сумме двух предыдущих. дано натуральное число N больше либо равное 3.
# необходимо получить:
# 1) первые N членов последовательности
# 2) верно ли, что сумма первых N членов последовательности является чётным числом?
# 3) значение K-того члена последовательности

# N = int(input("Введите натуральное число N (N >= 3): "))
N = 10

sequence = [1, 1]  # первые два члена последовательности

for i in range(2, N):
    next_number = sequence[i - 1] + sequence[i - 2]
    sequence.append(next_number)

print("Первые {} членов последовательности: {}".format(N, sequence))

# проверка, является ли сумма первых N членов последовательности чётным числом
sum_of_sequence = sum(sequence)
is_even = sum_of_sequence % 2 == 0
print("Сумма первых N членов последовательности является чётным числом: {}".format(is_even))

# Ввод значения K
# K = int(input("Введите номер K-го члена последовательности (1 <= K <= N): "))
K = 5

# Получение значения K-го члена последовательности
nth_number = sequence[K - 1]
print("Значение K-го члена последовательности: {}\n\n".format(nth_number))

######################################################################################################

# ах, условие звучало так интересно )) а код и ответ оказались очень простыми :)
# одноклеточная амёба каждые 3 часа делится пополам. определить, сколько амёб будет через
# 3, 6, 9, 12, 15, 18, 21, 24 часа, если первоначально была одна амёба

# первоначальное количество амеб
amoeba_count = 1
# время в часах
time = 24
# цикл для расчета количества амёб
for t in range(3, time + 1, 3):
    amoeba_count *= 2
    # вывод количества амёб через указанное время
    print("через {}ч будет {} амёб{}...".format(t, amoeba_count, 'ы' if amoeba_count in (2, 4, 32, 64) else ''), end = ' ')
print('ну как будет, - гипотетически :) иногда амёбы испытывают недостаток питательных веществ\
 (к счастью, они не всеядны), им приходится конкурировать с другими живыми организмами, они\
 бедняги часто подвергаются патогенам и болезням... а то б уже давно во вселенной остались\
 одни только амёбы)))')

######################################################################################################

# гражданин 1 марта открыл счёт в банке, вложив 1000 гривен. через каждый месяц размер вклада
# увеличивается на 2% от имеющейся суммы. определить:
# 1) прирост суммы вклада за каждый месяц
# 2) сумму вклада по итогам каждого месяца
# 3) реальный профит, с учётом того, что инфляция в стране составляет более 25% (((

initial_amount = 1000
inflation_rate = 0.25
months = 10

current_amount = initial_amount

for month in range(1, months + 1):
    growth = current_amount * 0.02  # размер прироста суммы вклада
    current_amount += growth  # обновление общей суммы вклада
    
    # расчет реального профита с учётом инфляции
    real_profit = growth - (current_amount * inflation_rate)
    
    print(f"Месяц {month}: Прирост суммы вклада: {growth:.2f} грн,\n"
          f"Общая сумма вклада: {current_amount:.2f} грн, "
          f"реальный профит: {real_profit:.2f} грн\n\n")
    
######################################################################################################

# с лыжником всё ясно :)