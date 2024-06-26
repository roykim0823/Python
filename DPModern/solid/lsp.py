class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if self.is_square():
            raise RuntimeError("Set width is not allowed in a square.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if self.is_square():
            raise RuntimeError("Set height is not allowed in a sqaure.")
        self._height = value

    # to detect squre
    def is_square(self):
        return self._width == self._height

    class Factory:
        @staticmethod
        def create_rectangle(x, y):
            return Rectangle(x, y)
        @staticmethod
        def create_square(size):
            return Rectangle(size, size)


def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle.Factory.create_rectangle(2, 3)
use_it(rc)

sq = Rectangle.Factory.create_square(5)
use_it(sq)
