# Дан текстовый файл. Подсчитать количество слов, начинающихся с символа, который задаёт пользователь.
count=0
c = input("Введите символ -> ")
with open("rez.txt","r") as f:
    buf = f.read()

arr = buf.split(' ')    
for i in range(len(arr)):      
    if arr[i].startswith('H'):  
        print(arr[i])
        count+=1
print(count)