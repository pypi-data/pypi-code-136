## THIS DECK FILE IS FOR TESTING THE TEST CASES FOR DETECTOR ###
class Quantos:

    def __init__(self):
        front_door_testing = True
    
    def test_front_door_position(self):
        return 'OPEN'

class Robot:

    def __init__(self):
        robot_testing = True
    
    def test_get_robot_pos(self):
        pos = {'x': 22, 'y': -159436}
        return pos

quan = Quantos()
robo = Robot()