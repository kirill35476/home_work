from hitbox import Hitbox
from tkinter import  PhotoImage,NW
class Tank:
    __count = 0
    #__SIZE = 100
    def __init__(self,canvas , x, y , model = 'Т-14 Армата',
                 ammo = 100, speed = 10,
                 up = '../img/tank_up.png',
                 down = '../img/tank_down.png',
                 right = '../img/tank_right.png',
                 left = '../img/tank_left.png',):
        self.__skin_up = PhotoImage(file=up)
        self.__skin_down = PhotoImage(file=down)
        self.__skin_left = PhotoImage(file=left)
        self.__skin_right = PhotoImage(file=right)
        self.__hitbox = Hitbox(x, y, self.get_size(), self.get_size())
        Tank.__count +=1
        self.__model = model
        self.__canvas = canvas
        self.__xp =  0
        self.__hp = 100
        self.__ammo = ammo
        self.__fuel = 10000
        self.__x = x
        self.__y = y
        self.__vx = 0
        self.__vy = 0
        self.__speed = speed
        if self.__x < 0 :
            self.__x = 0
        if self.__y < 0 :
            self.__y = 0
        self.__create()
        self.right()
    def fire(self):
        if self.__ammo>0:
            self.__ammo-=1
            print('стреляю')

    def forvard(self):
        self.__vx = 0
        self.__vy = -1
        self.__canvas.itemconfig(self.__id, image=self.__skin_up)

    def dackward(self):
        self.__vx = 0
        self.__vy = 1
        self.__canvas.itemconfig(self.__id, image=self.__skin_down)


    def left(self):
        self.__vx = -1
        self.__vy = 0
        self.__canvas.itemconfig(self.__id,image = self.__skin_left)


    def right(self):
        self.__vx = 1
        self.__vy = 0
        self.__canvas.itemconfig(self.__id,image = self.__skin_right)


    def ubdate(self):
        if self.__fuel > self.__speed:
            self.__x += self.__vx * self.__speed
            self.__y += self.__vy * self.__speed
            self.__fuel -= self.__speed
            self.__ubdate_hitbox()
            self.__repaint()

    def __create(self):
        self.__id = self.__canvas.create_image(self.__x, self.__y, image = self.__skin_up, anchor = NW)
    def __repaint(self):
        self.__canvas.moveto(self.__id, x = self.__x, y = self.__y)

    def __ubdate_hitbox(self):
        self.__hitbox.moveto(self.__x, self.__y)

    def inersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_ammo(self):
        return self.ammo
    def get_model(self):
        return self.model
    def get_hp(self):
        return self.hp
    def get_xp(self):
        return self.xp
    def get_fuel(self):
        return self.fuel
    def get_speed(self):
        return self.speed
    @staticmethod
    def get_quantity(self):
        return self.__count
    #@staticmethod
    def get_size(self):
        return self.__skin_up.width()

    def __str__(self):
        return (f'Танк модели {self.__model}, имеет {self.__xp} опыта, имеет {self.__fuel} топливо, здоровье:{self.__hp}'
              f', Патроны: {self.__ammo}, Координаты:({self.__x},{self.__y})')