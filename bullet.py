import pygame
from pygame import Rect
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,game, isUp = True):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.isUp = isUp

        if isUp == True:
            self.boat = game.boats.sprites()[1]
        else:
            self.boat = game.boats.sprites()[0]


        if isUp == True:
            self.image = pygame.image.load("images/bullet2.png")
        else:
            self.image = pygame.image.load("images/bullet1.png")

        self.rect = self.image.get_rect()

        if isUp == True:
            self.rect.midtop = self.boat.rect.midbottom
        else:
            self.rect.midbottom = self.boat.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        if not self.isUp:
            self.y -= self.settings.bulletspeed
            self.rect.y = self.y
        else:
            self.y += self.settings.bulletspeed
            self.rect.y = self.y


    def Blitme(self):
        self.screen.blit(self.image, self.rect)
