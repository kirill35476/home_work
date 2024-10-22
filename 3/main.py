from tank import Tank
from tkinter import*

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68

def check_collision():
    if player.intersects(enemy):
        print('танки столькнулись')

def key_press(event):
    if event.keycode ==KEY_W:
        player.forvard()
    if event.keycode ==KEY_S:
        player.dackward()
    if event.keycode ==KEY_A:
        player.left()
    if event.keycode ==KEY_D:
        player.right()
    check_collision()

w = Tk()
w.title('танки на минималках 2.0')
canv = Canvas(w, width=800, height=600, bg='alice blue')
canv.pack()

player = Tank(canvas=canv,x=100, y=50, ammo=100)

enemy = Tank(canvas=canv, x=300, y=300, ammo=100)

w.bind('<KeyPress>', key_press)

w.mainloop()