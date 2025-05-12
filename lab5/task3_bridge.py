class Shape:
    def render(self):
        pass

class Circle(Shape):
    def render(self):
        print("Rendering Circle")

class Square(Shape):
    def render(self):
        print("Rendering Square")

class Triangle(Shape):
    def render(self):
        print("Rendering Triangle")

class VectorRender(Shape):
    def render(self):
        print("Drawing shape as vectors")

class RasterRender(Shape):
    def render(self):
        print("Drawing shape as pixels")
