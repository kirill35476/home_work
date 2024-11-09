from tank import Tank
from tkinter import *
import world

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
    world.set_camera_xy(player.get_x() - world.SREEN_WIDTH//2 + player.get_size()//2,
                        player.get_y() - world.SREEN_HEIGHT//2 + player.get_size()//2)
    player.update()
    enemy.update()
    neutral.update()
    check_collision()
    w.after(1000 // FPS, update)

def check_collision():
    player.intersects(enemy)
    enemy.intersects(player)

def key_press(event):
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
    check_collision()

w = Tk()
w.title('')
canv = Canvas(w, width=world.SREEN_WIDTH, height=world.SREEN_HEIGHT, bg='alice blue')
#canv = Canvas(w, width=800, height=600, bg='alice blue')
canv.pack()

player = Tank(canvas=canv, x=100, y=50, ammo=100, speed=1,bot = False)

enemy = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1,bot = True)

neutral = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1,bot = False)

neutral.stop()

enemy.set_target(player)

w.bind('<KeyPress>', key_press)
update()
w.mainloop()