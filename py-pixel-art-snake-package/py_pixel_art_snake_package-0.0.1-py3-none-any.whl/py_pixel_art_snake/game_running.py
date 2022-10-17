##### 10 - Game over ####
from pickle import TRUE
import pygame
from pygame.locals import *
#from functions import on_grid_random, collision, dist_to_go, direct_to_go, snake_showing

from sys import exit



def Game_running(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador):
    config_jogador.game_over = False
    config_jogador.score = 0
    config_jogador.clock_ticking = 4
    
    while True:
        config_jogador.clock.tick(config_jogador.clock_ticking)
    
        if config_jogador.auto_mode:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    

            dist_maca = dist_to_go.dist_to_go(config_jogador.snake[0], config_jogador.apple_pos)
            config_jogador.my_direction = direct_to_go.direct_to_go(dist_maca, config_jogador.my_direction)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and config_jogador.my_direction != config_jogador.DOWN:
                        config_jogador.my_direction = config_jogador.UP
                    if event.key == pygame.K_DOWN and config_jogador.my_direction != config_jogador.UP:
                       config_jogador.my_direction = config_jogador.DOWN
                    if event.key == pygame.K_LEFT and config_jogador.my_direction != config_jogador.RIGHT:
                        config_jogador.my_direction = config_jogador.LEFT
                    if event.key == pygame.K_RIGHT and config_jogador.my_direction != config_jogador.LEFT:
                        config_jogador.my_direction = config_jogador.RIGHT

        # Check if snake collided with boundaries
        #if config_jogador.snake[0][0] >= config_jogador.screen_size_scale_x * 600 or config_jogador.snake[0][1] >= config_jogador.screen_size_scale_y * 600 or config_jogador.snake[0][0] < 0 or config_jogador.snake[0][1] < 0:
            #game_over = True
            #break

        # Check if the snake has hit itself

        for i in range(1, len(config_jogador.snake) - 1):
            c3 = config_jogador.snake[0][0] - config_jogador.snake[i][0]
            c4 = config_jogador.snake[0][1] - config_jogador.snake[i][1]
            if abs(c3) == 0 and abs(c4) == 0:
                config_jogador.game_over = True
                break
        
        
        if config_jogador.game_over:
            config_jogador.pos_cobra = on_grid_random.on_grid_random(config_jogador.screen_size_scale_x, config_jogador.screen_size_scale_y)
            config_jogador.snake = [(config_jogador.pos_cobra[0], config_jogador.pos_cobra[1]), (config_jogador.pos_cobra[0] +
                                                               config_jogador.screen_size_scale_x * 10, config_jogador.pos_cobra[1]), (config_jogador.pos_cobra[0] + config_jogador.screen_size_scale_x * 20, config_jogador.pos_cobra[1])]
            config_jogador.game_over = False
            
            break

        for i in range(len(config_jogador.snake) - 1, 0, -1):
            config_jogador.snake[i] = (config_jogador.snake[i-1][0], config_jogador.snake[i-1][1])
            
        config_jogador.screen.fill((0, 0, 0))

        config_jogador.screen.blit(config_jogador.grass_img, (config_jogador.rect_grass.x, config_jogador.rect_grass.y))
        
        if config_jogador.pause_button.draw(config_jogador.screen):
            game_paused = True
            while game_paused:
                config_jogador.screen.fill((0, 0, 0))
                config_jogador.screen.blit(config_jogador.grass_img, (config_jogador.rect_grass.x, config_jogador.rect_grass.y))
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                if config_jogador.pause_button.draw(config_jogador.screen):
                    game_paused = False
                
                config_jogador.screen.blit(score_font, score_rect)
                
                config_jogador.screen.blit(config_jogador.apple_img, config_jogador.apple_pos)
                
                snake_showing.Showing_snake(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador=config_jogador) 
                    
                pygame.display.update()
  

        config_jogador.screen.blit(config_jogador.apple_img, config_jogador.apple_pos)
        

        #Manual Mode

        # Actually make the snake move.
        if config_jogador.my_direction == config_jogador.UP:
            if config_jogador.snake[0][1] > 0:
                config_jogador.snake[0] = (config_jogador.snake[0][0], config_jogador.snake[0][1] -  config_jogador.screen_size_scale_y  * 10)
            else:
                config_jogador.snake[0] = (config_jogador.snake[0][0], config_jogador.snake[0][1]  + config_jogador.screen_size_scale_y * 600)
                
            
        if config_jogador.my_direction == config_jogador.DOWN:
            
            if config_jogador.snake[0][1] < config_jogador.screen_size_scale_y * 600:
            
                config_jogador.snake[0] = (config_jogador.snake[0][0], config_jogador.snake[0][1] + config_jogador.screen_size_scale_y  * 10)
            else:
                config_jogador.snake[0] = (config_jogador.snake[0][0], config_jogador.snake[0][1]  - config_jogador.screen_size_scale_y * 600)
            
            
        if config_jogador.my_direction == config_jogador.RIGHT:
            if config_jogador.snake[0][0] < config_jogador.screen_size_scale_x * 600:
                config_jogador.snake[0] = (config_jogador.snake[0][0] + config_jogador.screen_size_scale_x  * 10, config_jogador.snake[0][1])
            else:
                config_jogador.snake[0] = (config_jogador.snake[0][0]  - config_jogador.screen_size_scale_x * 600, config_jogador.snake[0][1])
            
            
        if config_jogador.my_direction == config_jogador.LEFT:
            if config_jogador.snake[0][0] > 0:
                config_jogador.snake[0] = (config_jogador.snake[0][0] - config_jogador.screen_size_scale_x  * 10, config_jogador.snake[0][1])
            else:
                config_jogador.snake[0] = (config_jogador.snake[0][0]  + config_jogador.screen_size_scale_x * 600, config_jogador.snake[0][1])


        score_font = config_jogador.font.render('Score: %s' % (config_jogador.score), True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (config_jogador.screen_size_scale_x * (600 - 120), config_jogador.screen_size_scale_y * 10)
        config_jogador.screen.blit(score_font, score_rect)
     
        snake_showing.Showing_snake(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador)
        
        pygame.display.update()

    return config_jogador
