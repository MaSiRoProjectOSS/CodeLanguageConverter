import math


class Vector3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.length = 3

    def add(self, other):

        self.x += other.x
        self.y += other.y
        self.z += other.z

    def sub(self, other):

        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def mul(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    def dot(self, other):

        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):

        x = self.y * other.z - \
            self.z * other.y
        y = self.z * other.x - \
            self.x * other.z
        z = self.x * other.y - \
            self.y * other.x
        return Vector3d(x, y, z)

    def magnitude(self):
        return math.sqrt(self.dot(self))

    def average(self):
        return sum([self.x, self.y, self.z]) / self.length
