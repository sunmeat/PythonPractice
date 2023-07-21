# Напишите информационную систему «Сотрудники». Программа должна обеспечивать
# ввод данных, редактирование данных сотрудника, удаление сотрудника,
# поиск сотрудника по фамилии, вывод информации обо всех сотрудниках,
# указанного возраста, или фамилия которых начинается на указанную букву.
# Организуйте возможность сохранения найденной информации в файл.
# Также весь список сотрудников сохраняется в файл (при выходе из программы —
# автоматически, в процессе исполнения программы — по команде пользователя).
# При старте программы происходит загрузка списка сотрудников из указанного
# пользователем файла.

def load_data_from_file(file_name):
    try:
        with open(file_name, "r", encoding = "utf-8") as file:
            lines = file.readlines()
            data = [line.strip().split(", ") for line in lines]
            return data
    except FileNotFoundError:
        return []

def save_data_to_file(data, file_name):
    with open(file_name, "w", encoding = "utf-8") as file:
        for employee in data:
            file.write(", ".join(employee) + "\n")

def add_employee(data):
    name = input("Введите имя сотрудника: ")
    surname = input("Введите фамилию сотрудника: ")
    age = input("Введите возраст сотрудника: ")
    
    employee = [name, surname, age]
    data.append(employee)
    print("Сотрудник успешно добавлен!")

def edit_employee(data):
    surname = input("Введите фамилию сотрудника, которого хотите отредактировать: ")
    for employee in data:
        if employee[1] == surname:
            name = input("Введите новое имя сотрудника: ")
            age = input("Введите новый возраст сотрудника: ")
            employee[0] = name
            employee[2] = age
            print("Информация о сотруднике успешно отредактирована!")
            break
    else:
        print("Сотрудник с такой фамилией не найден!")

def delete_employee(data):
    surname = input("Введите фамилию сотрудника, которого хотите удалить: ")
    for employee in data:
        if employee[1] == surname:
            data.remove(employee)
            print("Сотрудник успешно удалён!")
            break
    else:
        print("Сотрудник с такой фамилией не найден!")

def search_by_surname(data):
    surname = input("Введите фамилию сотрудника для поиска: ")
    found_employees = []
    for employee in data:
        if employee[1].startswith(surname):
            found_employees.append(employee)
    if found_employees:
        print("Результаты поиска:")
        for employee in found_employees:
            print(f"{employee[0]} {employee[1]}, возраст: {employee[2]}")
    else:
        print("Сотрудники с такой фамилией не найдены!")

def search_by_age(data):
    age = input("Введите возраст сотрудников для поиска: ")
    found_employees = []
    for employee in data:
        if employee[2] == age:
            found_employees.append(employee)
    if found_employees:
        print("Результаты поиска:")
        for employee in found_employees:
            print(f"{employee[0]} {employee[1]}, возраст: {employee[2]}")
    else:
        print("Сотрудники указанного возраста не найдены!")

def show_all_employees(data):
    if not data:
        print("Нет данных о сотрудниках.")
    else:
        print("Список всех сотрудников:")
        for employee in data:
            print(f"{employee[0]} {employee[1]}, возраст: {employee[2]}")

def main():
    file = "data.txt"
    data = load_data_from_file(file)
    
    show_all_employees(data)
    
    while True:
        print("\n1 - Добавить сотрудника")
        print("2 - Редактировать информацию о сотруднике")
        print("3 - Удалить сотрудника")
        print("4 - Поиск по фамилии")
        print("5 - Поиск по возрасту")
        print("6 - Вывести список всех сотрудников")
        print("0 - Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_employee(data)
        elif choice == "2":
            edit_employee(data)
        elif choice == "3":
            delete_employee(data)
        elif choice == "4":
            search_by_surname(data)
        elif choice == "5":
            search_by_age(data)
        elif choice == "6":
            show_all_employees(data)
        elif choice == "0":
            save_data_to_file(data, file)
            print("Данные успешно сохранены. Выход из программы.")
            break
        else:
            print("Неверный выбор, повторите попытку!")

main()