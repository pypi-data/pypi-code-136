import math
import random


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.force_x = 0
        self.force_y = 0

    def __repr__(self):
        return f"Node({self.x},{self.y})"

    def reset_force(self, apply_random_force=False):
        self.force_x = 0
        self.force_y = 0

        if apply_random_force:
            r_fx = (random.random()-0.5)*0.01
            r_fy = (random.random()-0.5)*0.01
            self.append_force(r_fx, r_fy)

    def append_force(self, fx, fy):
        self.force_x += fx
        self.force_y += fy

    def update_position(self, delta_time, max_displacement_squared=100):
        dx = delta_time * self.force_x
        dy = delta_time * self.force_y

        displacement_squared = dx * dx + dy * dy

        if (displacement_squared > max_displacement_squared):
            s = math.sqrt(max_displacement_squared / displacement_squared)
            dx = dx * s
            dy = dy * s

        self.x = self.x + dx
        self.y = self.y + dy
