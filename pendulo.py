#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import animation as animation
import math

#definindo a classe
class Pendulo:
#inicialização
	def __init__(self, l, massa, x, v): #theta = x - theta ponto = v
		self.l= l
		self.m= massa
		self.x= x
		self.v= v
		self.w2= g/l
		self.e = 0.5*massa*(l*v)**2+m*g*l*(1-math.cos(x)) #energia
#aceleração
	def a(self, x, v):
		return -2*v*self.w2**(1/2) -x*self.w2
#movimentação]
	def move(self, t):
		at= self.a(self.x, self.v)
		self.x= self.x + self.v*dt + 0.5*at*(dt**2)
		atem= self.a(self.x, self.v)
		vtem= self.v + 0.5*(at+atem)*dt
		atem= self.a(self.x, vtem)
		self.v= self.v + 0.5*(at+atem)*dt
		self.at= self.a(self.x, self.v)
		self.e = 0.5*self.m*(self.l*self.v)**2 +(self.m*g*self.l*(1-math.cos(self.x)))
#declaração das variáveis
g= 9.8
l= 98		#comprimento do pêndulo
m= 10		#massa do pêndulo (valor arbitrário)
dt= 0.1
t= 0
#objeto
p = Pendulo(l, m, 10**-2, 0) #theta inicial = PI/20
#arrays
tmax= 50
t= np.arange(0, tmax, dt)
x= np.zeros(t.size)
v= np.zeros(t.size)
e= np.zeros(t.size)
x[0]= p.x
v[0]= p.v
e[0]= p.e

for i in range(t.size):
	p.move(t[i])
	x[i]= p.x
	v[i]= p.v
	e[i]= p.e
	
#masterização dos gráficos
fig = plt.figure()
plt.title('Pendulo', fontsize=12)
#gráfico 1
XT=fig.add_subplot(331, xlim=(0, tmax), ylim=(min(x)*1.05, max(x)*1.05))
XT.xaxis.grid(True)
XT.yaxis.grid(True)
plt.setp(XT.get_xticklabels(), visible=False)
#plt.xlabel('Tempo (s)')
plt.ylabel('Theta (rad)')
line1, = XT.plot([], [], 'g-', lw=0.5)
plt.legend(loc='upper right')
#gráfico 2
VT=fig.add_subplot(334, xlim=(0, tmax), ylim=(min(v)*1.05, max(v)*1.05))
VT.xaxis.grid(True)
VT.yaxis.grid(True)
plt.setp(VT.get_xticklabels(), visible=False)
#plt.xlabel('Tempo(s)')
plt.ylabel('Vel. angular(rad/s)')
line2, = VT.plot([], [], 'r-', lw=0.5)
plt.legend(loc='upper right')
#gráfico 3
ET=fig.add_subplot(337, xlim=(0, tmax), ylim=(min(e)*1.05, max(e)*1.05))
ET.xaxis.grid(True)
ET.yaxis.grid(True)
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
line3, = ET.plot([], [], 'c-', lw=0.5)
plt.legend(loc='upper right')
#gráfico 4
VX=fig.add_subplot(122, xlim=(min(x)*1.05, max(x)*1.05), ylim=(min(v)*1.05, max(v)*1.05))
VX.xaxis.grid(True)
VX.yaxis.grid(True)
plt.setp(VX.get_xticklabels(), visible=False)
plt.xlabel('Theta (rad)')
plt.ylabel('Vel. angular(rad/s)')
line4, = VX.plot([], [], 'b-', lw=0.5)
plt.legend(loc='upper right')

#animação
def init():
	line1.set_data([],[])
	line2.set_data([],[])
	line3.set_data([],[])
	line4.set_data([],[])
	return line1, line2, line3, line4,
def animate(i):
	tt= t[:i]
	xx= x[:i]
	vv= v[:i]
	ee= e[:i]
	line1.set_data(tt, xx)
	line2.set_data(tt, vv)
	line3.set_data(tt, ee)
	line4.set_data(xx, vv)
	return line1, line2, line3, line4,
#execução da animação
anim= animation.FuncAnimation(fig, animate, init_func= init, frames= t.size,
interval= 20, blit= True, repeat= False)
#salvar animação
anim.save('pendulo.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#mostrar animação
plt.show()




