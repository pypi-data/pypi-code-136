# https://codereview.stackexchange.com/questions/264080/a-simple-noise-visualizer-made-using-pygame-gui


from pickle import TRUE
from matplotlib import container
import pygame
from pygame.locals import *
import pygame_gui
import pandas as pd

from pygame_gui.elements.ui_drop_down_menu import UIDropDownMenu

from sys import exit

import sys
import os

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
#from def_states import init_definitions
#from pygame_gui.core.ui_container import UIContainer
#from functions import screen_resolutions

def Config_state(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador):
    config_path = resource_path('config.csv')
    
    pygame.BUTTON_LEFT = 1
    pygame.BUTTON_MIDDLE = 2
    pygame.BUTTON_RIGHT = 3
    screen_1 = "600 x 600"
    screen_2 = "800 x 800"
    screen_sizes = [screen_1, screen_2]
    manager = pygame_gui.UIManager(
        (config_jogador.screen_resolution_selected[0], config_jogador.screen_resolution_selected[1]))
    
    if config_jogador.screen_resolution_selected[0] == 600:
        first_screen_size = 0

    else:
        first_screen_size = 1
        
    screen_resolution_drop_menu = UIDropDownMenu(manager=manager, relative_rect=pygame.Rect(
            (config_jogador.screen_size_scale_x * 10, config_jogador.screen_size_scale_y * 50), (config_jogador.screen_size_scale_x * 200, config_jogador.screen_size_scale_y * 24)), options_list=screen_sizes, starting_option=screen_sizes[first_screen_size])
   
    while True:
        config_jogador.screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == screen_resolution_drop_menu:

                    if screen_resolution_drop_menu.selected_option == screen_sizes[0]:
                        config_jogador.screen_resolution_selected = [600, 600]
                        config_jogador.screen_size_scale_x = 1.0
                        config_jogador.screen_size_scale_y = 1.0
                        
                        df = pd.read_csv(config_path,sep=',',index_col = "Name_variables")
                        df.loc['screen_res'] = [600, 600]
                        df.loc['screen_scale_x'] = [1.0, None]
                        df.loc['screen_scale_y'] = [1.0, None]
                        df.to_csv(config_path,index=True)
                        
                    else:
                        config_jogador.screen_resolution_selected = [800, 800]
                        config_jogador.screen_size_scale_x = config_jogador.screen_resolution_selected[0]/600
                        config_jogador.screen_size_scale_y = config_jogador.screen_resolution_selected[1]/600
                        df = pd.read_csv(config_path,index_col = "Name_variables")
                        
                        df.loc['screen_scale_x'] = [800/600, None]
                        df.loc['screen_scale_y'] = [800/600, None]
                        df.loc['screen_res'] = [800, 800]
                        
                        df.to_csv(config_path,index=True)
                        

            manager.process_events(event)

        screen_resolution_drop_menu.update(60.0/1000.0)
       

        screen_size_render = config_jogador.font.render(
            f'Screen Size', True, (255, 255, 255))
        screen_size_rect = screen_size_render.get_rect()
        screen_size_rect.topleft = (
            config_jogador.screen_size_scale_x * 10, config_jogador.screen_size_scale_y * 10)

        config_jogador.screen.blit(screen_size_render, screen_size_rect)

        if config_jogador.exit_button.draw(config_jogador.screen):
            break
        
        manager.update(60.0/1000.0)
        manager.draw_ui(config_jogador.screen)

        pygame.display.update()

    config_jogador = init_definitions.Init_definitions(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd)

    return config_jogador
