#Faça um programa em Python que abra e reproduza o áuio de um arquivo mp3

import pygame
pygame.init()
pygame.mixer.music.load('exercicio21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

import playsound
playsound.playsound('exercicio21.wav')




