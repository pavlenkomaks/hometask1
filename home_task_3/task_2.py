class Vehicle:
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed

    def move(self):
        print(f'Vehicle {self.brand} is moving!')

    def set_max_speed(self, max_speed=70):
        self.max_speed = max_speed

class Bus(Vehicle):

    def __init__(self, brand, year_of_production):
        super().__init__(brand, year_of_production, 70)
    def move(self):
        return f'Bus {self.brand} is moving with max speed {self.max_speed}'



honda = Bus('Honda', 1990)
volvo = Bus('Volvo', 2001)

volvo.set_max_speed(99)

print(honda.move())
print(volvo.move())
