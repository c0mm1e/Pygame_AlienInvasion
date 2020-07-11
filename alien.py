import pygame,sys
from pygame.sprite import Sprite

class Alien(Sprite):
    #单个Alien
    def __init__(self,ai_settings,screen):
        #初始化Alien及其位置
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #加载Alien图像
        self.image=pygame.image.load(sys.path[0]+r'\images\alien.bmp')
        self.rect=self.image.get_rect()
        #初始化位置（屏幕左上角）
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #存储Alien的float位置
        self.x=float(self.rect.x)

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.left<=0 or self.rect.right>=screen_rect.right:
            return True

    def update(self):
        #移动Alien
        self.x+=self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x=self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)