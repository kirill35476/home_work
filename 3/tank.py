from hitbox import Hitbox
from tkinter import PhotoImage, NW
from random import randint
import world
class Tank:
    __count = 0
    __SIZE = 100

    def __init__(self, canvas, x, y,model='Т-14 Армата', ammo=100, speed=1,
                 up='../img/tank_up.png',
                 down='../img/tank_down.png',
                 right='../img/tank_right.png',
                 left='../img/tank_left.png',
                 bot=True):
        self.__bot = bot
        self.__target = None
        self.__skin_up = PhotoImage(file=up)
        self.__skin_down = PhotoImage(file=down)
        self.__skin_left = PhotoImage(file=left)
        self.__skin_right = PhotoImage(file=right)
        self.__hitbox = Hitbox(x, y, self.get_size(), self.get_size(),  padding = -10)
        Tank.__count += 1
        self.__model = model
        self.__canvas = canvas
        self.__xp = 0
        self.__hp = 100
        self.__ammo = ammo
        self.__fuel = 10000
        self.__x = x
        self.__y = y
        self.__vx = 0
        self.__vy = 0
        self.__speed = speed
        self.__dx = 0  # хранение последнего перемещения танка вдоль осей x и y
        self.__dy = 0
        if self.__x < 0:
            self.__x = 0
        if self.__y < 0:
            self.__y = 0
        self.__create()
        self.right()

    def __check_out_of_world(self):
        if self.__hitbox.left < 0 or \
                self.__hitbox.top < 0 or \
                self.__hitbox.right >= world.WIDTH or \
                self.__hitbox.bottom >= world.HEIGHT:
            self.__undo_move()
            if self.__bot:
                self.__AI_change_orientation()
    def set_target(self, target):
        self.__target = target

    def __AI(self):
        if randint(1,30) == 1:
            if randint(1,10) < 9 and self.__target is not None:
                self.__AI_goto_target()
            else:
                self.__AI_change_orientation()

    def __AI_goto_target(self):
        if randint(1,2) ==1:
            if self.__target.get_x() < self.get_x():
                self.left()
            else:
                self.right()
        else:
            if self.__target.get_y() < self.get_y():
                self.forvard()
            else:
                self.backward()


    def __AI_change_orientation(self):
        rand = randint(0,3)
        if rand == 0:
            self.left()
        if rand == 1:
            self.right()
        if rand == 2:
            self.forvard()
        if rand == 3:
            self.backward()

    def fire(self):
        if self.__ammo > 0:
            self.__ammo -= 1
            print('стреляю')

    def forvard(self):
        self.__vx = 0
        self.__vy = -1
        self.__canvas.itemconfig(self.__id, image=self.__skin_up)

    def backward(self):
        self.__vx = 0
        self.__vy = 1
        self.__canvas.itemconfig(self.__id, image=self.__skin_down)

    def left(self):
        self.__vx = -1
        self.__vy = 0
        self.__canvas.itemconfig(self.__id, image=self.__skin_left)

    def right(self):
        self.__vx = 1
        self.__vy = 0
        self.__canvas.itemconfig(self.__id, image=self.__skin_right)

    def update(self):
        if self.__fuel >= self.__speed:
            self.__update_hitbox()
            self.__check_out_of_world()
            if self.__bot:
                self.__AI()

            self.__dx = self.__vx * self.__speed
            self.__dy = self.__vy * self.__speed
            self.__x += self.__dx
            self.__y += self.__dy

            self.__fuel -= self.__speed
            self.__update_hitbox()
            self.__repaint()

    def __create(self):
        self.__id = self.__canvas.create_image(self.__x, self.__y, image=self.__skin_up, anchor=NW)

    def __repaint(self):
        self.__canvas.moveto(self.__id, x=self.__x, y=self.__y)

    def __update_hitbox(self):
        self.__hitbox.moveto(self.__x, self.__y)

    def intersects(self, other_tank):
        value = self.__hitbox.intersects(other_tank.__hitbox)
        if value:
            self.__undo_move()
            if self.__bot:
                self.__AI_change_orientation()
            return value

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_ammo(self):
        return self.__ammo

    def get_model(self):
        return self.__model

    def get_hp(self):
        return self.__hp

    def get_xp(self):
        return self.__xp

    def get_fuel(self):
        return self.__fuel

    def get_speed(self):
        return self.__speed


    @staticmethod
    def get_quantity(self):
        return self.__count

    #@staticmethod
    def get_size(self):
        return self.__skin_up.width()

    def __undo_move(self):  # откат к предыдущим координатам
        if self.__dx == 0 and self.__dy == 0:
            return
        self.__x -= self.__dx  # отмена последнего движения
        self.__y -= self.__dy
        self.__fuel += self.__speed
        self.__update_hitbox()
        self.__repaint()
        self.__dx = 0
        self.__dy = 0

    def __str__(self):
        return (f'Танк модели {self.__model}, имеет {self.__xp} опыта, имеет {self.__fuel}',
                f' топливо, здоровье:{self.__hp}, Патроны: {self.__ammo}, Координаты:({self.__x},{self.__y})')