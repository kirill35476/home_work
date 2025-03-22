from tkinter import *
from menu import Menu
import missile_collection
import world
import tank_collection
import textytre

KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37, 39, 38, 40
KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68
FPS = 60


def update():
    tank_collection.update()
    missile_collection.update()
    player = tank_collection.get_player()
    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_size() // 2,
                        player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_size() // 2)
    world.update_map()
    w.after(1000 // FPS, update)


def key_press(event):
    player = tank_collection.get_player()

    if player.is_destroyed():
        return

    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
    elif event.keycode == KEY_UP:
        world.move_camera(0, -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(0, 5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(-5, 0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(5, 0)
    elif event.keycode == 32:  # Пробел
        player.fire()



def load_textures():
    textytre.load('tank_up', '../img/tank_up.png')
    textytre.load('tank_down', '../img/tank_down.png')
    textytre.load('tank_left', '../img/tank_left.png')
    textytre.load('tank_right', '../img/tank_right.png')

    textytre.load('tank_up_player', '../img/tank_up_player.png')
    textytre.load('tank_down_player', '../img/tank_down_player.png')
    textytre.load('tank_left_player', '../img/tank_left_player.png')
    textytre.load('tank_right_player', '../img/tank_right_player.png')

    textytre.load(world.BRICK, '../img/brick.png')
    textytre.load(world.WATER, '../img/water.png')
    textytre.load(world.CONCRETE, '../img/wall.png')

    textytre.load(world.MISSLE, '../img/bonus.png')

    textytre.load('missile_up', '../img/missile_up.png')
    textytre.load('missile_left', '../img/missile_left.png')
    textytre.load('missile_right', '../img/missile_right.png')
    textytre.load('missile_down', '../img/missile_down.png')

    textytre.load('tank_destroy', '../img/tank_destroy.png')


def start_game(difficulty="normal"):
    """Запуск игры с выбранной сложностью."""
    print(f"Выбрана сложность: {difficulty}")  # Для отладки
    menu.hide()  # Скрываем меню
    canv.pack()  # Показываем холст с игрой
    world.initialize(canv)
    tank_collection.initialize(canv, difficulty)  # Передаем сложность
    missile_collection.initialize(canv)
    w.bind('<KeyPress>', key_press)
    update()


def exit_game():
    """Выход из игры."""
    w.destroy()


# Создание основного окна
w = Tk()
w.title('Танки на минималках 2.0')
w.geometry(f"{world.SCREEN_WIDTH}x{world.SCREEN_HEIGHT}")

# Загрузка текстур
load_textures()

# Создание холста для игры
canv = Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg='light green')

# Создание меню
menu = Menu(w, start_game, exit_game)

# Показываем меню при запуске
menu.show()

# Запуск основного цикла
w.mainloop()