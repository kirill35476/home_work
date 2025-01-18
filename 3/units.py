import textytre as skin
import world
from hitbox import Hitbox
from tkinter import NW
from random import randint

class Unit:
    def __init__(self, canvas, x, y, speed, padding, bot, default_image):
        self._speed = speed
        self._x = x
        self._y = y
        self._vx = 0
        self._vy = 0
        self._canvas = canvas
        self._hp = 100
        self._dx = 0
        self._dy = 0
        self._bot = bot
        self._hitbox = Hitbox(x,y,
                              world.BLOCK_SIZE,
                              world.BLOCK_SIZE,
                              padding=padding)
        self._default_image = default_image
        self._left_image = default_image
        self._right_image = default_image
        self._forward_image = default_image
        self._backward_image = default_image

        self._create()
        self._update_hitdox()
        self._check_map_collision()

    def _create(self):
        self._id = self._canvas.create_image(self._x,self._y,
                                              image = skin.get(self._default_image),
                                              anchor = NW)

    def __del__(self):
        try:
            self._canvas.delete(self._id)
        except Exception:
            pass

    def forvard(self):
        self._vx = 0
        self._vy = -1
        self._canvas.itemconfig(self._id,
                                 image=skin.get(self._forward_image))

    def backward(self):
        self._vx = 0
        self._vy = 1
        self._canvas.itemconfig(self._id,
                                 image=skin.get(self._backward_image))

    def left(self):
        self._vx = -1
        self._vy = 0
        self._canvas.itemconfig(self._id,
                                 image=skin.get(self._left_image))

    def right(self):
        self._vx = 1
        self._vy = 0
        self._canvas.itemconfig(self._id,
                                 image=skin.get(self._right_image))


    def stop(self):
        self._vx = 0
        self._vy = 0

    def update(self):
        if self._bot:
            self._AI
        self._dx = self._vx * self._speed
        self._dy = self._vy * self._speed
        self._x += self._dx
        self._y += self._dy
        self._update_hitdox()
        self._check_map_collision()
        self._repaint()


    def _AI(self):
        pass

    def _update_hitdox(self):
        self._hitbox.moveto(self._x, self._y)


    def _check_map_collision(self):
        detals = {}
        result = self._hitbox.check_map_collision(detals)
        if result:
            self._on_map_collision(detals)
        else:
            self._no_map_collision()

    def _no_map_collision(self):
        pass

    def _on_map_collision(self, details):
        pass

    def repaint(self):
        screen_x = world.get_screen_x(self._x)
        screen_y = world.get_screen_x(self._y)
        self._canvas.moveto(self._id, x=screen_x, y=screen_y)

    def _undo_move(self):
        if self._dx == 0 and self._dy == 0:
            return
        self._x -= self._dx
        self._y -= self._dy
        self._update_hitdox()
        self.repaint()
        self._dx = 0
        self._dy = 0

    def intersect(self,other_unit):
        value = self._hitdox.intersect(other_unit._hitdox)
        if value:
            self._on_collision(other_unit)
        return value

    def _on_collision(self, other_unit):
        self._undo_move()

    def _change_orintation(self):
        rand = randint(0, 3)
        if rand == 0:
            self.left()
        if rand == 1:
            self.forvard()
        if rand == 2:
            self.right()
        if rand == 3:
            self.backward()

    def get_hp(self):
        return self._hp
    def get_speed(self):
        return self._speed
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_vx(self):
