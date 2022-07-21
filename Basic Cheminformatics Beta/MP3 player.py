import pygame
from pygame import mixer

pygame.init()
mixer.init()
screen = pygame.display.set_mode((600, 400))
mixer.music.load("filename.mp3")
mixer.music.play()

print("Press 'p' to pause 'r' to resume")
print("Press 'q' to quit")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer.music.pause()
            if event.key == pygame.K_r:
                mixer.music.unpause()
            if event.key == pygame.K_q:
                running = False
quit()