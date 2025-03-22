from tkinter import *

class Menu:
    def __init__(self, root, start_game_callback, exit_game_callback):
        self.root = root
        self.frame = Frame(root, bg="lightblue")
        self.frame.pack(fill="both", expand=True)

        # Сохраняем callback-функции
        self.start_game_callback = start_game_callback
        self.exit_game_callback = exit_game_callback

        # Показываем главное меню
        self.show_main_menu()

    def hide(self):
        """Скрыть меню."""
        self.frame.pack_forget()

    def show(self):
        """Показать меню."""
        self.frame.pack(fill="both", expand=True)

    def show_main_menu(self):
        """Показывает главное меню."""
        # Очищаем текущее содержимое меню
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Заголовок меню
        self.title_label = Label(
            self.frame,
            text="Танки на минималках 2.0",
            font=("Arial", 36),
            bg="lightblue"
        )
        self.title_label.pack(pady=50)

        # Кнопка "Начать игру"
        self.start_button = Button(
            self.frame,
            text="Начать игру",
            font=("Arial", 24),
            width=20,
            height=2,
            command=self.show_difficulty_menu
        )
        self.start_button.pack(pady=20)

        # Кнопка "Настройки"
        self.settings_button = Button(
            self.frame,
            text="Настройки",
            font=("Arial", 24),
            width=20,
            height=2,
            command=self.show_soon_message
        )
        self.settings_button.pack(pady=20)

        # Кнопка "Выход"
        self.exit_button = Button(
            self.frame,
            text="Выход",
            font=("Arial", 24),
            width=20,
            height=2,
            command=self.exit_game_callback
        )
        self.exit_button.pack(pady=20)

    def show_difficulty_menu(self):
        """Показывает меню выбора сложности."""
        # Очищаем текущее содержимое меню
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Заголовок меню выбора сложности
        Label(
            self.frame,
            text="Выберите сложность",
            font=("Arial", 36),
            bg="lightblue"
        ).pack(pady=50)

        # Кнопка "Легкий"
        Button(
            self.frame,
            text="Легкий",
            font=("Arial", 24),
            width=20,
            height=2,
            command=lambda: self.start_game_callback("easy")
        ).pack(pady=10)

        # Кнопка "Нормальный"
        Button(
            self.frame,
            text="Нормальный",
            font=("Arial", 24),
            width=20,
            height=2,
            command=lambda: self.start_game_callback("normal")
        ).pack(pady=10)

        # Кнопка "Сложный"
        Button(
            self.frame,
            text="Сложный",
            font=("Arial", 24),
            width=20,
            height=2,
            command=lambda: self.start_game_callback("hard")
        ).pack(pady=10)

        # Кнопка "Назад"
        Button(
            self.frame,
            text="Назад",
            font=("Arial", 24),
            width=20,
            height=2,
            command=self.show_main_menu
        ).pack(pady=20)

    def show_soon_message(self):
        """Показывает сообщение 'Скоро'."""
        # Очищаем текущее содержимое меню
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Надпись "Скоро"
        Label(
            self.frame,
            text="Скоро",
            font=("Arial", 36),
            bg="lightblue"
        ).pack(pady=50)

        # Кнопка "Назад"
        Button(
            self.frame,
            text="Назад",
            font=("Arial", 24),
            width=20,
            height=2,
            command=self.show_main_menu
        ).pack(pady=20)