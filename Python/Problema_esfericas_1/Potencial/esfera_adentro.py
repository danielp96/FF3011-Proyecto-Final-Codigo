#método github

#Gráfica del problema de Laplace de esféricas
#Problema 1
#importamos los módulos necesarios (es necesario tenerlos en el sistema)

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cte

#Creamos los ejes en 3d
fig = plt.figure("Potencial_Esfericas_adentro")
ax = plt.axes(projection='3d')

#Creamos la función que vamos a graficar

R = 10 #radio del cilindro de 1 unidad en m
e_0 = cte.epsilon_0 #permitividad

r = np.linspace(R, 100, 40)
phi = np.linspace(0, 2*np.pi, 40)

#Paso importante
r, phi = np.meshgrid(r, phi) #hacemos una malla con las dos variables

Y = r*np.sin(phi)
X = r*np.cos(phi)

#Armamos la función de potencial V(r, phi) en V adentro de la esfera
V = (3*(R**3)*np.cos(phi))/(10*e_0*(r**2)) - (6*(R**5)*(np.cos(phi))**3)/(7*e_0*(r**4)) + (18*(R**5)* np.cos(phi))/(35*e_0*(r**4))

#Graficamos la función
ax.plot_surface(r, phi, V, rstride = 1, cstride = 1, cmap = 'viridis', edgecolor = 'none')

#Añadimos detalles adicionales estéticos 'esféricas'
ax.set_xlabel(r'$r$')
ax.set_ylabel(r'$\theta$')
ax.set_zlabel(r'$V(r,\theta)$')
ax.set_title("Potencial adentro de la esfera (V)")

#Mostramos la gráfica
plt.show()
