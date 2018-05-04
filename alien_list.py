import pygame
from alien import Alien
class Alien_list():
    def __init__(self,screen,ai_settings):
        self.screen     =   screen 
        self.ai_settings=   ai_settings 
        self.enemy_max  =   ai_settings.enemy_num
        self.alien_list =   [] 
    
    def alien_auto_create(self):
        '''该函数将alien的个数动态维持在系统所设定的上限'''
        while len(self.alien_list) < self.enemy_max :
            self.alien_create()
    
    def alien_create(self):
        '''用于新建一个外星人，新建成功时返回True，新建失败返回False'''
        #只有当当前alien_list中元素个数小于规定的最大上限数才可以新建外星人
        if len(self.alien_list) < self.enemy_max :
            self.alien_list.append(Alien(self.screen,self.ai_settings))
            return True
        return False
    
    def alien_hit_check(self,rect,val=1,godie=False):
        '''用于检测输入的rect是否在所有的alien内，所有与rect相交的alien血量减1，返回True，若均不相交返回False'''
        status = False
        for alien in self.alien_list :
            if alien.rect.colliderect(rect):
                alien.hit(val=val,godie=godie)
                status = True
        return status
        

    def alien_death_check(self,remove = True):
        '''该函数将会检测列表中所有HP降低至0的alien,并返回数目'''
        '''2018/4/29修改，返回为对应外星人的rect列表'''
        #death_num = 0 
        death_rect_list = []
        for alien in self.alien_list :
            if alien.death_check() :
                #death_num += 1
                death_rect_list.append(alien.rect_get())
                if remove : # 如果remove设置为True将会从列表中移除该外星人
                    self.alien_list.remove(alien) 
        return death_rect_list
        
    def alien_update(self):
        '''更新外星人的位移'''
        for alien in self.alien_list :
            alien.random_move()
            alien.blitme()
            
            