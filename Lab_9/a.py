import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

#Уствновка фпс
FPS = 60
FramePerSec = pygame.time.Clock()

#Цвета
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Нужные переменные
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
COINS = 0
SCORE = 0
SPEED = 5 
SPEED_OF_COIN = 5

#Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#Фон и фоновая музыка
background = pygame.image.load("Lab_8/Resources/AnimatedStreet.png")
background_song = pygame.mixer.music.load("Lab_8/Resources/background.wav")
pygame.mixer.music.play(-1)

#Создание белого экрана
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Создание всех классов
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab_8/Resources/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        self.rect.move_ip(0, SPEED_OF_COIN)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -self.rect.bottom)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab_8/Resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -self.rect.bottom)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab_8/Resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Создание спрайтов       
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Добавление спрайтов в группы
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

while True:
      
    #Цикл всех событий
    for event in pygame.event.get():   
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Отрисовка счета
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    score_of_coins = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(score_of_coins, (360,10))

    #Движение всех спрайтов 
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #Коллизии между игроком и врагом
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('Lab_8/Resources/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        

    #Коллизии между игроком и монетой
    if pygame.sprite.spritecollideany(P1, coins):
        self_COINS = COINS
        COINS += random.randint(1, 4) #разный вес монет при столкновении
        if COINS // 4 > self_COINS // 4:   #изменение скорости в зависимости от набранных монет
            SPEED += 1
        for coin in coins:
            coin.rect.top = 0
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -coin.rect.bottom)

        
    pygame.display.update()
    FramePerSec.tick(FPS)
