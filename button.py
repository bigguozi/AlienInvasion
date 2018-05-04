import pygame
class Button():
    def __init__(self,x,y,screen,text):
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.text   = text
        self.text_color = pygame.Color('black')
        self.button_color = pygame.Color('yellow')
        self.width = 100
        self.height = 50
        self.font = pygame.font.SysFont(None,24)
        self.rect = pygame.Rect(x,y,self.width,self.height)
        #self.rect.center = self.screen_rect.center
        self.text_image_convert(text)
        
    def text_image_convert(self,text):
        self.text_image = self.font.render(text,True,self.text_color,self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        pygame.draw.rect(self.screen,self.text_color,self.rect,1)
        self.screen.blit(self.text_image,self.text_image_rect)
        
    def clicked_check(self,x,y):
        return self.rect.collidepoint(x,y)
    