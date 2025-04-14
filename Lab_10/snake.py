from insert import *
from update import *
from delete import *
from get import *

import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

#FPS
FPS = 5
FramePerSec = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

#цвета
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (211, 211, 211)

WIDTH = 600
HEIGHT = 600
CELL = 30
MAX_SCORE = WIDTH // CELL * HEIGHT// CELL - 3
SCORE = 0 
EATEN_FOOD = 0
LEVEL = 1

DISAPEAR = pygame.USEREVENT + 1

walls = [] 

Screen = pygame.display.set_mode((WIDTH, HEIGHT))
Screen.fill(WHITE)

#отрисовка серого поля 
def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(Screen, GRAY, (i * CELL, j * CELL, CELL, CELL), 1)

#отрисовка поля в клетку
def draw_grid_chess():
    colors = [WHITE, GRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(Screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

def generate_walls(level, snake, food):
    walls.clear()

    def is_safe(x, y):
        #проверяем, не пересекается ли с телом змейки или едой
        for segment in snake.body:
            if segment.x == x and segment.y == y:
                return False
        if food.pos.x == x and food.pos.y == y:
            return False
        return True

    if level == 2:
        for i in range(5, 15):
            if is_safe(i, 10):
                walls.append(Point(i, 10))
    elif level == 3:
        for i in range(5, 15):
            if is_safe(10, i):
                walls.append(Point(10, i))
    elif level == 4:
        for i in range(5, 15):
            if is_safe(i, i):
                walls.append(Point(i, i))

def draw_walls():
    for wall in walls:
        pygame.draw.rect(Screen, BLACK, (wall.x * CELL, wall.y * CELL, CELL, CELL))

#класс точки определяет позицию еды, змейки и ее элементов
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x}, {self.y}"

#класс змейки
class Snake:
    def __init__(self):
        self.body = [Point(0, 1), Point(0, 2), Point(0, 3)] #инициализирует змейку с тремя элементами цепочки
        self.dx = 1
        self.dy = 0
    
    def move(self): #функция движения, каждый елемент змейки получает координаты следующего елемента при движении
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x > WIDTH // CELL - 1:
            self.body[0].x = 0
        elif self.body[0].y > HEIGHT // CELL - 1:
            self.body[0].y = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // CELL - 1
        elif self.body[0].y < 0:
            self.body[0].y = HEIGHT // CELL - 1
    
    def draw(self):#функция отрисовки каждого элемента змейки
        head = self.body[0]
        pygame.draw.rect(Screen, RED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(Screen, YELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):#проверка столкновений
        global SCORE
        global FPS
        global LEVEL
        global EATEN_FOOD
        head = self.body[0]
        for segment in self.body[1:]:
            if segment.x == head.x and segment.y == head.y:#game over при столкновении головы с другим элементом змейки
                save_score(user_id, SCORE, LEVEL)

                SCORE = 0
                LEVEL = 1
                FPS = 5
                EATEN_FOOD = 0  
                
                time.sleep(1)
                Screen.fill(RED)
                Screen.blit(font.render("Game over", True, BLACK), (125,250))
                pygame.display.update()
                time.sleep(2)
                pygame.quit()
                sys.exit()
        
        for wall in walls:
            if head.x == wall.x and head.y == wall.y:
                save_score(user_id, SCORE, LEVEL)
                SCORE = 0
                LEVEL = 1
                FPS = 5
                EATEN_FOOD = 0
                time.sleep(1)
                Screen.fill(RED)
                Screen.blit(font.render("Game over", True, BLACK), (125,250))
                pygame.display.update()
                time.sleep(2)
                pygame.quit()
                sys.exit()
        if head.x == food.pos.x and head.y == food.pos.y:#съедение еды и увеличение змейки
            SCORE += random.randint(1, 4)#разный вес еды
            EATEN_FOOD += 1 #подсчет количества съеденной еды, нужный для победы, если свободные клетки закончатся
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self)
            if SCORE != 0 and SCORE % 3 == 0:
                FPS += 1
                LEVEL += 1
                generate_walls(LEVEL, snake, food)
        


            



class Food:#класс еды
    def __init__(self):#инициализация
        self.pos = Point(0, 0)

    def draw(self):#отрисовка еды
        pygame.draw.rect(Screen, GREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    
    def generate_random_pos(self, snake):#генерация случайной позиции
        while True:
            pygame.time.set_timer(DISAPEAR, 5000)#таймер исчезновения еды и появления ее в другом месте
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
        
            #проверяем, не находится ли новая позиция еды на теле змейки
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake.body):
                break  #если позиция свободна, выходим из цикла
        




food = Food()
snake = Snake()
food.generate_random_pos(snake)

username = input("Введите имя пользователя: ")
user_id = get_or_create_user(username) #Добавление или возвращение нового пользователя


SCORE, LEVEL = get_last_score(user_id) #Счет и уровень игрока

choice = input("Начать заново (y) или продолжить (n)? ").lower()

if choice == "y":
    SCORE = 0
    LEVEL = 1
else:
    SCORE, LEVEL = get_last_score(user_id)

generate_walls(LEVEL, snake, food)
FPS = 5 + (LEVEL - 1)



while True:
      
    #Цикл всех событий
    for event in pygame.event.get():
        if event.type == DISAPEAR:
            food.generate_random_pos(snake)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1 and snake.dy != 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1 and snake.dy != 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dx != 0 and snake.dy != 1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dx != 0 and snake.dy != -1:
                snake.dx = 0
                snake.dy = -1
            elif event.key == pygame.K_ESCAPE:
                save_score(user_id, SCORE, LEVEL)
                print("Игра на паузе. Счёт сохранён.")
                paused = True
                while paused:
                    for ev in pygame.event.get():
                        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                            paused = False
                        

    Screen.fill(BLACK)
    draw_grid_chess()
    snake.move()
    snake.check_collision(food)
    if EATEN_FOOD == MAX_SCORE:#победа, когда количество сьеденной еды не оставляет свободных ячеек на поле
        Screen.fill(GREEN)
        Screen.blit(font.render("You win", True, WHITE), (30,250))
          
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    snake.draw()
    food.draw()
    scores = font_small.render(str(SCORE), True, BLACK)
    level = font_small.render(f"level: {str(LEVEL)}", True, BLACK)
    Screen.blit(scores, (10, 10))
    Screen.blit(level, (500, 10))
    
    draw_walls()
    pygame.display.flip()
    FramePerSec.tick(FPS)
