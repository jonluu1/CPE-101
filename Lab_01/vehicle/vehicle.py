class Vehicle:
    def __init__(self, wheels, fuel, doors, roof):
        self.wheels = int(wheels)
        self.fuel = int(fuel)
        self.doors = int(doors)
        self.roof = bool(roof)
