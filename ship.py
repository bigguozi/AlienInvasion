import pygame
import settings
import math
from bullet import Bullet
from device import Device

class Ship():
    def __init__(self,screen,ai_settings):
        self.screen        = screen
        #初始化时设置各个移动变为0
        self.create_bullet = False          
        self.bullet_num    = ai_settings.bullet_num 
        self.shot_max_num  = ai_settings.shot_max_num 
        self.hit_reward    = ai_settings.hit_reward 
        self.ship_speed    = ai_settings.ship_speed
        self.bullet_list   = list()
        self.bullet_speed  = ai_settings.bullet_speed 
        self.max_hp        = ai_settings.ship_hp 
        self.hp            = self.max_hp
        self.ship_size     = ai_settings.ship_size
        self.device        = Device()
        self.angle         = 0.0 
        self.a             = 0.0
        # 飞船是否被摧毁
        self.crashed       = False
        # 飞船朝向            
        self.forward       = 'UP'
        self.image         = pygame.image.load('ship.png')
        #使用pygame.transform.scale来对输入图片进行处理
        self.image         = pygame.transform.scale(self.image,self.ship_size)
        self.rect          = self.image.get_rect()
        self.screen_rect   = screen.get_rect()
        # 加载飞船爆炸的图片
        self.explosion_image = pygame.image.load('explosion.png')
        #飞船爆炸图片转换
        self.explosion_image = pygame.transform.scale(self.explosion_image,self.ship_size)
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom  = self.screen_rect.bottom
    
    def blitme(self):
        #t_image = self.image
        t_image = pygame.transform.rotate(self.image,((self.angle)/math.pi)*180)
        if self.crashed :
            self.screen.blit(self.explosion_image,self.rect)
        else :
            self.screen.blit(t_image,self.rect)
        pygame.draw.arc(self.screen,(0,0,0),self.rect,0,2*math.pi,5)
        pygame.draw.arc(self.screen,(255,0,0),self.rect,0,(self.hp/self.max_hp)*2*math.pi,5)
        for all_bullet in self.bullet_list:
            if all_bullet.recthit :
                self.bullet_list.remove(all_bullet)
            else :
                all_bullet.update()
                all_bullet.blitme()
                
    def ship_bullet_load(self,val=1):
        self.bullet_num += val
    
    def ship_bullet_unload(self,val=1):
        self.bullet_num -= val
        
    def ship_hp_add(self,val=1):
        self.hp += val 
        
    def hit(self,val=1,godie=False):
        ''' 表示对该目标造成伤害，伤害数值为val,目标HP最低可降低至0 ,若HP降低至0，飞船将会设置Crashed标志为True,
        若godie设置为True目标HP直接清零'''
        self.hp = 0 if godie else self.hp-val ;
        self.hp = max(0,self.hp); #目标hp最低为0
        if self.hp == 0 :
            self.crashed = True  
        

    def update_bullet_list(self):
        # 建立新的子弹
        if self.create_bullet :
            if self.bullet_num > 0  and len(self.bullet_list)<self.shot_max_num :
                self.bullet_list.append(Bullet(self.screen,self,self.bullet_speed))
                self.bullet_num -= 1
            self.create_bullet = False
            
    def update(self):
        # 加载外部传感器数据
        sensorData=self.device.getSensorData()
        x_speed   = sensorData['ax']*self.ship_speed 
        y_speed   = sensorData['ay']*self.ship_speed 
        x_pos_new = self.rect.centerx - y_speed 
        y_pos_new = self.rect.centery - x_speed
        self.create_bullet =  sensorData['btn']
        
        # 检测运动后的飞船是否在屏幕内如果在的话进行坐标更新，否则坐标不变
        if self.screen_rect.collidepoint(x_pos_new,y_pos_new) :
            self.rect.centerx  = x_pos_new 
            self.rect.centery  = y_pos_new    
        self.angle = sensorData['angle']
        # 更新子弹列表
        self.update_bullet_list() 
        # 绘制飞船相关元素
        self.blitme()
        