import tkinter as tk

# Создаем главное окно
root = tk.Tk()

# Устанавливаем заголовок окна
root.title("Управляем квадратиком")

# Устанавливаем размеры окна
window_width = 400
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Создаем холст (Canvas) внутри окна с размерами окна
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Рассчитываем начальные координаты верхнего левого угла квадратика
square_size = 50
square_x = (window_width - square_size) // 2
square_y = (window_height - square_size) // 2

# Рисуем квадратик на холсте
square = canvas.create_rectangle(square_x, square_y, square_x + square_size, square_y + square_size, fill="red")

# Функция для обработки событий клавиатуры
def handle_key_event(event):
    key = event.keysym
    move_distance = 10  # Расстояние, на которое перемещается квадратик при каждом нажатии стрелки

    # Перемещение квадратика в зависимости от нажатой стрелки
    if key == "Up":
        canvas.move(square, 0, -move_distance)
    elif key == "Down":
        canvas.move(square, 0, move_distance)
    elif key == "Left":
        canvas.move(square, -move_distance, 0)
    elif key == "Right":
        canvas.move(square, move_distance, 0)

# Привязываем функцию обработки событий клавиатуры к главному окну
root.bind("<Key>", handle_key_event)

# Запускаем цикл обработки событий
root.mainloop()