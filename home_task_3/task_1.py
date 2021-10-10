class Vehicle:
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed

    def move(self):
        print(f'Vehicle {self.brand} is moving!')

smart = Vehicle('Smart', 2000, 140)
camry = Vehicle('Camry', 2012, 223)

smart.move()
camry.move()






