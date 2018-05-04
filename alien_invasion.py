import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from item import Item
from device import Device
import game_functions as gf
from button import Button
from alien_list import Alien_list
def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    bg_color    = (230,230,230)
    ai_settings = Settings()
    screen      = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height),pygame.FULLSCREEN)
    #screen      = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship        = Ship(screen,ai_settings)
    active      = False
    pause       = False
    alien_list  = Alien_list(screen,ai_settings)
    item_list   = []
    start_button      = Button(screen.get_rect().centerx,screen.get_rect().centery,screen,"Start Game")
    pause_button= Button(0,80,screen,"Pause")
    
    
    
    
    
    #
    #
    #
    while not active :
        screen.fill(ai_settings.bg_color)
        start_button.draw_button()
        pygame.display.flip()
        event=gf.check_events()
        if start_button.clicked_check(event["mouse_x"],event["mouse_y"]) :
            active = True
            
    while active : 
        if not pause :
            gf.update_screen(ai_settings,screen,ship,alien_list,item_list)
        #若游戏处在激活状态则运行
        event=gf.check_events()
        if pause_button.clicked_check(event["mouse_x"],event["mouse_y"]) :
            pause = not pause
        pause_button.draw_button()
        #更新显示界面
        pygame.display.flip()
run_game()
