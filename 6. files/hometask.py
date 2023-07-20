# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли их строки.
# Если нет, то вывести несовпадающую строку из каждого файла. 

def compare_files(file1, file2):
    try:
        with open(file1, 'r', encoding = 'utf-8') as f1, open(file2, 'r', encoding = 'utf-8') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            min_len = min(len(lines1), len(lines2))

            for i in range(min_len):
                if lines1[i] != lines2[i]:
                    # https://metanit.com/python/tutorial/5.2.php about strip method
                    print(f"Файл 1: {lines1[i].strip()}")
                    print(f"Файл 2: {lines2[i].strip()}")
                    # return
            if len(lines1) != len(lines2):
                if len(lines1) > min_len:
                    print(f"Файл 1: {lines1[min_len].strip()}")
                else:
                    print(f"Файл 2: {lines2[min_len].strip()}")
    except FileNotFoundError:
        print("Ошибка: один из файлов не найден.")
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def task1():
    file1 = "input.txt"
    file2 = "output.txt"
    compare_files(file1, file2)

###############################################################################

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл и записать
# в него следующую статистику по исходному файлу:
# Количество символов;
# Количество строк;
# Количество гласных букв;
# Количество согласных букв;
# Количество цифр

def count_statistics(input_file, output_file):
    try:
        with open(input_file, 'r', encoding = 'utf-8') as file:
            content = file.read()

            num_characters = len(content)
            num_lines = len(content.split('\n'))

            vowels = 'AEIOUaeiou'
            consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
            digits = '0123456789'

            num_vowels = 0
            num_consonants = 0
            num_digits = 0

            for char in content:
                if char in vowels:
                    num_vowels += 1
                elif char in consonants:
                    num_consonants += 1
                elif char in digits:
                    num_digits += 1

        with open(output_file, 'w', encoding = 'utf-8') as file:
            file.write(f"Количество символов: {num_characters}\n")
            file.write(f"Количество строк: {num_lines}\n")
            file.write(f"Количество гласных букв: {num_vowels}\n")
            file.write(f"Количество согласных букв: {num_consonants}\n")
            file.write(f"Количество цифр: {num_digits}\n")

    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def task2():
    input_file = "input.txt"
    output_file = "output.txt"
    count_statistics(input_file, output_file)
    print("Статистика успешно записана в файл.")

###############################################################################

# Задание 3
# Дан текстовый файл. Удалить из него последнюю строку.
# Результат записать в другой файл. 

def remove_last_line(input_file, output_file):
    try:
        with open(input_file, 'r', encoding = 'utf-8') as source_file:
            lines = source_file.readlines()

            if lines:
                lines.pop()  # удаляем последнюю строку

        with open(output_file, 'w', encoding = 'utf-8') as destination_file:
            destination_file.writelines(lines)

        print("Последняя строка успешно удалена и результат записан в файл.")
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def task3():
    input_file = "input.txt"
    output_file = "output.txt"
    remove_last_line(input_file, output_file)

###############################################################################

# Задание 4
# Дан текстовый файл. Найти длину самой длинной строки.

def find_longest_line_length(file_name):
    try:
        with open(file_name, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
            longest = 0
            for line in lines:
                line_length = len(line)
                if line_length > longest:
                    longest = line_length
            return longest
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден.")
        return 0
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
        return 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return 0

def task4():
    file_name = "input.txt"
    longest_length = find_longest_line_length(file_name)
    print(f"Длина самой длинной строки в файле '{file_name}': {longest_length}")

###############################################################################

# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нём
# встречается заданное пользователем слово.

def count_word_occurrences(file_name, word):
    try:
        with open(file_name, 'r', encoding = 'utf-8') as file:
            content = file.read()
            word_count = content.lower().count(word.lower())
            return word_count
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден.")
        return 0
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
        return 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return 0

def task5():
    file = "input.txt"
    word = input("Введите слово для поиска: ")
    count = count_word_occurrences(file, word)
    print(f"Количество вхождений слова '{word}' в файле '{file}': {count}")
    # Введите слово для поиска: это
    # Количество вхождений слова 'это' в файле 'input.txt': 2

###############################################################################

# Задание 6
# Дан текстовый файл. Найти и заменить в нём заданное слово.
# Что искать и на что заменять определяется пользователем.

def find_and_replace(file_name, searchw, replacew):
    try:
        with open(file_name, 'r', encoding = 'utf-8') as file:
            content = file.read()

        # замена слова (с учётом регистра)
        updated_content = content.replace(searchw, replacew)

        with open(file_name, 'w', encoding = 'utf-8') as file:
            file.write(updated_content)

        print("Замена выполнена успешно.")
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден.")
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def task6():
    file_name = "input.txt"
    search = input("Введите слово для поиска: ")
    replace = input("Введите слово для замены: ")

    find_and_replace(file_name, search, replace)
    # Введите слово для поиска: это
    # Введите слово для замены: 11111
    # Замена выполнена успешно.

###############################################################################

def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    task6()

###############################################################################

main()