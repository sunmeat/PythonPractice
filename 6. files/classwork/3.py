# with open("hello.txt", "w", encoding="utf8") as somefile:
#     somefile.write("Привет мир")
#     somefile.write("\nHello world")

#     with open(file, mode) as file_obj:
#       инструкции

# Эта конструкция определяет для открытого файла переменную file_obj и выполняет набор инструкций. После их выполнения файл автоматически закрывается. Даже если при выполнении инструкций в блоке with возникнут какие-либо исключения, то файл все равно закрывается.

# filename = "hello.txt"
# with open(filename, encoding="utf8") as file:
#     text = file.read()
#     print(text)

# file = open("hello.txt","r",encoding="utf8")
# text = file.read()
# print(text)
# file.close()