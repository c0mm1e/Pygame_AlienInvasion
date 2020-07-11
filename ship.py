import pygame,sys

class Ship():
    #初始化飞船及其位置
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图像
        self.image=pygame.image.load(sys.path[0]+r'\images\ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #初始化位置（屏幕底部中央）
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        #在飞船的属性Center中存储float
        self.center=float(self.rect.centerx)
        #移动标志
        self.moving_right=False
        self.moving_left=False

    #根据移动标志调整飞船位置
    def update(self):
        #更新飞船的center值
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed_factor
        #更新rect对象
        self.rect.centerx=self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center=self.screen_rect.centerx