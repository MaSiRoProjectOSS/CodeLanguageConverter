import copy
from vector_3d import Vector3d


class Person:
    def __init__(self):
        self.position = Vector3d(0, 0, 0)
        self.velocity = Vector3d(0, 0, 0)
        self.acceleration = Vector3d(1, 0, 0)

        self.timestep = 0.01
        self.walk_amount_max = 100

    def walk(self):
        vel_dif = copy.deepcopy(self.acceleration)
        vel_dif.mul(self.timestep)
        self.velocity.add(vel_dif)

        pos_dif = copy.deepcopy(self.velocity)
        pos_dif.mul(self.timestep)
        self.position.add(pos_dif)

        walk_amount = self.position.magnitude()

        if walk_amount > self.walk_amount_max:
            walk_amount = self.walk_amount_max

        return walk_amount
