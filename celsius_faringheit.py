class Temperature:

    temp = 25

    def __init__(self, celsius):
        self.__celsius = celsius

    def to_fahrenheit(self):
        temp = temp*9/5+32
        print(temp)