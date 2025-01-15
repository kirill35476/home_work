import tkinter as tk
import math


class BaseAnimationApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Анимации")
        self.geometry("600x400")

        self.canvas = tk.Canvas(self, width=600, height=400)
        self.canvas.pack()

        self.start_animations()


class CombinedAnimations(BaseAnimationApp):
    def start_animations(self):
        self.circle_moving()

        self.square_rotating()

    def circle_moving(self):

        self.circle = self.canvas.create_oval(100, 150, 200, 250, fill="red", outline="black")

        self.direction = 5

        self.animate_circle()

    def animate_circle(self):
        x1, y1, x2, y2 = self.canvas.coords(self.circle)
        if x2 >= 550:
            self.direction = -5
        elif x1 <= 10:
            self.direction = 5

        self.canvas.move(self.circle, self.direction, 0)
        self.after(50, self.animate_circle)

    def square_rotating(self):

        self.square = self.canvas.create_polygon(50, 50, 150, 50, 150, 350, 50, 350, fill="blue", outline="black")

        self.angle = 0

        self.rotate_square()

    def rotate_square(self):

        coords = self.canvas.coords(self.square)

        center_x = sum(coords[::2]) / 4
        center_y = sum(coords[1::2]) / 4

        rotated_coords = []
        for i in range(0, len(coords), 2):
            rotated_coords.extend(self.rotate_point(center_x, center_y, coords[i], coords[i + 1]))

        self.canvas.delete(self.square)
        self.square = self.canvas.create_polygon(rotated_coords, fill="blue", outline="black")

        self.angle += 1
        if self.angle > 360:
            self.angle -= 360

        self.after(20, self.rotate_square)

    def rotate_point(self, cx, cy, x, y):

        s = self.sin(self.angle)
        c = self.cos(self.angle)

        x -= cx
        y -= cy

        new_x = x * c - y * s
        new_y = x * s + y * c

        return [new_x + cx, new_y + cy]

    def sin(self, angle):
        return round(10000 * math.sin(math.radians(angle))) / 10000

    def cos(self, angle):
        return round(10000 * math.cos(math.radians(angle))) / 10000


app = CombinedAnimations()
app.mainloop()
