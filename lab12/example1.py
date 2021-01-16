class Cylinder() :
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def base_area(self):
        return 3.14 * (self.radius ** 2)

    def surface_area(self):
        return 2 * 3.14 * self.height

    def area(self):
        return 2 * self.base_area() + self.surface_area()

    def volume(self):
        return self.base_area() * self.height

cylinder1 = Cylinder(3,5)
print(cylinder1.volume())
