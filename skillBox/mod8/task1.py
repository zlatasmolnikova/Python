class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self.__coordinates = coordinates
        self.__speed = speed
        self.__brand = brand
        self.__year = year
        self.__number = number

    def get_coordinates(self):
        return self.__coordinates

    def set_coordinates(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value has to be number")
        self.__coordinates = value

    def get_speed(self):
        return self.__speed

    def set_speed(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value has to be number")
        self.__speed = value

    def get_brand(self):
        return self.__brand

    def set_brand(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value has to be number")
        self.__brand = value

    def get_year(self):
        return self.__year

    def set_year(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value has to be number")
        self.__year = value

    def get_number(self):
        return self.__number

    def set_number(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value has to be number")
        self.__number = value

    def __str__(self):
        return f"__str__ method: self.coordinates = {self.__coordinates}, self.speed = {self.__speed}, self.brand = {self.__brand}, self.year = {self.__year}, self.number = {self.__number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return (pos_x <= self.__coordinates[0] <= width + pos_x) and (pos_y <= self.__coordinates[1] <= length + pos_y)


class Passenger():
    def __init__(self, passengers_capacity, number_of_passengers):
        self.__passengers_capacity = passengers_capacity
        self.__number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if not isinstance(passengers_capacity, (int, float)):
            raise ValueError("passengers_capacity has to be number")
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if not isinstance(number_of_passengers, (int, float)):
            raise ValueError("number_of_passengers has to be number")
        self.__number_of_passengers = number_of_passengers


class Cargo():
    def __init__(self, carrying):
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if not isinstance(carrying, (int, float)):
            raise ValueError("Carrying has to be number")
        self.__carrying = carrying


class Plane(Transport):

    def __init__(self, coordinates, speed, brand, year, number, height):
        Transport.__init__(self, coordinates, speed, brand, year, number)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, (int, float)):
            raise ValueError("Height has to be number")
        self.__height = height

plane1 = Plane((3, 4), 250, "bmw", 2018, 489, 20)


class Auto(Transport):

    def __init__(self,coordinates, speed, brand, year, number, mileage):
        super().__init__(coordinates, speed, brand, year, number)
        self.__mileage = mileage

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, mileage):
        if not isinstance(mileage, (int, float)):
            raise ValueError("Height has to be number")
        self.__mileage = mileage


class Ship(Transport):

    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.__port = port

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if not isinstance(port, str):
            raise ValueError("Port has to be string")
        self.__port = port


class Car(Auto):

    def __init__(self, coordinates, speed, brand, year, number, mileage):
        super().__init__(coordinates, speed, brand, year, number, mileage)


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, mileage, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number, mileage)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoAuto(Auto, Cargo):
    def __init__(self,coordinates, speed, brand, year, number, mileage, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number, mileage)
        Cargo.__init__(self, carrying)


class Boat(Ship):

    def __init__(self, coordinates, speed, brand, year, number, port):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)


class PassengerShip(Ship, Passenger):

    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoShip(Ship, Cargo):

    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)


class Airplane(Plane):
    def __init__(self, coordinates, speed, brand, year, number, height):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)


class PassengerPlane(Plane, Passenger):
    
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoPlane(Plane, Cargo):

    def __init__(self, coordinates, speed, brand, year, number, height, carrying):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Cargo.__init__(self, carrying)


class SeaPlane(Plane, Ship):

    def __init__(self, coordinates, speed, brand, year, number, height, port):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
