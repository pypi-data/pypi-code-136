from likeprocessing.processing import *

def setup():
    createCanvas(400,200)
    background("grey")
    noLoop()
def compute():
    for i in range(10):
        print_var(i)
    redraw()

def draw():
    pass

run(globals())