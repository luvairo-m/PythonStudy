class Transport:
    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, value):
        self.__coords = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value if value != "" else self.__brand

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value if value >= 0 else self.__speed

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value if value > 0 and isinstance(value, int) else self.__year

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value if isinstance(value, int) else self.__number

    def __init__(self, coords, speed, brand, year, number):
        self.__coords = []
        self.__speed = self.__year = self.__number = 0
        self.__brand = "default"

        self.coords = coords
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        return (f"<- Transport unit ->\nSpeed: {self.speed}\nBrand: {self.brand}\nYear: {self.year}\n"
                f"Coordinates: x = {self.coords[0]}, y = {self.coords[1]}\nNumber: {self.number}")

    def is_in_area(self, pos_x, pos_y, length, height) -> bool:
        return (pos_x >= self.coords[0] >= pos_x + length) and (pos_y >= self.coords[1] >= pos_y + height)


class Passenger:
    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, value):
        if isinstance(value, int) and value >= 0:
            self.__passengers_capacity = value

    @property
    def number_of_passengers(self):
        return self.__passengers_amount

    @number_of_passengers.setter
    def number_of_passengers(self, value):
        if isinstance(value, int) and value >= 0:
            self.__passengers_amount = value

    def __init__(self, capacity, amount):
        self.__passengers_capacity = self.__passengers_amount = 0
        self.passengers_capacity = capacity
        self.number_of_passengers = amount


class Cargo:
    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, value):
        if isinstance(value, int) and value >= 0:
            self.__carrying = value

    def __init__(self, carrying):
        self.__carrying = 0
        self.carrying = carrying


class Plane(Transport):
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value >= 0:
            self.__height = value

    def __init__(self, height, coords, speed, brand, year, number):
        super().__init__(coords, speed, brand, year, number)
        self.__height = 0
        self.height = height


class Auto(Transport):
    def __init__(self, coords, speed, brand, year, number):
        super().__init__(coords, speed, brand, year, number)


class Ship(Transport):
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value != "":
            self.__name = value

    def __init__(self, name, coords, speed, brand, year, number):
        super().__init__(coords, speed, brand, year, number)
        self.__name = "default"
        self.name = name


class Car(Auto):
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def __init__(self, coords, speed, brand, year, number):
        super().__init__(coords, speed, brand, year, number)
        self.__model = "default"


class Bus(Auto, Passenger):
    def __init__(self, coords, speed, brand, year, number, capacity, amount):
        super().__init__(coords, speed, brand, year, number)
        self.passengers_capacity = capacity
        self.number_of_passengers = amount


class CargoAuto(Auto, Cargo):
    def __init__(self, coords, speed, brand, year, number, carrying):
        super().__init__(coords, speed, brand, year, number)
        self.carrying = carrying


class Boat(Ship):
    def __init__(self, name, coords, speed, brand, year, number):
        super().__init__(name, coords, speed, brand, year, number)


class PassengerShip(Ship, Passenger):
    def __init__(self, name, coords, speed, brand, year, number, capacity, amount):
        super().__init__(name, coords, speed, brand, year, number)
        self.passengers_capacity = capacity
        self.number_of_passengers = amount


class CargoShip(Ship, Cargo):
    def __init__(self, name, coords, speed, brand, year, number, carrying):
        super().__init__(name, coords, speed, brand, year, number)
        self.carrying = carrying


if __name__ == "__main__":
    transport = Transport([10, 15], 140, "Toyota", 1995, 11199333)
    print(transport)
