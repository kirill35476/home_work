import tkinter as tk
import main
from tkinter import messagebox

# Основное окно
root = tk.Tk()
root.title("Меню и игра")
root.geometry("800x800")  # Размер окна


# Функция для переключения между экранами
def show_frame(frame):
    frame.tkraise()


# Создание фреймов для меню и игры
menu_frame = tk.Frame(root)
game_frame = tk.Frame(root)

# Размещение фреймов в окне
for frame in (menu_frame, game_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# ==================== Меню ====================
# Заголовок меню
title_label = tk.Label(menu_frame, text="Главное меню", font=("Arial", 36))
title_label.pack(pady=50)

# Кнопка "Начать игру"
start_button = tk.Button(
    menu_frame,
    text="Начать игру",
    font=("Arial", 24),
    width=20,
    height=2,
    command=lambda: show_frame(game_frame)  # Переключаемся на экран игры
)
start_button.pack(pady=20)

# Кнопка "Настройки"
settings_button = tk.Button(
    menu_frame,
    text="Настройки",
    font=("Arial", 24),
    width=20,
    height=2,
    command=lambda: messagebox.showinfo("Настройки", "Здесь будут настройки игры")
)
settings_button.pack(pady=20)

# Кнопка "Выход"
exit_button = tk.Button(
    menu_frame,
    text="Выход",
    font=("Arial", 24),
    width=20,
    height=2,
    command=root.destroy  # Закрываем приложение
)
exit_button.pack(pady=20)

# ==================== Игра ====================
# Заголовок игры
game_title_label = tk.Label(game_frame, text="Игра началась!", font=("Arial", 36))
game_title_label.pack(pady=50)

# Кнопка "Выйти в меню"
back_to_menu_button = tk.Button(
    game_frame,
    text="Выйти в меню",
    font=("Arial", 24),
    width=20,
    height=2,
    command=lambda: show_frame(menu_frame)  # Переключаемся на экран меню
)
back_to_menu_button.pack(pady=20)

# Показываем меню при запуске
show_frame(menu_frame)

# Запуск основного цикла
root.mainloop()
