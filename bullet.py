import pygame
import math
class Bullet():
    def __init__(self,screen,ship,speed):
        self.screen  = screen
        self.image   = pygame.image.load('bullet.png')
        self.image   = pygame.transform.scale(self.image,(40,40))
        self.rect    = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.forward = ship.forward
        self.recthit = False
        self.speed   = speed
        self.angle   = ship.angle
        self.rect.centerx =ship.rect.centerx
        self.rect.centery =ship.rect.centery
        self.image   = pygame.transform.rotate(self.image,((self.angle)/math.pi)*180)

    def blitme(self):
              self.screen.blit(self.image,self.rect)

    def update(self):
        x_div = self.speed * math.cos(self.angle) ;
        y_div = self.speed * math.sin(self.angle) ;
        x_pos_new = self.rect.centerx - y_div;
        y_pos_new = self.rect.centery - x_div ;
        
        if self.screen_rect.collidepoint(x_pos_new,y_pos_new) == False :
            self.recthit = True
        
        self.rect.centerx = x_pos_new ;
        self.rect.centery = y_pos_new ;


