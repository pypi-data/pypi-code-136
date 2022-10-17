import random

def on_grid_random(scale_x,scale_y):
    x = random.randint(0,int(scale_x * 58))
    y = random.randint(0,int(scale_y * 58))
    return (x * 10, y * 10)