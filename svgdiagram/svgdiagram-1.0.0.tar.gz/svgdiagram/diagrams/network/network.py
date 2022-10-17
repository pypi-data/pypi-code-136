import math


class Network:
    def __init__(self):
        self.nodes = []
        self.links = []

    def append_node(self, node):
        self.nodes.append(node)
        return node

    def append_link(self, link):
        assert link.start_node in self.nodes, \
            f'Start node of link "{link}" not part of Network!'
        assert link.end_node in self.nodes, \
            f'End node of link "{link}" not part of Network!'
        self.links.append(link)
        return link

    def _sim_step(self, delta_time, k_r, apply_random_force):
        for node in self.nodes:
            node.reset_force(apply_random_force=apply_random_force)

        for index, node1 in enumerate(self.nodes):
            for node2 in self.nodes[index+1:]:
                dx = node2.x - node1.x
                dy = node2.y - node1.y

                if dx != 0 and dy != 0:
                    # TODO: Consider proper use case
                    # of too close situation that both are drifted slowly
                    # apart
                    dist_squared = dx * dx + dy * dy
                    dist = math.sqrt(dist_squared)

                    force = k_r / dist_squared

                    fx = force * dx / dist
                    fy = force * dy / dist

                    node1.append_force(-fx, -fy)
                    node2.append_force(fx, fy)

        for link in self.links:
            link.append_force()

        for node in self.nodes:
            node.update_position(delta_time)

    def simulate(self, apply_random_force=False):
        # L = 50, K_r = 6250, K_s = 1,
        # delta_t = 0.04, R = 0.05.
        for index in range(5000):
            print(index)
            self._sim_step(0.04, 6250, apply_random_force=apply_random_force)
