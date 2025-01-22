import tkinter as tk # вызов библиотеки  tkinter

class MovingObject: # создание класса MovingObject
    def __init__(self, canvas, x, y, image_path):# конструктор класса 
        self.canvas = canvas
        self.x = x
        self.y = y
        self.image_tk = tk.PhotoImage(file=image_path)
        self.obj = self.canvas.create_image(x, y, anchor=tk.CENTER, image=self.image_tk)

    def move(self, dx, dy):# движение объекта\
        self.canvas.move(self.obj, dx, dy)
        self.x += dx
        self.y += dy

class BouncingObject(MovingObject):# создание класса наследника 
    def __init__(self, canvas, x, y, image_path, dx, dy):# конструктор класса

    def update(self, width, height): # создание мотода update
        #Проверка на столкновение с стенками
        img_width = self.image_tk.width()
        img_height = self.image_tk.height()
        #изменение напровления при столкновении с стенами
        if self.x + img_width / 2 >= width or self.x - img_width / 2 <= 0:
            self.dx = -self.dx
        if self.y + img_height / 2 >= height or self.y - img_height / 2 <= 0:
            self.dy = -self.dy

        self.move(self.dx, self.dy)# вызов метода move

class App:# создание класса App
    def __init__(self, master, bg_image_path):# конструктор класса 
        #переменные
        self.master = master
        self.canvas = tk.Canvas(master, width=800, height=600)#создание окна
        self.canvas.pack()

        # Установка фонового изображения
        self.bg_image_tk = tk.PhotoImage(file=bg_image_path)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image_tk

        # Создаем два объекта с изображениями
        self.object1 = BouncingObject(self.canvas, 200, 150, 'УИТЛИL.PNG', 3, 4) №путь к изображению
        self.object2 = BouncingObject(self.canvas, 600, 450, 'модуль космоса1.png', -4,
                                      -3) №путь к изображению

        self.update() #вызов метода update

    def update(self):#создание метода update который обновляет положение объектов
        self.object1.update(self.canvas.winfo_width(), self.canvas.winfo_height())
        self.object2.update(self.canvas.winfo_width(), self.canvas.winfo_height())
        self.master.after(20, self.update)


root = tk.Tk()
root.title("анимация")#название окна 

#  путь к фоновому изображению
background_image_path = 'космос.png'
app = App(root, background_image_path)

#запуск цикла
root.mainloop()
