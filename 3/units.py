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
        value = self._hitbox.intersects(other_unit._hitbox)
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
        return self._vx

    def get_vy(self):
        return self._vy

    def get_size(self):
        return world.BLOCK_SIZE

    def get_bot(self):
        return self._bot


class Tank(Unit):
    def __init__(self,canvas,row,col,bot = True):
        super().__init__(canvas,col*world.BLOCK_SIZE,row * world.BLOCK_SIZE,2,8,
                         bot,'tank_up')

        if bot:
            self._forward_image = 'tank_up'
            self._backward_image = 'tank_down'
            self._left_image = 'tank_left'
            self._right_image = 'tank_right'
        else:
            self._forward_image = 'tank_up_player'
            self._backward_image = 'tank_down_player'
            self._left_image = 'tank_left_player'
            self._right_image = 'tank_right_player'

        self.forvard()
        self._ammo = 80
        self._usual_speed = self._speed
        self._water_speed = self._speed//2
        self._target = None

        def set_target(self,target):
            self._target = target


        def _AI_goto_target(self):
            if randint(1,2) == 1:
                if self._target.get_x()<self.get_x():
                    self._left()
                else:
                    self.right()
            else:
                if self._target.get_y < self.get_y():
                    self.forvard()
                else:
                    self.backward()

        def _AI(self):
            if randint(1,30)==1:
                if randint(1,10)<9 and self._target is not None:
                    self._AI_goto_target()
                else:
                    self._change_orientation()

        def fire(self):
            if self._ammo > 0:
                self._ammo -= 1

        def _take_ammo(self):
            self._ammo += 10
            if self._ammo > 100:
                self._ammo1 =100

        def get_ammo(self):
            return  self._ammo

        def _set_usual_speed(self):
            self._speed = self._usual_speed
        def _set_water_speed(self):
            self._speed = self._water_speed

        def _on_map_collision(self, details):
            if world.WATER in details and len(details) == 1:
                self.__set_water_speed()
            elif world.MISSLE in details:
                pos = details[world.MISSLE]
                if world.take(pos['row'], pos['col'])!= world.AIR:
                    self._take_ammo()
            else:
                self._undo_move()
                if self._bot:
                    self._change_orientation()

        def _no_map_collision(self):
            self.__set_usual_speed()

        def _on_intersect(self, other_unit):
            super()._on_intersect(other_unit)
            if self._bot:
                self._change_orientation()