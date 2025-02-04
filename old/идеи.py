# Создаем HP-бар
self._hp_bar_width = world.BLOCK_SIZE  # Ширина HP-бара
self._hp_bar_height = 5  # Высота HP-бара
self._hp_bar = self._canvas.create_rectangle(
    self._x, self._y - 5,  # Начальные координаты (над танком)
             self._x + self._hp_bar_width, self._y - 5 + self._hp_bar_height,  # Конечные координаты
    fill="green",  # Цвет HP-бара
    outline="black"  # Обводка
)


def damage(self, value):
    self._hp -= value
    if self._hp <= 0:
        self.destroy()
    self._update_hp_bar()  # Обновляем HP-бар


def _update_hp_bar(self):
    # Вычисляем ширину HP-бара в зависимости от текущего здоровья
    hp_width = (self._hp / 100) * self._hp_bar_width

    # Обновляем координаты прямоугольника
    self._canvas.coords(
        self._hp_bar,
        self._x, self._y - 5,  # Начальные координаты
                 self._x + hp_width, self._y - 5 + self._hp_bar_height  # Конечные координаты
    )

    # Меняем цвет HP-бара в зависимости от здоровья
    if self._hp > 50:
        self._canvas.itemconfig(self._hp_bar, fill="green")
    elif self._hp > 20:
        self._canvas.itemconfig(self._hp_bar, fill="yellow")
    else:
        self._canvas.itemconfig(self._hp_bar, fill="red")


def destroy(self):
    super().destroy()
    # Удаляем HP-бар при уничтожении танка
    self._canvas.delete(self._hp_bar)


def update(self):
    super().update()
    # Обновляем позицию HP-бара
    self._canvas.coords(
        self._hp_bar,
        self._x, self._y - 5,  # Начальные координаты
                 self._x + self._hp_bar_width, self._y - 5 + self._hp_bar_height  # Конечные координаты
    )
    self._update_hp_bar()
