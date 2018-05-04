import pygame
class Item():
    def __init__(self,screen,rect,type,ai_settings):
        """初始化物品
        screen      : 物品显示到的屏幕
        type        : 物品类型
        ai_settings : 系统设置参数集
        """
        # 确定物品被绘制到的界面
        self.screen = screen
        # 加载物品对应的图片（存储在ai_settings中的字典里）
        self.image  = pygame.image.load(ai_settings.item_dict[type]) 
        # 加载物品大小
        self.item_size = ai_settings.item_size
        # 将加载图片转换为设定大小
        self.image = pygame.transform.scale(self.image,self.item_size)
        # 获取物品所在矩形
        self.rect = self.image.get_rect()
        # 配置物品坐标
        self.rect.centerx = rect.centerx
        self.rect.centery = rect.centery
        
    def blitme(self):
        """绘制出物品"""
        self.screen.blit(self.image,self.rect)
        
    def hitcheck(self,rect):
        if self.rect.colliderect(rect) :
            return True 
        else :
            return False 