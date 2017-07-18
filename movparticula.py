#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
import numpy as np
import math

#definindo a classe
class Particula:
#inicialização
	def __init__(self, massa, x, vx):
		self.m= massa
		self.x= x
		self.r= np.sqrt(self.x**2 + R**2)
		self.v= vx
#aceleração
	def a(self, pos):
		return -(G*M/ np.sqrt((self.x**2 + R**2)**3))*pos
#movimentação
	def move(self):
		at= self.a(self.x)
		self.x= self.x + self.v*dt + 0.5*at*dt**2
		self.v= self.v + at*dt
#declaração das variáveis
G= 6.67*10**-11
M= 7.65*10**11
m= 8.68*10**3
R= 1
dt= 0.001
#objeto
p= Particula(m, 1, 0)

#pygame
pygame.init()
screen= pygame.display.set_mode((650,450)) #tamanho da imagem
myfont= pygame.font.Font(None,60) #fonte, tamanho

galaxy = pygame.image.load("galaxy.jpg").convert() # carregar imagem
planet = pygame.image.load("particula.png").convert_alpha()
planet = pygame.transform.scale(planet,(40,29))  #mudar escala da imagem
pygame.display.set_caption("Movimento da partícula")

while True: #roda enquanto não clicar em "quit"
	for event in pygame.event.get():
		if event.type in (QUIT,KEYDOWN):
			sys.exit()
	
	screen.blit(galaxy, (0,0)) #plotar "galaxy" na coordenada 0,0
	p.move() 
	screen.blit(planet, (320, p.x*(450-29)/2 + (450-29)/2)) #plotar "planet" na coordenada
	pygame.display.update() #atualizar display
