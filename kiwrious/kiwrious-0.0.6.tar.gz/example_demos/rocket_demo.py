import pygame
from kiwrious.service import KiwriousService
import sys
import os
from pygame.locals import *
import time


# This is a demo utilising the air quality sensor. Blowing on it will result in the rocket flying faster in space! 
# Simply plug in the sensor and run this program and the game will run. 
# NOTE: You must have pygame installed, to do this type in the command 'pip install pygame' into a terminal.


class ScrollingBackground:
    def __init__(self, screenheight, imagefile):
        self.img = pygame.image.load("example_demos/rocket_demo_images/" + imagefile)
        self.coord = [0, 0]
        self.coord2 = [0, -screenheight]
        self.y_original = self.coord[1]
        self.y2_original = self.coord2[1]

    def Show(self, surface):
        surface.blit(self.img, self.coord)
        surface.blit(self.img, self.coord2)

    def UpdateCoords(self, speed_y, time):
        distance_y = speed_y * time
        self.coord[1] += distance_y
        self.coord2[1] += distance_y
        
        if self.coord2[1] >= 0:
            self.coord[1] = self.y_original
            self.coord2[1] = self.y2_original


class HeroShip:

    def __init__(self, screenheight, screenwidth, imagefile):
        self.shape = pygame.image.load("example_demos/rocket_demo_images/" + imagefile)
        self.top = screenheight - self.shape.get_height()
        self.left = screenwidth/2 - self.shape.get_width()/2

    def Show(self, surface):
        surface.blit(self.shape, (self.left, self.top))

    def UpdateCoords(self, y):
        self.top = y - self.shape.get_height()/2


pygame.init()  # initialize pygame
clock = pygame.time.Clock()
screenwidth, screenheight = (700, 666)
screen = pygame.display.set_mode((screenwidth, screenheight))

# Set the framerate
framerate = 60

# Load the background image here. Make sure the file exists!
StarField = ScrollingBackground(screenheight*2, "background.png")
pygame.mouse.set_visible(0)
pygame.display.set_caption('Space Age Game')

my_service = KiwriousService()
my_service.start_service()

time.sleep(2)

timeout = 10
acc = 0
vel = 0
max_vel = 3000

while True:
    time = clock.tick(framerate)/1000.0
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            my_service.stop_service()
            sys.exit()

    Hero = HeroShip(screenheight, screenwidth, "ship.png")
    reading = my_service.get_sensor_reading(my_service.AIR_QUALITY)

    try:
        ppb, c02 = reading[0]
    except IndexError:
        print("NO SENSOR DETECTED")
        my_service.stop_service()
        sys.exit()

    acc = (ppb.data_value - vel) / 40
     
    if vel + acc > max_vel:
        vel = max_vel 
    else: 
        vel = vel + acc
    pos = screenheight - ((vel / max_vel) * (screenheight - (293/1.35))) - (293/3.25)

    # print('rounded_ppb:', ppb.data_value, 'acc:', acc, 'vel:', vel)

    Hero.UpdateCoords(pos)

    animation_speed = c02.data_value
    if c02.data_value < 0:
        animation_speed = 6000
    
    # Set new Background Coordinates and update the screen
    StarField.UpdateCoords(animation_speed, time)
    StarField.Show(screen)
    Hero.Show(screen)
    pygame.display.update()
