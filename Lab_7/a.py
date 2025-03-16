import pygame
import os
import datetime

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((1200, 800))
done = False
clock = pygame.time.Clock()
mclock = get_image('clock.png')
min_hand_or = get_image('min_hand.png')
sec_hand_or = get_image('sec_hand.png')
min_hand = get_image('min_hand.png')
sec_hand = get_image('sec_hand.png')



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    screen.fill((255, 255, 255))
    x = datetime.datetime.now()
    min_hand = pygame.transform.rotate(min_hand_or, -48 - x.minute * 6)
    sec_hand = pygame.transform.rotate(sec_hand_or,  60 -x.second * 6)

    screen.blit(mclock , mclock.get_rect(center = screen.get_rect().center))
    screen.blit(min_hand, min_hand.get_rect(center = screen.get_rect().center))
    screen.blit(sec_hand, sec_hand.get_rect(center = screen.get_rect().center))
        
    pygame.display.flip()

    clock.tick(60)