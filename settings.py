class Settings():
    def __init__(self):
        #屏幕设置
        self.screen_width=1080
        self.screen_height=720
        self.bg_color=(230,230,230)
        #飞船属性设置
        self.ship_limit=3
        #Alien设置
        self.fleet_drop_speed=10
        #子弹设置
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed=5
        #加速
        self.speedup_scale=1.1

        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.alien_speed_factor=0.75
        self.bullet_speed_factor=1.25
        self.fleet_direction=1
    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale       
