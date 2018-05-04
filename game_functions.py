import sys
import pygame
import math
import random
from item import Item

# 检查各种事件
def check_events():
    mouse_x = 0
    mouse_y = 0
    clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE :
                pygame.quit()
                exit()        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            clicked         = True
        
    event = {"mouse_x":mouse_x,"mouse_y":mouse_y,"clicked":True}
    return event     
            
                
        
            
def show_text(surface_handle, pos, text, color = (255,0,0), font_bold = False, font_size = 48, font_italic = False):   
    #获取系统字体，并设置文字大小  
    cur_font = pygame.font.SysFont("宋体", font_size)  
    #设置是否加粗属性  
    cur_font.set_bold(font_bold)  
    #设置是否斜体属性  
    cur_font.set_italic(font_italic)  
    #设置文字内容  
    text_fmt = cur_font.render(text, 1, color)  
    #绘制文字  
    surface_handle.blit(text_fmt, pos)   
        
def end_screen():
    """ 游戏结束界面 """
    
        
def game_process(ai_settings,screen,ship,alien_list,item_list):
    
    # 更新飞船
    ship.update()
    # 根据设置中最大的外星人数量自动生成外星人
    alien_list.alien_auto_create()
    # 检测所有子弹与外星人是否出现碰撞，如果有删除子弹同时外星人HP降低
    for bullet in ship.bullet_list:
        if alien_list.alien_hit_check(bullet.rect) :
            ship.bullet_list.remove(bullet)
    # 检测外星人与飞船的碰撞，如果碰撞，则外星人直接狗带
    if alien_list.alien_hit_check(ship.rect,godie=True) :
        ship.hit()
    # 检测HP值降低至零的外星人的数目，并将其从列表中移除
    alien_death_rect_list= alien_list.alien_death_check()
    alien_death_num      = len(alien_death_rect_list)
    # 根据杀死外星人的数目为飞船加载奖励子弹
    ship.ship_bullet_load(alien_death_num*ai_settings.hit_reward)
    # 根据外星人的死亡数目增加分数
    ai_settings.score += alien_death_num
    # 绘制外星人列表中的所有外星人
    alien_list.alien_update()

    # 更新外星人列表
    for rect in alien_death_rect_list :
        if random.randint(1,3) <= 1 :
            item_list.append(Item(screen,rect,'hp_item',ai_settings))
    
    # 更新物品列表
    for item in item_list :
        # 如果相重合则飞船回血，删除血瓶
        if item.hitcheck(ship.rect):
            ship.ship_hp_add()
            item_list.remove(item)
        else :
            item.blitme()    
        
   
        
# 更新屏幕绘制内容  
def update_screen(ai_settings,screen,ship,alien_list,item_list):
    #screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg, (0, 0))  
    show_text(screen,(0,0),'Score:' + str(ai_settings.score))
    show_text(screen,(0,50),'Bullet Num:' + str(ship.bullet_num))
    game_process(ai_settings,screen,ship,alien_list,item_list)
    #当子弹数变为0的时候游戏结束
    if ship.bullet_num == 0 or ship.crashed :
        screen.fill((230,230,230)) 
        show_text(screen,(0,300),'Game Over! Your Score is : '+ str(ai_settings.score)+'!',color=(0,0,0),font_size=100)
    #pygame.display.flip()
