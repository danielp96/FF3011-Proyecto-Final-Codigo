#segunda prueba de graficación
#método github

#Gráfica del problema de Laplace de cilíndricas

#importamos los módulos necesarios 
#Se necesita tener instalado:
##Matplotlib
##Numpy
##Scipy
#para poder ejecutar el código

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#Creamos los ejes en 3d
fig = plt.figure("Potencial_Cilíndricas")
ax = plt.axes(projection='3d')

#Creamos la función que vamos a graficar

R = 1 #radio del cilindro de 1 unidad en m
E_0 = 3 #Valor del campo eléctrio en V/m

r = np.linspace(1, 100, 10)
phi = np.linspace(0, 2*np.pi, 40)
r, phi = np.meshgrid(r, phi) #hacemos una malla con las dos variables

Y = r*np.sin(phi)
X = r*np.cos(phi)

#Armamos la función de potencial V(r, phi) en V
V = -E_0*(r - (R**2)/(r))*np.cos(phi)


#Graficamos la función
ax.plot_surface(r, phi, V, rstride = 1, cstride = 1, cmap = 'winter', edgecolor = 'none')

#Añadimos detalles adicionales estéticos
ax.set_xlabel(r'$r$')
ax.set_ylabel(r'$\phi$')
ax.set_zlabel(r'$V(r,\phi)$')
ax.set_title("Potencial afuera del cilindro")

#Mostramos la gráfica
plt.show()
