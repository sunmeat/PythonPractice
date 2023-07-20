# Задание 1
# Дан текстовый файл. Необходимо создать новый файл, в который требуется
# переписать из исходного файла все слова, состоящие не менее чем из семи букв. 

# исходный текстовый файл создаётся программно
def create_input_file(file_name):
    try:
        file = open(file_name, 'w', encoding = 'utf-8')
        try:
            file.write("Python поддерживает множество различных типов файлов, но условно их можно разделить на два вида: текстовые и бинарные.\n")
            file.write("Текстовые файлы - это к примеру файлы с расширением cvs, txt, html, в общем любые файлы, которые сохраняют информацию в текстовом виде.\n")
            file.write("Бинарные файлы - это изображения, аудио и видеофайлы и т.д. \n")
            file.write("В зависимости от типа файла работа с ним может немного отличаться.\n")
        except Exception as e:
            print(e)
        finally:
            file.close()
    except Exception as e:
        print(e)

def extract_words(input_file, output_file):
    try:
        file = open(input_file, 'r', encoding = 'utf-8')
        try:
            text = file.read()
        except Exception as e:
            print(e)
        finally:
            file.close()
    except Exception as e:
            print(e)

    words = []
    for word in text.split():
        if len(word) >= 7:
            words.append(word)

    try:
        file = open(output_file, 'w', encoding = 'utf-8')
        try:
            for word in words:
                file.write(word)
                file.write(' ')
            file.close()
        except Exception as e:
            print(e)
        finally:
            file.close()
    except Exception as e:
            print(e)

def task1():
    input_file = "input.txt"
    output_file = "output.txt"

    create_input_file(input_file)
    extract_words(input_file, output_file)
    print("Слова, длиной не менее 7 букв, успешно извлечены из input.txt и записаны в output.txt.")

###############################################################################

# Задание 2
# Дан текстовый файл. Необходимо переписать его строки в другой файл.
# Порядок строк во втором файле должен совпадать с порядком строк в заданном файле. 

def copy_file(source_file, destination_file):
    try:
        source = open(source_file, 'r', encoding = 'utf-8')
        destination = open(destination_file, 'w', encoding = 'utf-8')

        for line in source:
            destination.write(line)

        source.close()
        destination.close()

    except FileNotFoundError:
        print(f"Ошибка: файл '{source_file}' не найден.")
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def task2():
    source_file = "input.txt"
    destination_file = "output.txt"
    copy_file(source_file, destination_file)
    print("Файл успешно скопирован.")

###############################################################################

# Задание 3
# Дан текстовый файл. Необходимо переписать его строки в другой файл.
# Порядок строк во втором файле должен быть обратным по отношению к порядку
# строк в заданном файле. 

def reverse_copy_file(source_file, destination_file):
    try:
        source = open(source_file, 'r', encoding = 'utf-8')
        lines = source.readlines()
        source.close()

        reversed_lines = list(reversed(lines)) # https://www.w3schools.com/python/ref_func_reversed.asp

        destination = open(destination_file, 'w', encoding = 'utf-8')
        destination.writelines(reversed_lines)
        destination.close()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_file}' не найден.")
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def task3():
    source_file = "input.txt"
    destination_file = "output.txt"
    reverse_copy_file(source_file, destination_file)
    print("Файл успешно скопирован в обратном порядке.")

###############################################################################

# Задание 4
# Дан текстовый файл. Добавить в него строку из двенадцати
# звездочек (************), поместив её после последней из строк,
# в которых нет запятой. Если таких строк нет, то новая строка должна быть
# добавлена после всех строк имеющегося файла. Результат записать в другой файл. 

