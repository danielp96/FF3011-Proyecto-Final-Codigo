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

#r = np.linspace(0, R, 100)
phi = np.linspace(0, 2*np.pi, 90)
theta = np.linspace(0, np.pi, 90)

#Paso importante
theta, phi = np.meshgrid(theta, phi) #hacemos una malla con las dos variables

#Coordenadas cartesianas (graficamos una esfera de base)

Y = R*np.sin(theta)* np.cos(phi)
X = R*np.sin(theta)* np.sin(phi)
Z = R*np.cos(theta)


#Graficamos la esfera base
ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1 , color = 'black', alpha = 0.3, shade = 0)



#graficamos la densidad por medio de puntos sobre la esfera
sigma = (-3/2)*np.cos(3*theta)

densidad = ax.scatter(X, Y, Z, s = 3, c = sigma)

#Añadimos detalles adicionales estéticos 'esféricas'
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Densidad superficial de la esfera (C/m^2)")

#barra de color de la densidad superficial
import matplotlib as mpl
fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom = 0.4)

cmap = mpl.cm.viridis
norm = mpl.colors.Normalize(vmin= -3/2, vmax = 3/2)

fig.colorbar( densidad,
             cax=ax, orientation='horizontal', label='Densidad superficial de carga (C/m^2)')




#Mostramos la gráfica
plt.show()
