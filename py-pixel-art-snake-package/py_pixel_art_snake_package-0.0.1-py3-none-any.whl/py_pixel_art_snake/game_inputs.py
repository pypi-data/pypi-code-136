from pickle import TRUE
import pygame
from pygame.locals import *
import os
import sys

from sys import exit

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)



def Game_inputs(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador):
    
    font_path = resource_path('freesansbold.ttf')
    while True:

        config_jogador.screen.fill((0,0,0))
        
        
        if config_jogador.name_input == None:

            config_jogador.screen.blit(config_jogador.start_menu_img, (config_jogador.rect_start_menu.x, config_jogador.rect_start_menu.y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                for box in config_jogador.input_boxes:
                        config_jogador.name_input = box.handle_event(event)    

            for box in config_jogador.input_boxes:
                    box.update()

            for box in config_jogador.input_boxes:
                    box.draw(config_jogador.screen)
            
            
            
            config_jogador.screen.blit(config_jogador.name_screen, config_jogador.name_rect)


        else:
            config_jogador.screen.fill((0,0,0))
            config_jogador.screen.blit(config_jogador.start_menu_img, (config_jogador.rect_start_menu.x, config_jogador.rect_start_menu.y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if config_jogador.start_button.draw(config_jogador.screen):

                break

            name_input_font = pygame.font.Font(font_path, 75)
            name_input_screen = name_input_font.render(config_jogador.name_input, True, (255, 255, 255))
            name_input_rect = name_input_screen.get_rect()
            name_input_rect.midtop = (config_jogador.screen_size_scale_x * int(600 / 2), config_jogador.screen_size_scale_y * 10)
            
            config_jogador.screen.blit(name_input_screen, name_input_rect)
        
        pygame.display.update()

    return config_jogador