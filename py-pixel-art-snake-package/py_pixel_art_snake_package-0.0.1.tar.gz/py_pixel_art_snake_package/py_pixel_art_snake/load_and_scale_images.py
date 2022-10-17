import pygame
import sys
import os


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def Load_and_scale_images(path,scale_x,scale_y):
    path_to_reach = resource_path(path)
    image = pygame.image.load(path_to_reach).convert_alpha()
    image = pygame.transform.scale(image, (int(image.get_width() * scale_x), int(image.get_height() * scale_y)))
    return image
    