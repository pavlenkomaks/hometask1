class Vehicle:
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed

    def move(self):
        print(f'Vehicle {self.brand} is moving!')


class Bus(Vehicle):
    def move(self):
        return f'Bus {self.brand} is moving with max speed {self.max_speed}'

    def set_max_speed(self, max_speed=70):
        self.max_speed = max_speed

honda = Bus('Honda', 1990, 90)
volvo = Bus('Volvo', 2001, 120)

honda.set_max_speed()
volvo.set_max_speed()
print(honda.move())
print(volvo.move())
