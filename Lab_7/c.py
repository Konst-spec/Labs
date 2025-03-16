import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
done = False
is_blue = True
x, y = 600, 400

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y - 25 > 0:
        y -= 20
    if pressed[pygame.K_DOWN] and y + 25 < screen.get_height():  
        y += 20
    if pressed[pygame.K_LEFT] and x - 25 > 0:  
        x -= 20
    if pressed[pygame.K_RIGHT] and x + 25 < screen.get_width():  
        x += 20

    screen.fill((255, 255, 255))
    color = (0, 128, 255) if is_blue else (255, 100, 0)
    pygame.draw.circle(screen, color, (x, y), 25)

    pygame.display.flip()
    clock.tick(60)