class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def drive(self):
        print(f"The {self.name} is driving with a maximum speed of {self.max_speed} km/h.")

class Car(Vehicle):
    def drive(self):
        print(f"The {self.name} car is driving with a maximum speed of {self.max_speed} km/h.")

class Motorcycle(Vehicle):
    def drive(self):
        print(f"The {self.name} motorcycle is driving with a maximum speed of {self.max_speed} km/h.")

# Membuat objek Vehicle, Car, dan Motorcycle
vehicle = Vehicle("generic vehicle", 100)
car = Car("Honda Civic", 200)
motorcycle = Motorcycle("Kawasaki Ninja", 300)

# Memanggil method drive pada objek Vehicle, Car, dan Motorcycle
vehicle.drive()
car.drive()
motorcycle.drive()
