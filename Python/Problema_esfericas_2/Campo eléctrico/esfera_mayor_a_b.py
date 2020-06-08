#Gráfica del problema de Laplace de esféricas
#Problema 2
#importamos los módulos necesarios (es necesario tenerlos en el sistema)
#Código por Juan Pablo Valenzuela


#ESTE ES EL ARCHIVO PARA GRAFICAR DE r > b
#Campo eléctrico

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cte

#Creamos los ejes en 3d
fig = plt.figure("Potencial_Esfericas_adentro")
ax = plt.axes(projection='3d')

#Creamos la función que vamos a graficar
a = 5 #radio esfera pequeña
V_0 = 20 #potencial esfera pequeña
b = 15  #radio esfera grande
k = 3  #constante
e_0 = cte.epsilon_0  #permitividad

r = np.linspace(b, 60, 40) #va desde cero hasta a
phi = np.linspace(0, 2*np.pi, 40)

#Paso importante
r, phi = np.meshgrid(r, phi) #hacemos una malla con las dos variables



#Armamos la función de potencial V(r, phi) en V adentro de la esfera
V = (a*V_0)/r - (k*(b**2))/(3*e_0*r) + (4*k*(b**4)*(3*(np.cos(phi)**2)-1))/(15*e_0*(r**3)*2)

#Calculamos el campo eléctrico como el gradiente del potencial
E = np.gradient(-V, axis= 0)

#Graficamos la función
ax.plot_surface(r, phi, E, rstride = 1, cstride = 1, cmap = 'viridis', edgecolor = 'none')

#Añadimos detalles adicionales estéticos 'esféricas'
ax.set_xlabel(r'$r$')
ax.set_ylabel(r'$\theta$')
ax.set_zlabel(r'$E(r,\theta)$')
ax.set_title("Campo en r > b (V/m)")

#Mostramos la gráfica
plt.show()
