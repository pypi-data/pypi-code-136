from pickle import TRUE
import pygame
from pygame.locals import *
import pandas as pd

import sys
import os

from sys import exit



def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def Game_over_state(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador):
    
    score_path = resource_path('Score.csv')

    while True:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        if (config_jogador.score > config_jogador.highest_score):
            if (not config_jogador.write_score):
                df = pd.DataFrame({'name': [config_jogador.name_input],
        
                            'score': [config_jogador.score]})

                df.to_csv(score_path,index=False)
                config_jogador.write_score = True
                config_jogador.highest_score = config_jogador.score
                config_jogador.name_highest_score = config_jogador.name_input

        

        #if config_jogador.exit_button.draw(config_jogador.screen):
         #   pygame.quit()
          #  exit()
        
        highest_score_font = config_jogador.font.render(f'Top1_Name: {config_jogador.name_highest_score} Highest Score: {config_jogador.highest_score}', True, (250, 0, 0))
        highest_score_rect = highest_score_font.get_rect()
        highest_score_rect.topleft = (0, 10)
        

        score_font = config_jogador.font.render(f'Name: {config_jogador.name_input} Score: {config_jogador.score}', True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (config_jogador.screen_size_scale_x  * 0, config_jogador.screen_size_scale_y  * 30)

        config_jogador.screen.blit(highest_score_font, highest_score_rect)
        config_jogador.screen.blit(score_font, score_rect)
        
        config_jogador.screen.blit(config_jogador.play_again_img , config_jogador.rect_play_again)
        
        if config_jogador.yes_button.draw(config_jogador.screen):
            config_jogador.try_again = True
            break
        
        if config_jogador.no_button.draw(config_jogador.screen):
            config_jogador.try_again = False
            break
            

        #if config_jogador.new_game_button.draw(config_jogador.screen):
           # config_jogador.try_again = False
           # break
        
        
        #if config_jogador.start_button.draw(config_jogador.screen):
           # config_jogador.try_again = True
            #break
       # game_over_button.draw(screen)

        
        
        pygame.display.update()
    
        
    return config_jogador
    
    
