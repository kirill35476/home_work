from random import randint
from missile_collection import check_missiles_collision
from units import Tank
from tkinter import NW
import world

_tanks = []
_canvas = None
id_screen_text = 0


def initialize(canv, difficulty="normal"):
    global _canvas, id_screen_text
    _canvas = canv

    # Спавн игрока
    player = spawn(False)

    # Спавн врагов в зависимости от уровня сложности
    if difficulty == "easy":
        num_enemies = 2  # Легкий уровень: 2 врага
    elif difficulty == "normal":
        num_enemies = 4  # Нормальный уровень: 4 врага
    elif difficulty == "hard":
        num_enemies = 6  # Сложный уровень: 6 врагов
    else:
        num_enemies = 4  # По умолчанию: 4 врага

    for _ in range(num_enemies):
        enemy = spawn(True)
        enemy.set_target(player)  # Назначаем игрока целью для врагов

    # Создание текста на экране
    id_screen_text = _canvas.create_text(10, 10,
                                         text=_get_screen_text(),
                                         font=('TkDefualFont', 20),
                                         fill='black',
                                         anchor=NW)


def _get_screen_text():
    if get_player().is_destroyed():
        return 'GAME OVER'
    if len(_tanks) == 1:
        return 'YOU WON'
    return 'Осталось врагов: {}'.format(len(_tanks) - 1)


def _update_screen():
    _canvas.itemconfig(id_screen_text, text=_get_screen_text())


def get_player():
    return _tanks[0]


def update():
    _update_screen()
    start = len(_tanks) - 1
    for i in range(start, -1, -1):
        if _tanks[i].is_destroyed() and i != 0:
            del _tanks[i]
        else:
            _tanks[i].update()
            check_collision(_tanks[i])
            check_missiles_collision(_tanks[i])


def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersect(other_tank):
            return True
    return False


def spawn_enemy():
    pos_x = randint(200, world.WIDTH - 200)
    pos_y = randint(200, world.HEIGHT - 200)
    t = Tank(_canvas, x=pos_x, y=pos_y, speed=1)

    t.set_target(get_player())
    _tanks.append(t)


def spawn(is_bot=True):
    cols = world.get_cols()
    rows = world.get_rows()

    while True:
        col = randint(1, cols - 1)
        row = randint(1, rows - 1)

        if world.get_block(row, col) != world.GROUND:
            continue

        t = Tank(_canvas, row,
                 col, bot=is_bot)

        if not check_collision(t):
            _tanks.append(t)
            return t