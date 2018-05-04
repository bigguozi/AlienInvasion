#alien 类规划
#需要实现功能：
#类的创建于删除应该置于更高的一层的列表中
#该类仅仅实现外星人的显示与血值控制功能
import random
import math
import pygame
from item import Item
class Alien():
    def __init__(self,screen,ai_settings):
        # 设置敌人所在屏幕
        self.screen = screen
        self.ai_settings = ai_settings
        self.image    = pygame.image.load('alien.png')
        self.enemy_size= ai_settings.enemy_size
        #self.hp  = ai_settings.enemy_hp 
        self.max_hp  = random.randint(1,ai_settings.enemy_hp)
        self.hp  = self.max_hp
        # 将外星人资源图片处理到标准大小
        self.image  = pygame.transform.scale(self.image,self.enemy_size)
        # 加载外星人爆炸的图片
        self.explosion_image = pygame.image.load('explosion.png')
        #外星人爆炸图片转换
        self.explosion_image = pygame.transform.scale(self.explosion_image,self.enemy_size)
        # 获取外星人与显示窗口的大小
        self.rect     = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 初始化外星人坐标(在屏幕范围内产生随机数)
        self.x_pos  = random.randint(1,self.screen_rect.width)
        self.y_pos  = random.randint(1,self.screen_rect.height)
        # 配置外星人坐标 
        self.rect.centerx = self.x_pos 
        self.rect.centery = self.y_pos
        # 外星人是否被击中
        self.crashed= False
        # 外星人移动速度
        self.speed  =ai_settings.enemy_speed
        
    def blitme(self):
        # 若飞碟被碰撞则绘制爆炸图案
        if self.hp == 0 :
            self.screen.blit(self.explosion_image,self.rect)
        else :
            self.screen.blit(self.image,self.rect)
        self.draw_hp_bar()
    
    def draw_hp_bar(self):
        pygame.draw.arc(self.screen,(0,0,0),self.rect,0,2*math.pi,5)
        pygame.draw.arc(self.screen,(255,0,0),self.rect,0,(self.hp/self.max_hp)*2*math.pi,5)
    
    def random_move(self,val=64):
        '''随机产生一定范围内的位移'''
        #随机生成外星人的运动方向
        dir   = random.randint(1,val)
        # 根据生成的dir与speed确定下一次的位移量
        if dir == 1 and self.rect.right + self.speed < self.screen_rect.right :
            self.x_pos += self.speed 
        elif dir == 2 and self.rect.left - self.speed > self.screen_rect.left :
            self.x_pos -= self.speed 
        elif dir == 3 and self.rect.top - self.speed > self.screen_rect.top :
            self.y_pos -= self.speed
        elif dir == 4 and self.rect.bottom + self.speed < self.screen_rect.bottom:
            self.y_pos += self.speed
        self.rect.centerx = self.x_pos 
        self.rect.centery = self.y_pos
         
    def hit(self,val=1,godie=False):
        ''' 表示对该目标造成伤害，伤害数值为val,目标HP最低可降低至0 ,若HP降低至0，飞船将会设置Crashed标志为True,
        若godie设置为True目标HP直接清零'''
        self.hp = 0 if godie else self.hp-val ;
        self.hp = max(0,self.hp); #目标hp最低为0
        if self.hp == 0 :
            self.crashed = True
    
    
    def hitcheck(self,rect):
        '''用于检测子弹是否再外星人所在矩形内,是返回True反之返回False'''
        if self.rect.colliderect(rect) :
            return True 
        else :
            return False 
    def rect_get(self):
        '''用于获得外星人所在矩形'''
        return self.rect 
    
    def death_check(self):
        '''检测目标外形人是否死亡，如果死亡返回True，否则返回False'''
        return True if self.hp==0 else False ;
        