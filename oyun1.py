#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
import random
import time
import locale
from karakterler import Player, Bullet
# locale.setlocale(locale.LC_ALL,'tr_TR.utf8')


# Renk tanımları
GREEN = (0, 128, 0)
LIME = (0, 255, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE1 = (15, 69, 75)
BLUE2 = (106, 144, 147)

# Ekran değerleri ayarla
WIDTH = 360
HEIGHT = 480
FPS = 30
CAPTION = "Oyunum"
running = False
skorY = 0
skorK = 0
# Pygame başlangıç ayarları ve pencere oluşturma
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

# Classes/ oyunda kullanılacak sınıflar

# functions/Oyunda kullanılcak Fonksiyonlar

# Game loop/oyun döngüsü


def oyun():
    # oyunda kullanılacak nesnelerin ilk başlatılması oyunda kullanılşcak değişkenler
    p1 = Player(int(WIDTH/2),HEIGHT-20,RED,0)
    p2 = Player(int(WIDTH/2),20,SILVER,1)
    butun_karakterler = pygame.sprite.Group()
    butun_karakterler.add(p1)
    butun_karakterler.add(p2)
    global running
    running = True
    while running:
        # keep loop running at the right speed
        # oyun hızının ayarlanması
        clock.tick(FPS)
        # Process inputs(events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                print("Oyun Kapatıldı")
                running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    b1= Bullet(p1.rect.centerx,p1.rect.top,YELLOW,-10)
                    butun_karakterler.add(b1)
                if event.key == pygame.K_LCTRL:
                    b2=Bullet(p2.rect.centerx,p2.rect.bottom+20,MAROON,10)
                    butun_karakterler.add(b2)
            if event.type == pygame.KEYUP:
                pass
        # update
        # Oyunda kullanılan nesnelerin değerlerinin değiştirilmesi x,y ses, renk vb
        butun_karakterler.update()

        ##draw / render
        # oyunda kullanılacak nesnelerin güncellenmiş değelere göre çizilmesi
        screen.fill(BLACK)
        butun_karakterler.draw(screen)

        # ekranın tekrar yeni çizimler ile güncellenmesi
        pygame.display.update()  # pygame.display.flip()


    # pygame.quit()
if __name__ == "__main__":
    oyun()
    pygame.quit()
