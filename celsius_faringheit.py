class Temperature:

    def __init__(self, celsius):
        self.__celsius = celsius

    def to_fahrenheit(self, fahrenheit):
        self.fahrenheit = fahrenheit
        self.fahrenheit = (temp * (9/5) + 32)
    def get_celsius(self):
        return self.__celsius

temp = Temperature(25)
temp.to_fahrenheit = (temp * (9/5) + 32)
print(temp.to_fahrenheit)
print(temp.get_celsius())