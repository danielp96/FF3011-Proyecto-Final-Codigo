#método github

#Gráfica del problema de Laplace de esféricas
#Problema 1
#importamos los módulos necesarios (es necesario tenerlos en el sistema)

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cte

#Creamos los ejes en 3d
fig = plt.figure("Potencial_Esfericas_afuera")
ax = plt.axes(projection='3d')

#Creamos la función que vamos a graficar

R = 10 #radio de la esfera medido en m
e_0 = cte.epsilon_0 #permitividad

r = np.linspace(0, R, 40)
phi = np.linspace(0, 2*np.pi, 40)

#Paso importante
r, phi = np.meshgrid(r, phi) #hacemos una malla con las dos variables

Y = r*np.sin(phi)
X = r*np.cos(phi)

#Armamos la función de potencial V(r, phi) en V adentro de la esfera
V = (3*r*np.cos(phi))/(10*e_0) - (6*(r**3)*(np.cos(phi))**3)/(7*e_0*R**2) + (18*(r**3)* np.cos(phi))/(35*e_0*(R**2))

#Calculamos el campo eléctrico como el gradiente del potencial
E = np.gradient(-V, axis=0)  #axis calcula el gradiente en todos los ejes (variables)

#Graficamos la función
ax.plot_surface(r, phi, E, rstride = 1, cstride = 1, cmap = 'viridis', edgecolor = 'none')

#Añadimos detalles adicionales estéticos 'esféricas'
ax.set_xlabel("r")
ax.set_ylabel(r'$\theta$')
ax.set_zlabel(r'$E(r,\theta)$')
ax.set_title("Campo eléctrico afuera de la esfera (V/m)")

#Mostramos la gráfica
plt.show()
