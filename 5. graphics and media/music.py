import tkinter as tk
import pygame

# Создаем главное окно
root = tk.Tk()

# Устанавливаем заголовок окна
root.title("Проигрывание музыки")

# Устанавливаем размеры окна
window_width = 400
window_height = 300
root.geometry(f"{window_width}x{window_height}")

# Функция для проигрывания музыки
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/1/armin.mp3")  # Укажите путь к вашему музыкальному файлу
    pygame.mixer.music.play()

# Создаем кнопку для проигрывания музыки
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=20)

# Запускаем цикл обработки событий
root.mainloop()