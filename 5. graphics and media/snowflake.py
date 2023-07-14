import tkinter as tk
import random
import math

# Создаем главное окно
root = tk.Tk()

# Устанавливаем заголовок окна
root.title("Анимация снежинки")

# Устанавливаем размеры окна
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Создаем холст (Canvas) внутри окна
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Определяем начальные координаты и размер снежинки
x = random.randint(0, window_width)
y = 0
size = random.randint(1, 5)

# Определяем параметры для движения по синусоиде
amplitude = 100
frequency = 0.02
angle = 0

# Функция для анимации падения снежинки
def animate():
    global x, y, angle

    # Declare and initialize the 'size' variable
    size = random.randint(1, 5)

    # If the snowflake reaches the bottom of the window
    if y >= window_height:
        # Return the snowflake to the top
        x = random.randint(0, window_width)
        y = 0

    # Increase the snowflake's coordinates for falling and sinusoidal movement
    y += size
    x = window_width/2 + amplitude * math.sin(angle)
    angle += frequency

    # Clear the canvas
    canvas.delete("all")

    # Draw the snowflake on the canvas
    canvas.create_oval(x, y, x + size, y + size, fill="white")

    # Schedule the next animation step after a small interval of time
    canvas.after(10, animate)

# Запускаем анимацию
animate()

# Запускаем цикл обработки событий
root.mainloop()