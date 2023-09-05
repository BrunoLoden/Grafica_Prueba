# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 07:24:22 2023

@author: ep_blizarme
"""

import matplotlib.pyplot as plt
import numpy as np



#%%
#Dominio de y
#Demanda 1
# q1 = lambda p1 :(6-p1)/2
qg1 = lambda pg1: 48-8*pg1
# Demanda 2 
# q2 = lambda p2 : 2-p2
qg2 = lambda pg2: 28-14*pg2

#%%
#Ploteo
# Valores del eje X que toma el gráfico.
yi,ys1,ys2 = 0,10,2
pts = 50
# Establecer el color de los ejes.
plt.axhline(6, color="y",linestyle="--",linewidth=1.5)
plt.axhline(2, color="y",linestyle="--",linewidth=1.5)
#Demandas
# plt.title("Demanda 1")
plt.plot(qg1(np.linspace(yi, ys1, pts)),np.linspace(yi, ys1, pts),label="Qg1 = 48-8*Pg1",color="cornflowerblue")
# plt.title("Demanda 2")
plt.plot(qg2(np.linspace(yi, ys2, pts)),np.linspace(yi, ys2, pts),label="Qg2 = 28-14*Pg2",color="lightcoral")
plt.title("Demanda 1 y 2")
plt.legend()
plt.xlabel("Demanda (Q)")
plt.ylabel("Precio (P)")
# Limitar los valores de los ejes.
plt.xlim(0, 80)
plt.ylim(0, 7)
#Grid
plt.grid(True,color='gray', linestyle='--', linewidth=0.5)
# Guardar gráfico como imágen PNG.
# plt.savefig("Grafica1y2.png")
# Mostrarlo.
plt.show()

#---------------------------------------------------------------
print("Se agregara una extos extra")
#---------------------------------------------------------------
    

#%%

# def graf_dem(lsx,lsy,pts):
    

#%%
p1,p2,p3 = 6,2,0
ax3 = plt.subplot()

ax3.plot((qg1(np.linspace(p2, p1, pts))),
         np.linspace(p2, p1, pts),
         label="Qtotal=Qg1",
         color="cornflowerblue")
ax3.plot((qg1(np.linspace(p3, p2, pts))+qg2(np.linspace(p3, p2, pts))),
         np.linspace(p3, p2, pts),
         label="Qtotal=Qg1+Qg2",
         color="mediumpurple")
ax3.legend()
# ax3.hlines(1)
ax3.axhline(6, color="y",linestyle="--")
ax3.axhline(2, color="y",linestyle="--")
ax3.set_xlabel("Demanda (Q)")
ax3.set_ylabel("Precio (P)")
ax3.set_title("Demanda total")
ax3.set_xlim(0, 80)
ax3.set_ylim(0,7)
ax3.grid(True,color='gray', linestyle='--', linewidth=0.5)
#%%
#Calculo de Area

#Demanda 1
qg1 = lambda pg1: 48-8*pg1
# Demanda 2 
qg2 = lambda pg2: 28-14*pg2

q_interseccion = qg1
#%%
# # Generamos los datos para las gráficas
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# # Creamos una figura con dos subparcelas
# plt.subplot(2, 1, 1)
# plt.plot(x, y1)
# plt.title('Gráfica 1')
# plt.xlabel('x')
# plt.ylabel('y1')

# #%%
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
# temperaturas = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
# ax.plot(dias, temperaturas['Madrid'], label = 'Madrid')
# ax.plot(dias, temperaturas['Barcelona'], label = 'Barcelona')
# ax.legend(loc = 'upper right')
# plt.show()

## %%
# xpts = np.linspace(0, 100, 1000)
# test = lambda x: ((x) <= 66)*.5 + .5
# print(type(np.array(10,)))
# plt.plot(xpts, test(xpts))
# plt.show()

#%%

# #Yo no acepto citas
# while calidad_cita == "Buena":
#     aceptar_cita()

# #Yo las elijo
# while True:
#     aceptar_cita()
    
    
# #Yo no acepto citas
# if calidad_cita == "Buena":
#     aceptar_cita()
# else:
#     rechazar_cita()
    
    
# #Yo las elijo
# while True:
#     aceptar_cita()
# else:
#     rechazar_cita()
