class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("The animal makes a sound.")

    def show_info(self):
        print(f"I am a {self.species} named {self.name}.")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

    def show_info(self):
        print(f"I am a {self.species} named {self.name} and I love to play with yarn.")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

    def show_info(self):
        print(f"I am a {self.species} named {self.name} and I love to fetch balls.")

# Membuat objek Animal, Cat, dan Dog
animal = Animal("generic animal", "unknown")
cat = Cat("Fluffy", "cat")
dog = Dog("Fido", "dog")

# Memanggil method make_sound dan show_info pada objek Animal, Cat, dan Dog
animal.make_sound()
animal.show_info()
cat.make_sound()
cat.show_info()
dog.make_sound()
dog.show_info()
