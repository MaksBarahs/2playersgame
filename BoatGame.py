import pygame
import sys

from bullet import Bullet
from settings import Settings
from Boat import Boat

class BoatGame():
    def __init__(self):
        # инициализация движка
        pygame.init()

        # создание экрана и установка размеров
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption("BoatGame")

        self.settings = Settings()
        self.boats = pygame.sprite.Group()

        self.boats.add(Boat(self,isUp=False))
        self.boats.add(Boat(self, isUp=True))

        self.bullets1 = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()
    def Fire(self, isUp):
        bullet = Bullet(self, isUp)
        if isUp == True:
            self.bullets2.add(bullet)
        else:
            self.bullets1.add(bullet)
    def Start(self):
        while True:
            # Чекаем события
            self.ChekEvents()
            # Обновляем лодки
            self.boats.update()
            self.UpdateBullets()
            # Обновляем экран
            self.UpdateScreen()

    def ChekEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.ChekDown(event)
            elif event.type == pygame.KEYUP:
                self.ChekUp(event)

    def ChekDown(self, event):
        if event.key == pygame.K_d:
            self.boats.sprites()[0].right = True
        elif event.key == pygame.K_a:
            self.boats.sprites()[0].left = True
        elif event.key == pygame.K_RIGHT:
            self.boats.sprites()[1].right = True
        elif event.key == pygame.K_LEFT:
            self.boats.sprites()[1].left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_KP_ENTER:
            self.Fire(True)
        elif event.key == pygame.K_SPACE:
            self.Fire(False)


    def ChekUp(self, event):
        if event.key == pygame.K_d:
            self.boats.sprites()[0].right = False
        elif event.key == pygame.K_a:
            self.boats.sprites()[0].left = False
        elif event.key == pygame.K_RIGHT:
            self.boats.sprites()[1].right = False
        elif event.key == pygame.K_LEFT:
            self.boats.sprites()[1].left = False

    def UpdateBullets(self):
        self.bullets1.update()
        self.bullets2.update()

        # УДАЛЯЕМ НЕНУЖНЫЕ ПУЛИ
        for bullet in self.bullets1.copy():
            if bullet.rect.bottom <= 0:
                self.bullets1.remove(bullet)

        for bullet in self.bullets2.copy():
            if bullet.rect.bottom >= self.screen.get_height():
                self.bullets1.remove(bullet)

    def UpdateScreen(self):
        self.screen.fill((122,187,240))

        for boat in self.boats.sprites():
            boat.Blitme()

        for bullet in self.bullets1.sprites():
            bullet.Blitme()
        for bullet in self.bullets2.sprites():
            bullet.Blitme()
        pygame.display.flip()

spase = BoatGame()
spase.Start()
