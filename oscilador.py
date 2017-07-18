#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation as animation
import math

#definindo a classe
class Oscilador:
#inicialização
	def __init__(self, lado, x, v):
		self.m= rob*(lado**3)
		self.l= lado
		self.x= x
		self.v= v
#aceleração
	def a(self, x, v):
		return (rob-rof)*g*(self.l**3)/self.m - (k/self.m)*(x-x0) - ro*v/self.m
#movimentação
	def move(self, t):
		at= self.a(self.x, self.v)
		self.x= self.x + self.v*dt + 0.5*at*(dt**2)
		atem= self.a(self.x, self.v)
		vtem= self.v + 0.5*(at+atem)*dt
		atem= self.a(self.x, vtem)
		self.v= self.v + 0.5*(at+atem)*dt
		self.at= self.a(self.x, self.v)
#declaração das variáveis
g= 9.8
lado= 0.1
rob= 8000	#densidade do bloco
rof= 1250	#densidade do fluido
ro= 2		#coeficiente de proporcionalidade
k= 40		#constante elástica
x0= 0.5
dt= 0.1
t= 0
#objeto
o1= Oscilador(lado, 0.51, 0)
#arrays
tmax= 60
t= np.arange(0, tmax, dt)
x= np.zeros(t.size)
v= np.zeros(t.size)
x[0]= o1.x
v[0]= o1.v

for i in range(t.size):
	o1.move(t[i])
	x[i]= o1.x
	v[i]= o1.v
	
#masterização dos gráficos
fig = plt.figure()
plt.title('Oscilador', fontsize=12)
#gráfico 1
XT=fig.add_subplot(331, xlim=(0, tmax), ylim=(min(x)*1.05, max(x)*1.05))
XT.xaxis.grid(True)
XT.yaxis.grid(True)
plt.setp(XT.get_xticklabels(), visible=False)
plt.xlabel('Tempo (s)')
plt.ylabel('Posicao (m)')
line1, = XT.plot([], [], 'g-', lw=1)
plt.legend(loc='upper right')
#gráfico 2
VT=fig.add_subplot(334, xlim=(0, tmax), ylim=(min(v)*1.05, max(v)*1.05))
VT.xaxis.grid(True)
VT.yaxis.grid(True)
plt.setp(VT.get_xticklabels(), visible=False)
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade(m/s)')
line2, = VT.plot([], [], 'r-', lw=1)
plt.legend(loc='upper right')
#gráfico 3
VX=fig.add_subplot(122, xlim=(min(x)*1.05, max(x)*1.05), ylim=(min(v)*1.05, max(v)*1.05))
VX.xaxis.grid(True)
VX.yaxis.grid(True)
plt.setp(VX.get_xticklabels(), visible=False)
plt.xlabel('Posicao (m)')
plt.ylabel('Velocidade (m/s)')
line3, = VX.plot([], [], 'b.', lw=0.5)
plt.legend(loc='upper right')

#animação
def init():
	line1.set_data([],[])
	line2.set_data([],[])
	line3.set_data([],[])
	return line1, line2, line3,
def animate(i):
	tt= t[:i]
	xx= x[:i]
	vv= v[:i]
	line1.set_data(tt, xx)
	line2.set_data(tt, vv)
	line3.set_data(xx, vv)
	return line1, line2, line3,
#execução da animação
anim= animation.FuncAnimation(fig, animate, init_func= init, frames= t.size,
interval= 20, blit= True, repeat= False)
#salvar animação
anim.save('oscilador.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#mostrar animação
plt.show()
