import pygame
import math
class Settings():
    """存储项目中设置的类"""
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 960
        self.bg_color     = (230,230,230)
        self.enemy_num    = 8
        self.score        = 0
        self.bullet_num   = 10
        self.shot_max_num = 3
        self.hit_reward   = 4
        self.ship_speed   = 50
        self.enemy_speed  = 60
        self.enemy_hp     = 4
        self.ship_hp      = 8
        self.enemy_size   = (90,90)
        self.ship_size    = (60,60)
        self.ship_angle_inc = math.pi/5 
        self.bullet_speed = 40
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg,(self.screen_width,self.screen_height))
        self.hp_item_str = 'hp_item.png'
        self.item_dict={'hp_item':self.hp_item_str}
        self.item_size= (96,50)