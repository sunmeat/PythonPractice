myfile = open("hello.txt", "w")

string  = input("Введите строку -> ")
myfile.write(string)

myfile.close()