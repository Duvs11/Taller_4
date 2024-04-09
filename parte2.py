import numpy as np

# Crear arreglos de dos dimensiones a partir de listas

miListaN=[[1,3,5,7],[3,8,2,4]]

miArregloN=np.array(miListaN)

print(miArregloN)
print(miListaN)

# Crear un arreglo con funciones de relleno

a=np.zeros((2,2,2))

print(a)

b=np.zeros((5,4))

print(b)

c=np.ones((5,4))

print(c)

d=np.empty((5,4))

print(d)

# Retorna valores hasta el valor especificado secuencial 
# En (-10,10,0.4) retorna los números de -10 a 10 sumando 0.4 a cada uno

e=np.arange(-10,10)

print(e)

# Función reshape, cambia la forma de un arreglo

e=e.reshape((2,10))

print(e.ndim)

