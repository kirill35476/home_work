from hitbox import Hitbox
from tkinter import PhotoImage, NW


class Tank:

    count = 0
    SIZE = 100

    def __init__(self, canvas, x, y, model='Т-14 Армата', ammo=100, speed=10,
                 file_up="../img/image (1).png",
                 file_down="../img/image 3.png",
                 file_right="../img/image 2.png",
                 file_left="../img/image 4.png"):
        self.__hitbox = Hitbox(x, y, Tank.SIZE, Tank.SIZE)
        self.__canvas = canvas
        Tank.count += 1
        self.model = model
        self.hp = 100
        self.xp = 0
        self.ammo = ammo
        self.fuel = 100
        self.speed = speed
        self.x = x
        self.y = y
        self.__skin_up = PhotoImage(file=file_up)
        self.__skin_down = PhotoImage(file=file_down)
        self.__skin_right = PhotoImage(file=file_right)
        self.__skin_left = PhotoImage(file=file_left)
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

        self.create()

    def fire(self):
        if self.ammo > 0:
            self.ammo -= 1
            print('стреляю')

    def forvard(self):
        if self.fuel > 0:
            self.y += -self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.__canvas.itemconfif(self.__id, image=self.__skin_up)
            self.repaint()
            print(self)

    def backward(self):
        if self.fuel > 0:
            self.y += self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.__canvas.itemconfif(self.__id, image=self.__skin_down)
            self.repaint()
            print(self)

    def left(self):
        if self.fuel > 0:
            self.x += -self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.__canvas.itemconfif(self.__id, image=self.__skin_left)
            self.repaint()
            print(self)

    def right(self):
        if self.fuel > 0:
            self.x += self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.__canvas.itemconfif(self.__id, image=self.__skin_right)
            self.repaint()
            print(self)

    def create(self):
        self.id = self.__canvas.create_image(self.x, self.y, self.x + Tank.SIZE,
                                             image=self.__skin_up, anchor = NW)

    def repaint(self):
        self.__canvas.moveto(self.id, x=self.x, y=self.y)

    def __update_hitbox(self):
        self.__hitbox.moveto(self.x, self.y)

    def inersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)

    def __str__(self):
        return (f'координаты: x = {self.x}, y = {self.y}, модель: {self.model}, '
                f'здоровье: {self.hp}, опыт: {self.xp}, боеприпасы: {self.ammo}')

