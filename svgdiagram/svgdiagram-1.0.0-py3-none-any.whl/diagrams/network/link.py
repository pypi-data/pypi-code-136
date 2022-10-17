import math


class Link:
    def __init__(self, start_node, end_node, length, k_spring):
        self.start_node = start_node
        self.end_node = end_node

        self.length = length
        self.k_spring = k_spring

    def __repr__(self):
        return f"{self.start_node}-({self.length}/{self.k_spring})->{self.end_node}"

    def append_force(self):
        raise NotImplementedError


class LinearLink(Link):
    def append_force(self):
        dx = self.end_node.x - self.start_node.x
        dy = self.end_node.y - self.start_node.y

        distance = math.sqrt(dx * dx + dy * dy)

        if distance == 0:
            return

        force = self.k_spring * (distance - self.length)
        fx = force * dx / distance
        fy = force * dy / distance

        self.start_node.append_force(fx, fy)
        self.end_node.append_force(-fx, -fy)
