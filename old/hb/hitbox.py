class Hitbox:

    def __init__(self,x,y,width,height):
        self.__x = x
        self.__y =y
        self.__set_width(width)
        self.__set_height(height)

#set and get
    def __get_width(self):
        return  self.__width

    def __set_width(self,width):
        if width < 0:
            width = 0
        self.__width = width

    def __get_height(self):
        return self.__height

    def __set_height(self, height):
        if height < 0:
            height = 0
        self.__height = height

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        self.__x = x

    def __get_y(self):
        return self.__y

    def __set_y(self, y):
        self.__y = y

# высота x и низ y
    def __get_top(self):
        return  self.y

    def __get_bottom(self):
        return self.y + self.height

    def __get_left(self):
        return  self.x

    def __get_right(self):
        return self.x + self.width

#moveto and move
    def moveto(self, x, y):
        self.__set_x(x)
        self.__set_y(y)

    def move(self, dx, dy):
        self.__set_x(dx + self.__get_x())
        self.__set_y(dy + self.__get_y())

#property
    x = property(__get_x,__set_x)
    y = property(__get_y, __set_y)
    width = property(__get_width, __set_width)
    height = property(__get_height, __set_height)

    top = property(__get_top)
    bottom = property(__get_bottom)
    left = property(__get_left)
    right = property(__get_right)

#intersects
    def intersects(self, other):
        if self.left > other.right:
            return False
        if self.right < other.left:
            return False
        if self.top > other.bottom:
            return False
        if self.bottom < other.top:
            return False
        return True

    def intersects1(self, other1):
        if self.left > other1.right:
            return False
        if self.right < other1.left:
            return False
        if self.top > other1.bottom:
            return False
        if self.bottom < other1.top:
            return False
        return True

    def intersects2(self, other2):
        if self.left > other2.right:
            return False
        if self.right < other2.left:
            return False
        if self.top > other2.bottom:
            return False
        if self.bottom < other2.top:
            return False
        return True

    def __str__(self):
        return (f'({self.__x =},{self.__y = },'
                f'{self.__width = },{self.__height=})')