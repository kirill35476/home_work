class Temperature:

    def __init__(self, celsius):
        self.__celsius = celsius

    def to_fahrenheit(self, fahrenheit):
        self.fahrenheit = fahrenheit
    def get_celsius(self):
        return self.__celsius

temp = Temperature(25)
fahrenheit = temp * 9 / 5 + 32
print(fahrenheit)
print(temp.get_celsius())


