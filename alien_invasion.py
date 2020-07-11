import sys,pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #初始化
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建Play按钮
    play_button=Button(ai_settings,screen,"Play")
    #创建统计
    stats=GameStats(ai_settings)
    #创建飞船
    ship=Ship(ai_settings,screen)
    #创建一个存储子弹的编组
    bullets=Group()
    #创建Alien的编组
    aliens=Group()
    #创建Alien的Group
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #主循环
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)

run_game()