import pygame
from pygame.sprite import Sprite

class Boat(Sprite):
    def __init__(self,game, isUp=True):
        super().__init__()
        self.hp = 100
        self.screen = game.screen
        self.screenrect = self.screen.get_rect()

        if isUp == True:
            self.image = pygame.image.load("images/player2.png")
        else:
            self.image = pygame.image.load("images/player1.png")

        self.rect = self.image.get_rect()

        if isUp==True:
            self.rect.midtop = self.screenrect.midtop
        else:
            self.rect.midbottom = self.screenrect.midbottom

        self.settings = game.settings
        self._x = float(self.rect.x)
        self.right = False
        self.left = False

    def update(self):
        if self.right == True and self.rect.right < self.screenrect.right:
            self._x += self.settings.BoatSpeed
        if self.left == True and self.rect.left > self.screenrect.left:
            self._x -= self.settings.BoatSpeed

        self.rect.x = self._x

    def Blitme(self):
        self.screen.blit(self.image,self.rect)