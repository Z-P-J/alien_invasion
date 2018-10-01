
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """初始化飞船并设置其初始位置"""
    def __init__(self, ai_setting, screen):
        super(Ship, self).__init__()
        
        self.ai_setting = ai_setting
        self.screen = screen

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        #更新飞船的center值， 而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #向右移动飞船
            self.center += self.ai_setting.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            #向左移动飞船
            self.center -= self.ai_setting.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.center


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕的中间"""
        self.center = self.screen_rect.centerx