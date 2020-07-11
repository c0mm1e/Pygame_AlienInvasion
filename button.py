import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        #按钮属性
        self.width,self.height=300,75
        self.button_color=(0,0,205)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,72)
        #创建按钮的rect对象
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        #只需创建一次按钮的标签
        self.prep_msg(msg)
    def prep_msg(self, msg):
        #将msg渲染为图像，并使其居中
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
