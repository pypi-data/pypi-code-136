
##### 10 - Game over ####
from pickle import TRUE
import pygame
from pygame.locals import *
import sys
import os
from sys import exit

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def Score_states(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador):
    
    font_path = resource_path('freesansbold.ttf')
    while True:

        config_jogador.screen.fill((0,0,0))
        config_jogador.screen.blit(config_jogador.pergaminho_img, (config_jogador.rect_pergaminho.x, config_jogador.rect_pergaminho.y))

        highest_score_defined_font = pygame.font.Font(font_path, 30)
        highest_score_font = highest_score_defined_font.render(f'Name: {config_jogador.name_highest_score}  Highest Score: {config_jogador.highest_score}', True, (0, 0, 0))
        highest_score_rect = highest_score_font.get_rect()
        highest_score_rect.topleft = (config_jogador.screen_size_scale_x * 0, config_jogador.screen_size_scale_y * 10)
        config_jogador.screen.blit(highest_score_font, highest_score_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if config_jogador.exit_button.draw(config_jogador.screen):
            break
        pygame.display.update()

        