def add_star_line(input_file, output_file):
    lines_with_comma = []
    try:
        input_file_handler = open(input_file, 'r', encoding = 'utf-8')
        lines = input_file_handler.readlines()
        input_file_handler.close()

        for index, line in enumerate(lines):
            if ',' not in line:
                lines_with_comma.append(index)

        # если есть строки без запятой, вставляем строку с 12 звёздочками перед последней из них
        if lines_with_comma:
            last_line_with_comma = lines_with_comma[-1]
            lines.insert(last_line_with_comma, "************\n")
        # если нет строк без запятой, добавляем строку с 12 звёздочками в конец файла
        else:
            lines.append("************\n")

        output_file_handler = open(output_file, 'w', encoding = 'utf-8')
        output_file_handler.writelines(lines)
        output_file_handler.close()

        print("Строка с 12 звёздочками успешно добавлена в файл.")
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def task4():
    input_file = "input.txt"
    output_file = "output.txt"
    add_star_line(input_file, output_file)

###############################################################################

# Задание 5
# Дан текстовый файл. Подсчитать количество слов, начинающихся с символа,
# который задаёт пользователь.

def count_words_with_starting_character(file_name, char):
    count = 0
    try:
        file = open(file_name, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()

        for line in lines:
            words = line.split()
            for word in words:
                if word.startswith(char):
                    count += 1
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден.")
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return count

def task5():
    file_name = "input.txt"
    char = input("Введите символ: ")
    count = count_words_with_starting_character(file_name, char)
    print(f"Количество слов, начинающихся с символа '{char}': {count}")
    # Количество слов, начинающихся с символа 'т': 5

###############################################################################

# Задание 6
# Дан текстовый файл. Переписать в другой файл все его строки с заменой
# в них символа * на символ & и наоборот.

def replace_and_copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r', encoding = 'utf-8') as source:
            lines = source.readlines()

            with open(destination_file, 'w', encoding = 'utf-8') as destination:
                for line in lines:
                    replaced_line = line.replace('*', '&').replace('&', '*')
                    destination.write(replaced_line)
    except FileNotFoundError:
        print(f"Ошибка: файл '{source_file}' не найден.")
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def task6():
    source_file = "input.txt"
    destination_file = "output.txt"
    replace_and_copy_file(source_file, destination_file)
    print("Файл успешно скопирован с заменой символов.")

###############################################################################

# Задание 7
# Дан массив строк. Записать их в файл, расположив каждый элемент массива
# на отдельной строке с сохранением порядка.

def write_array_to_file(array, file_name):
    try:
        with open(file_name, 'w', encoding = 'utf-8') as file:
            for item in array:
                file.write(item + '\n')
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def task7():
    array = ["строка 1", "строка 2", "строка 3", "ещё одна строка"]
    file_name = "output.txt"
    write_array_to_file(array, file_name)
    print("Массив успешно записан в файл.")

###############################################################################

# Задание 8
# Дан массив строк. Записать их в файл, расположив каждый элемент
# массива на отдельной строке с сохранением порядка. 

# не нашёл отличий в ТЗ 7 и 8 задания :)

###############################################################################

# Задание 9
# Дан текстовый файл. Подсчитать количество символов в нём. 

def count_characters_in_file(file_name):
    try:
        with open(file_name, 'r', encoding = 'utf-8') as file:
            content = file.read()
            count = len(content)
        return count
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден.")
        return 0
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
        return 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return 0

def task9():
    file_name = "input.txt"
    character_count = count_characters_in_file(file_name)
    print(f"Количество символов в файле '{file_name}': {character_count}")
    # Количество символов в файле 'input.txt': 383

###############################################################################

# Задание 10
# Дан текстовый файл. Подсчитать количество строк в нём.

def count_lines_in_file(file_name):
    try:
        with open(file_name, 'r', encoding = 'utf-8') as file:
            line_count = 0
            for _ in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден.")
        return 0
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
        return 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return 0

def task10():
    file_name = "input.txt"
    line_count = count_lines_in_file(file_name)
    print(f"Количество строк в файле '{file_name}': {line_count}")
    # Количество строк в файле 'input.txt': 4
    
def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6() # с этой функции файловые потоки уже открываются с with
    # task7()
    # ??? ТЗ совпадает с task7
    # task9()
    task10()

main()