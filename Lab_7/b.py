import pygame
_songs = ['1.mp3', '2.mp3', '3.mp3']
index = 0

def play_next_song():
    global index
    index = (index + 1) % len(_songs)
    pygame.mixer.music.load(_songs[index])
    pygame.mixer.music.play()

def play_previous_song():
    global index
    index = (index - 1) % len(_songs)
    pygame.mixer.music.load(_songs[index])
    pygame.mixer.music.play()


pygame.init()
screen = pygame.display.set_mode((1200, 800))
done = False
clock = pygame.time.Clock()
pause = 0

play_next_song()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pause == 0:
                    pause = 1
                    pygame.mixer.music.pause()
                else:
                    pause = 0
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:
                play_next_song()
            if event.key == pygame.K_LEFT:
                play_previous_song()
        
    screen.fill((255, 255, 255))
    
        
    pygame.display.flip()

    clock.tick(60)