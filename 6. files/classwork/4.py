# имя файла
FILENAME = "messages.txt"
# определяем пустой список
messages = list()
 
for i in range(4):
    message = input("Введите строку " + str(i+1) + ": ")
    messages.append(message + "\n")
 
# запись списка в файл
with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)
 
# считываем сообщения из файла
print("Считанные сообщения")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")