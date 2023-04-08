class Shape:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"I am a {self.name}.")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def display_info(self):
        super().display_info()
        print(f"My width is {self.width} and my height is {self.height}.")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def display_info(self):
        super().display_info()
        print(f"My radius is {self.radius}.")

# Membuat objek Rectangle dan Circle
rect = Rectangle(5, 3)
circ = Circle(7)

# Memanggil method display_info pada objek Rectangle dan Circle
rect.display_info()
circ.display_info()
