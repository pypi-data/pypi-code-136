#from functions import collision, on_grid_random
#import pygame


def Showing_snake(menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd, config_jogador):

    if collision.collision(config_jogador.snake[0], config_jogador.apple_pos):
                
        for i in range (len(config_jogador.snake) - 1 , -1, -1):
                    
            if config_jogador.my_direction == config_jogador.UP:
                if i == 0:
                    config_jogador.screen.blit(config_jogador.snake_head_up_eating_img , (config_jogador.snake[i][0] - 10 ,config_jogador.snake[i][1]))
                else:
                            
                    config_jogador.screen.blit(config_jogador.snake_gomo_top_img, config_jogador.snake[i])
                            
            if config_jogador.my_direction == config_jogador.DOWN:
                if i == 0:
                    config_jogador.screen.blit(config_jogador.snake_head_down_eating_img , (config_jogador.snake[i][0] -10 ,config_jogador.snake[i][1]))
                else:
                    config_jogador.screen.blit(config_jogador.snake_gomo_down_img, config_jogador.snake[i])
                            
            if config_jogador.my_direction == config_jogador.LEFT:
                if i == 0:
                    config_jogador.screen.blit(config_jogador.snake_head_left_eating_img , (config_jogador.snake[i][0] ,config_jogador.snake[i][1] - 10))
                else:
                    config_jogador.screen.blit(config_jogador.snake_gomo_img, config_jogador.snake[i])
                            
            if config_jogador.my_direction == config_jogador.RIGHT:
                if i == 0:
                    config_jogador.screen.blit(config_jogador.snake_head_right_eating_img , (config_jogador.snake[i][0]   ,config_jogador.snake[i][1] - 10))
                else:
                    config_jogador.screen.blit(config_jogador.snake_gomo_img, config_jogador.snake[i])                 

                
        config_jogador.apple_pos = on_grid_random.on_grid_random(config_jogador.screen_size_scale_x , config_jogador.screen_size_scale_y)
        config_jogador.snake.append((0, 0))
        config_jogador.score +=  1
        config_jogador.clock_ticking += 1
                
    else:
        for i in range (len(config_jogador.snake) - 1 , -1, -1):
            if config_jogador.my_direction == config_jogador.UP:
                if i == 0:
                    config_jogador.screen.blit(config_jogador.snake_head_up_img , (config_jogador.snake[i][0] - 10 ,config_jogador.snake[i][1]))
                else:
                    config_jogador.screen.blit(config_jogador.snake_gomo_down_img, config_jogador.snake[i])
                            
            if config_jogador.my_direction == config_jogador.DOWN:
                if i == 0:
                    config_jogador.screen.blit(config_jogador.snake_head_down_img , (config_jogador.snake[i][0] - 10 ,config_jogador.snake[i][1]))
                else:
                    config_jogador.screen.blit(config_jogador.snake_gomo_down_img, config_jogador.snake[i])
                            
            if config_jogador.my_direction == config_jogador.LEFT:
                if i == 0:
                    config_jogador.screen.blit(config_jogador.snake_head_left_img , (config_jogador.snake[i][0] ,config_jogador.snake[i][1] - 10))
                else:
                    config_jogador.screen.blit(config_jogador.snake_gomo_img, config_jogador.snake[i])
                            
            if config_jogador.my_direction == config_jogador.RIGHT:
                if i == 0:
                    config_jogador.screen.blit(config_jogador.snake_head_right_img , (config_jogador.snake[i][0] ,config_jogador.snake[i][1] - 10))
                else:
                    config_jogador.screen.blit(config_jogador.snake_gomo_img, config_jogador.snake[i])
                        
    #pygame.display.update()