# есть файл dictionary.txt, в котором находятся существительные на русском языке,
# по одному существительному на строку. приложение должно составлять новые
# смешные несуществующие слова, по следующему принципу: берём последние 4 буквы
# слова, находим все слова, которые начинаются на те же самые 4 буквы, соединяем.
# например, слово "пенопласт" и "ласточка". пенопласт заканчивается на "ласт",
# ласточка начинается на "ласт". итоговое слово - "пенопласточка". показать все
# полученные слова. существительные короче 4 символов проигнорировать.
# если итоговое слово будет полностью совпадать с одним из двух образующих слов -
# проигнорировать этот результат
# в результирующей выборке не должно быть повторов

def read_dictionary(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as file:
        words = [line.strip() for line in file if len(line.strip()) >= 4]
    return words

def write_to_file(file_name, data):
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for word in data:
            file.write(word + '\n')

def generate_funny_words(words):
    funny_words = set()

    for word1 in words:
        last_four_letters = word1[-4:]

        for word2 in words:
            if word2.startswith(last_four_letters) and word2 != word1:
                funny_word = word1 + word2[len(last_four_letters):]
                if funny_word != word1 and funny_word != word2:
                    funny_words.add(funny_word)

    return list(funny_words)

def task1():
    dictionary_file = "dictionary.txt"
    words_list = read_dictionary(dictionary_file)
    funny_words_list = generate_funny_words(words_list)

    result_file = "result.txt"
    write_to_file(result_file, funny_words_list)

    print("Смешные слова успешно записаны в файл 'result.txt'.")

###############################################################################

def main():
    task1()
    # task2()
    # task3()

###############################################################################

main()