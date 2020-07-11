import sys,pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    #单击Play按钮时开始新游戏
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置统计信息
        stats.reset_stats()
        stats.game_active=True
        #与Ship_hit类似
        aliens.empty()
        bullets.empty()
        #创建新的Aliens
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
    #监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button):
    #重绘背景
    screen.fill(ai_settings.bg_color)
    #绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #绘制Ship和Alien
    ship.blitme()
    aliens.draw(screen)
    #绘制Play
    if not stats.game_active:
        play_button.draw_button()
    #使最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    #更新子弹位置
    bullets.update()
    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)
    
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    #检查碰撞
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    #若Aliens被全部消灭，重建一群Aliens
    if len(aliens)==0:
        #bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)<ai_settings.bullet_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings,alien_width):
    #左右Alien之间的默认间距为Alien的宽度
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=available_space_x//(2*alien_width)
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    #上下Alien之间的默认间距为Alien的宽度
    available_space_y=ai_settings.screen_height-3*alien_height-ship_height
    number_rows=available_space_y//(2*alien_height)
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    #创建一个Alien的Group
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width*(2*alien_number+1)
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height*(2*row_number+1)
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    #计算一行最多Alien容纳数
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #创建所有Alien
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    if stats.ships_left>0:
        stats.ships_left-=1
        aliens.empty()
        bullets.empty()
        #创建新的Aliens
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #暂停
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    #更新所有Alien位置
    aliens.update()
    #检测碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    #检测触底
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

