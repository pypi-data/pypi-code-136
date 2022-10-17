from distutils.command import config
from multiprocessing import Manager
from pickle import TRUE
import pygame
from pygame.locals import *
#from def_states import score_states,config_state,init_definitions
import pygame_gui

from sys import exit




def Menu_state(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd):
    
    config_jogador = init_definitions.Init_definitions(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd)
    config_states_menu = False
    manager = pygame_gui.UIManager(
        (config_jogador.screen_resolution_selected[0], config_jogador.screen_resolution_selected[1]))
    config_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((config_jogador.screen_size_scale_x * 250, config_jogador.screen_size_scale_y * 336), (config_jogador.screen_size_scale_x * 100, config_jogador.screen_size_scale_y * 24)),
                                             text='Config.',
                                             manager=manager)
    
    while True:
        
        config_jogador.screen.fill((0,0,0))
        config_jogador.screen.blit(config_jogador.start_menu_img, (config_jogador.rect_start_menu.x, config_jogador.rect_start_menu.y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == config_button:
                  config_states_menu = True
                  
            manager.process_events(event)
        
        
        
        if config_states_menu:
            
           config_jogador = config_state.Config_state(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador=config_jogador)
           config_button.kill()
           config_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((config_jogador.screen_size_scale_x * 250, config_jogador.screen_size_scale_y * 336), (config_jogador.screen_size_scale_x * 100, config_jogador.screen_size_scale_y * 24)),
                                             text='Config.',
                                             manager=manager)
           
           config_states_menu = False
        
        if config_jogador.exit_button.draw(config_jogador.screen):
            pygame.quit()
            exit()

        if config_jogador.start_button.draw(config_jogador.screen):
            break

        if config_jogador.score_button.draw(config_jogador.screen):
           
            score_states.Score_states(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd,config_jogador=config_jogador)
            
        manager.update(60.0/1000.0)
        manager.draw_ui(config_jogador.screen)            

        
        pygame.display.update()
    
    return config_jogador
        
        