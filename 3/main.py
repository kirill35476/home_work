from tank import Tank
from tkinter import *
import world
import tank_collection
import textytre

KEY_UP = 38
KEY_LEFT = 39
KEY_RIGHT= 37
KEY_DOWN = 40

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68

FPS = 60

def update():
    tank_collection.update()
    player = tank_collection.get_player()
    world.set_camera_xy(player.get_x() - world.SREEN_WIDTH//2 + player.get_size()//2,
                        player.get_y() - world.SREEN_HEIGHT//2 + player.get_size()//2)
    w.after(1000 // FPS, update)

def key_press(event):

    player = tank_collection.get_player()

    if event.keycode == KEY_W:
        player.forvard()
    if event.keycode == KEY_S:
        player.backward()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()

    elif event.keycode == KEY_UP:
        world.move_camera(0, -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(0, 5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(-5, 0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(5, 0)
    elif event.keycode == 32:
        tank_collection.spawn_enemy()
#    check_collision()

def load_textytre():
    textytre.load('tank_up','../img/tank_up.png')
    textytre.load('tank_down','../img/tank_down.png')
    textytre.load('tank_left','../img/tank_left.png')
    textytre.load('tank_right','../img/tank_right.png')
    print(textytre._frames)

w = Tk()

load_textytre()

w.title('')
canv = Canvas(w, width=world.SREEN_WIDTH, height=world.SREEN_HEIGHT, bg='alice blue')
#canv = Canvas(w, width=800, height=600, bg='alice blue')
canv.pack()

tank_collection.initialize(canv)

w.bind('<KeyPress>', key_press)
update()
w.mainloop()