from array import array
from math import hypot

class Vector2d():

    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in(self.x,self.y))

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    # @staticmethod
    def get_x(x):
        return x


if __name__ == '__main__':
    v1 = Vector2d(2,4)
    print(v1.get_x(7))
