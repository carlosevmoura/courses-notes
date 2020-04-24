import pygame

pygame.init()
pygame.mixer.music.load('Exercícios/hino-flamengo.mp3')
pygame.mixer.music.play()
pygame.event.wait()