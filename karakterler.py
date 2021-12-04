import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,renk,oyuncu):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,20))
        self.image.fill(renk)
        self.rect =self.image.get_rect()
        self.rect.center=(x,y)
        self.hiz=0
        self.oyuncu=oyuncu

    def update(self):
        self.hiz=0
        tuslar = pygame.key.get_pressed()
        # print(tuslar)
        if self.oyuncu==0:
            if tuslar[pygame.K_LEFT]:
                self.hiz=-5
            elif tuslar[pygame.K_RIGHT]:
                self.hiz=5
        if self.oyuncu==1:
            if tuslar[pygame.K_a]:
                self.hiz=-5
            elif tuslar[pygame.K_d]:
                self.hiz=5


        self.rect.x+=self.hiz
        if self.rect.left>360:
            self.rect.right=0
        elif self.rect.right<0:
            self.rect.left=360


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,renk,hiz):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(renk)
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.bottom=y
        self.hiz=hiz
    def update(self):
        self.rect.y += self.hiz
        if self.rect.bottom<0 or self.rect.top>480:
            self.kill()