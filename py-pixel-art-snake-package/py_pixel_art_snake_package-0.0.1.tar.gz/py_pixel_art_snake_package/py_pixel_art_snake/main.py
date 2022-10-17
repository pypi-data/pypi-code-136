
# Adapt from: https://github.com/filhoweuler/Pygame-Snake/tree/master
# Adapt from: https://github.com/russs123/pygame_tutorials/tree/main/Button
# Text Input: https://www.ti-enxame.com/pt/python/como-criar-uma-caixa-de-entrada-de-texto-com-pygame/83411323

from pickle import NONE
import pygame
from pygame.locals import *
from py_pixel_art_snake_package.py_pixel_art_snake import menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state
from py_pixel_art_snake_package.py_pixel_art_snake import button, collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing
import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath('/home/caio/Games/Snake'))

from sys import exit

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#if getattr(sys, 'frozen', False):
 #   os.chdir(sys._MEIPASS)
    
#if getattr(sys, 'frozen', False):
 #  os.chdir(os.path.dirname(sys.executable))

# Inicialização

pygame.mixer.init()

audio_dir = resource_path("menu_music.mp3")

menu_music = pygame.mixer.Sound(audio_dir)
pygame.mixer.music.load(audio_dir)
pygame.mixer.music.play(-1)

pygame.init()

while True:

    config_jogador = menu_state.Menu_state(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions,config_state,
                                           button, collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd)

    config_jogador = game_inputs.Game_inputs(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador=config_jogador)

    while config_jogador.try_again:

        config_jogador = game_running.Game_running(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador=config_jogador)

        config_jogador = game_over_state.Game_over_state(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador=config_jogador)
