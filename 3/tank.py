# Перенести код из 1_2 tank часть 2
from hitbox import Hitbox

class Tank:
    count = 0
    SIZE = 100
    def __init__(self, canvas, x, y,model = 'Т-14 Армата', ammo = 100, speed = 10):
        self.__hitbox = Hitbox(x, y, Tank.SIZE, Tank.SIZE)   # 1. добавить атрибут hitbox
        self.canvas = canvas
        Tank.count += 1
        self.model = model
        self.hp = 100
        self.xp = 0
        self.ammo = ammo
        self.fuel = 100
        self.speed = speed
        self.x = x
        self.y = y
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
            self.__update_hitbox()  # 2.1 вызвать метод движения HB при смене позиции
            self.fuel -= 1
            self.repaint()
            print(self)

    def backward(self):
        if self.fuel > 0:
            self.y += self.speed
            self.__update_hitbox()   # 2.1 вызвать метод движения HB при смене позиции
            self.fuel -= 1
            self.repaint()
            print(self)

    def left(self):
        if self.fuel > 0:
            self.x += -self.speed
            self.__update_hitbox()  # 2.1 вызвать метод движения HB при смене позиции
            self.fuel -= 1
            self.repaint()
            print(self)

    def right(self):
        if self.fuel > 0:
            self.x += self.speed
            self.__update_hitbox()  # 2.1 вызвать метод движения HB при смене позиции
            self.fuel -= 1
            self.repaint()
            print(self)

    def create(self):
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + Tank.SIZE,
                                               self.y + Tank.SIZE, fill='red')

    def repaint(self):
        self.canvas.moveto(self.id, x = self.x, y = self.y)



    #  2 метод движения хитбокса
    def __update_hitbox(self):
        self.__hitbox.moveto(self.x, self.y)








#    3   метод проверки столкновения - обертка
    def inersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)

    def __str__(self):
        return (f'координаты: x = {self.x}, y = {self.y}, модель: {self.model}, '
                f'здоровье: {self.hp}, опыт: {self.xp}, боеприпасы: {self.ammo}')

