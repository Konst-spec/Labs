import pygame, sys, math


pygame.init()
screen = pygame.display.set_mode((640, 480))
basescreen = pygame.Surface((640, 480))
clock = pygame.time.Clock()

Thickness = 15

#координаты мыши
x = 0
y = 0

#координаты мыши при нажатии лкм
x1 = 0
y1 = 0

#начальный цвет
mode = 'blue'
LMBP = False
screen.fill((0, 0, 0))

#начальный режим
figure = "risovat"

#определение прямоугольника
def calc_rect(x1, y1, x, y):
    return pygame.Rect(min(x, x1), min(y, y1), abs(x - x1), abs(y - y1))

#определение квадрата
def calc_square(x1, y1, x, y):
    side = min(abs(x - x1), abs(y - y1))
    if x < x1: 
        x = x1 - side
    if y < y1:
        y = y1 - side
    return pygame.Rect(min(x1, x), min(y1, y), side, side)

#определение прямоугольного треугольника
def right_triangle(x1, y1, x, y):
    return [(x1, y1), (x, y1), (x1, y)]

#определение равностороннего треугольника
def equilateral_triangle(x1, y1, x, y):
    side = max(abs(x - x1), abs(y - y1))#сторона квадрата внутри которого треугольник

    p1 = (x1, y1 - side)
    p2 = (x1 - side // 2, y1)
    p3 = (x1 + side // 2, y1)

    return [p1, p2, p3]  

#определение ромба
def rhombus(x1, y1, x, y):
    p1 = ((x + x1) / 2, y1) #беру середины от стороно прямоугольника межды начальными и настоящими координатами
    p2 = (x1, (y + y1) / 2)
    p3 = ((x + x1) / 2, y)
    p4 = (x, (y + y1) / 2)

    return [p1, p2, p3, p4]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = 'red'
            elif event.key == pygame.K_2:
                mode = 'green'
            elif event.key == pygame.K_3:
                mode = 'blue'
            elif event.key == pygame.K_4:
                mode = "black"
            elif event.key == pygame.K_c:
                figure = "circle"
            elif event.key == pygame.K_r:
                figure = "rect"
            elif event.key == pygame.K_s:
                figure = "square"
            elif event.key == pygame.K_a:
                figure = "risovat"
            elif event.key == pygame.K_p:
                figure = "r_triangle"
            elif event.key == pygame.K_e:
                figure = "e_triangle"
            elif event.key == pygame.K_h:
                figure = "rhombus"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            LMBP = True
            x1 = event.pos[0]
            y1 = event.pos[1]
         
            
            
            
        #отрисовки при зажатой лкм
        if event.type == pygame.MOUSEMOTION:
            #отрисовка прямоугольника
            if LMBP and figure == "rect":
                x = event.pos[0]
                y = event.pos[1]
                basescreen.blit(basescreen, (0, 0))
                pygame.draw.rect(screen, mode, calc_rect(x1, y1, x, y))  
            #отрисовка круга
            elif LMBP and figure == "circle":
                x = event.pos[0]
                y = event.pos[1]
                basescreen.blit(basescreen, (0, 0))
                rect = calc_rect(x1, y1, x, y)
                pygame.draw.ellipse(screen, mode, rect)
            #отрисовка обычного режиса рисования
            elif LMBP and figure == "risovat":
                pygame.draw.circle(screen, mode, (x1, y1), Thickness)
                x1, y1 = event.pos  
                basescreen.blit(screen, (0, 0))
            #отрисовка квадрата
            elif LMBP and figure == "square":
                x = event.pos[0]
                y = event.pos[1]
                basescreen.blit(screen, (0, 0))
                pygame.draw.rect(screen, mode, calc_square(x1, y1, x, y))
            #отрисовка прямоугольного треугольника
            elif LMBP and figure == "r_triangle":
                x = event.pos[0]
                y = event.pos[1]
                basescreen.blit(screen, (0, 0))
                pygame.draw.polygon(screen, mode, right_triangle(x1, y1, x, y))
            #отрисовка правильного треугольника
            elif LMBP and figure == "e_triangle":
                x = event.pos[0]
                y = event.pos[1]
                basescreen.blit(screen, (0, 0))
                pygame.draw.polygon(screen, mode, equilateral_triangle(x1, y1, x, y))
            #отрисовка ромба
            elif LMBP and figure == "rhombus":
                x = event.pos[0]
                y = event.pos[1]
                basescreen.blit(screen, (0, 0))
                pygame.draw.polygon(screen, mode, rhombus(x1, y1, x, y))

        #отрисовки при отжатии лкм
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBP = False
            x = event.pos[0]
            y = event.pos[1]
            if figure == "rect":
                pygame.draw.rect(screen, mode, calc_rect(x1, y1, x, y))
            elif figure == "circle":
                rect = calc_rect(x1, y1, x, y)
                pygame.draw.ellipse(screen, mode, rect)
            elif figure == "square":
                pygame.draw.rect(screen, mode, calc_square(x1, y1, x, y))
            elif figure == "r_triangle":
                pygame.draw.polygon(screen, mode, right_triangle(x1, y1, x, y))
            elif figure == "e_triangle":
                pygame.draw.polygon(screen, mode, equilateral_triangle(x1, y1, x, y))
            elif figure == "rhombus":
                pygame.draw.polygon(screen, mode, rhombus(x1, y1, x, y))
            basescreen.blit(screen, (0, 0))
            
             
        pygame.display.flip()
        screen.blit(basescreen, (0, 0))   
    
    
    clock.tick(100000)