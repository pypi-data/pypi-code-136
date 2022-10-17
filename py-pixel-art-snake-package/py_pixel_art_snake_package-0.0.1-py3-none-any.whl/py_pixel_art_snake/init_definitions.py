from pickle import TRUE
import pygame
from pygame.locals import *
import sys
import os
#from functions import button, on_grid_random, input_box, load_and_scale_images,read_variable

#import pandas as pd

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Init_definitions():
    def __init__(self,menu_state, game_inputs, game_running, game_over_state, score_states, init_definitions, config_state, button,
                                             collision, direct_to_go, dist_to_go, input_box, load_and_scale_images, on_grid_random, read_variable, snake_showing,np,pd):
        
        variables = read_variable.main(np,pd)

        med_size_scale = (variables.screen_scale_x + variables.screen_scale_y)/2.0
        
        self.screen_resolution_selected = variables.screen_res
        self.screen_size_scale_x = variables.screen_scale_x
        self.screen_size_scale_y = variables.screen_scale_y

        self.screen = pygame.display.set_mode((self.screen_resolution_selected[0], self.screen_resolution_selected[1]))
        pygame.display.set_caption('Snake')
        
        self.COLOR_ACTIVE = pygame.Color(255,0,0)
        self.COLOR_INACTIVE = pygame.Color('lightskyblue3')

        self.FONT = pygame.font.Font(None, int(med_size_scale * 22))
        
        
        self.input_box1 = input_box.InputBox(
            self.screen_size_scale_x * 200, self.screen_size_scale_y * 288, self.screen_size_scale_x * 100, self.screen_size_scale_y * 25, self.COLOR_ACTIVE, self.COLOR_INACTIVE, self.FONT)
        
        self.input_boxes = [self.input_box1]
        
        font_path = resource_path('freesansbold.ttf')

        self.name_font = pygame.font.Font(
            font_path, int(med_size_scale * 28))
        
        self.name_screen = self.name_font.render('name', True, (255, 255, 255))
        self.name_rect = self.name_screen.get_rect()
        self.name_rect.midtop = (
            int(self.screen_size_scale_x * (600 / 4)), int(self.screen_size_scale_y * 288))
        

        # Macro definition for snake movement

        self.UP = 0
        self.RIGHT = 1
        self.DOWN = 2
        self.LEFT = 3

        # Scale of the screen
        
        self.new_game_img = load_and_scale_images.Load_and_scale_images('new_game.jpeg',self.screen_size_scale_x, self.screen_size_scale_y)
        self.score_img = load_and_scale_images.Load_and_scale_images('score.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.exit_img = load_and_scale_images.Load_and_scale_images('exit.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.pause_img = load_and_scale_images.Load_and_scale_images('pause.jpeg',self.screen_size_scale_x, self.screen_size_scale_y)
        self.game_over_img = load_and_scale_images.Load_and_scale_images('game_over.jpeg',self.screen_size_scale_x, self.screen_size_scale_y)
        self.start_img = load_and_scale_images.Load_and_scale_images('start.jpeg',self.screen_size_scale_x, self.screen_size_scale_y)
        self.grass_img = load_and_scale_images.Load_and_scale_images('grass.jpeg',self.screen_size_scale_x, self.screen_size_scale_y)
        self.start_menu_img =load_and_scale_images.Load_and_scale_images('Snake_menu.jpg',self.screen_size_scale_x, self.screen_size_scale_y)
        self.apple_img = load_and_scale_images.Load_and_scale_images('apple.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.pergaminho_img = load_and_scale_images.Load_and_scale_images('pergaminho.jpg',self.screen_size_scale_x, self.screen_size_scale_y)
        
        self.snake_head_up_img = load_and_scale_images.Load_and_scale_images('cabeça_cobra_top.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.snake_head_down_img = load_and_scale_images.Load_and_scale_images('cabeça_cobra_down.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.snake_head_left_img = load_and_scale_images.Load_and_scale_images('cabeça_cobra_left.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.snake_head_right_img = load_and_scale_images.Load_and_scale_images('cabeça_cobra_right.png',self.screen_size_scale_x, self.screen_size_scale_y)
        
        self.snake_head_up_eating_img = load_and_scale_images.Load_and_scale_images('cabeça_cobra_top_eating.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.snake_head_down_eating_img = load_and_scale_images.Load_and_scale_images('cabeça_cobra_down_eating.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.snake_head_left_eating_img = load_and_scale_images.Load_and_scale_images('cabeça_cobra_left_eating.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.snake_head_right_eating_img = load_and_scale_images.Load_and_scale_images('cabeça_cobra_right_eating.png',self.screen_size_scale_x, self.screen_size_scale_y)
        
        self.snake_gomo_top_img = load_and_scale_images.Load_and_scale_images('cobra_gomo_top.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.snake_gomo_down_img = load_and_scale_images.Load_and_scale_images('cobra_gomo_down.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.snake_gomo_img = load_and_scale_images.Load_and_scale_images('cobra_gomo.png',self.screen_size_scale_x, self.screen_size_scale_y)
        
        self.yes_img = load_and_scale_images.Load_and_scale_images('yes.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.no_img = load_and_scale_images.Load_and_scale_images('no.png',self.screen_size_scale_x, self.screen_size_scale_y)
        self.play_again_img = load_and_scale_images.Load_and_scale_images('play_again.png',self.screen_size_scale_x, self.screen_size_scale_y)
        
        
        
        # creating buttons

        self.new_game_button = button.Button(self.screen_size_scale_x * 250,self.screen_size_scale_y *  276, self.new_game_img)
        self.score_button = button.Button(self.screen_size_scale_x * 250, self.screen_size_scale_y * 305, self.score_img)
        self.exit_button = button.Button(self.screen_size_scale_x * 250, self.screen_size_scale_y * 360, self.exit_img)
        self.pause_button = button.Button(self.screen_size_scale_x * 10, self.screen_size_scale_y * 10, self.pause_img)
        self.game_over_button = button.Button(self.screen_size_scale_x * 250, self.screen_size_scale_y * 76, self.game_over_img)
        self.start_button = button.Button(self.screen_size_scale_x * 250,self.screen_size_scale_y *  275, self.start_img)
        self.yes_button = button.Button(self.screen_size_scale_x * 250,self.screen_size_scale_y *  250, self.yes_img)
        self.no_button = button.Button(self.screen_size_scale_x * 260,self.screen_size_scale_y *  290, self.no_img)

        self.rect_grass = self.grass_img.get_rect()
        self.rect_grass.topleft = (0, 0)

        self.rect_start_menu = self.start_menu_img.get_rect()
        self.rect_start_menu.topleft = (0, 0)

        self.rect_pergaminho = self.pergaminho_img.get_rect()
        self.rect_pergaminho.topleft = (0, 0)
        
        self.rect_play_again = self.play_again_img.get_rect()
        self.rect_play_again.topleft = (150, 200)


        self.pos_cobra = on_grid_random.on_grid_random(self.screen_size_scale_x, self.screen_size_scale_y)
        
        self.snake = [(self.pos_cobra[0], self.pos_cobra[1]), (self.pos_cobra[0] +
                                                               self.screen_size_scale_x * 10, self.pos_cobra[1]), (self.pos_cobra[0] + self.screen_size_scale_x * 20, self.pos_cobra[1])]
        #self.snake_skin = pygame.Surface((10, 10))
        #self.snake_skin.fill((217, 204, 58))  # Orange
        #self.snake_skin = self.snake_head_img

        self.apple_pos = on_grid_random.on_grid_random(self.screen_size_scale_x, self.screen_size_scale_y)
        
        self.snake_gomo = self.snake_gomo_img
        

        self.my_direction = self.LEFT

        self.clock = pygame.time.Clock()
        
        

        self.font = pygame.font.Font(font_path, 18)


        self.score = 0
        self.clock_ticking = 4

        self.dif_maca = None
        self.name_input = None
        self.name_putted = False
        self.score_screen = False
        self.write_score = False
        self.done = False
        self.game_over = False
        self.auto_mode = False
        self.try_again = True

        # leitura do score
        score_path = resource_path('Score.csv')

        self.df = pd.read_csv(score_path)
        self.name_highest_score = self.df.loc[0, 'name']
        self.score_planilha = self.df.loc[[0], 'score']
        self.score_planilha = pd.to_numeric(self.score_planilha)
        self.highest_score = int(self.score_planilha)

