# Importar la biblioteca
import numpy as np

# Una forma de crear arreglos (ndarray), es usando una lsita

miLista=[3,5,7,9]

# Drea un arreglo unidimensional a partir de una lista básica de python

miArreglo=np.array(miLista)

print(miArreglo.ndim)

# Dimensiones

print(miArreglo.shape)

# Número de elementos en el arreglo

print(miArreglo.size)

# Tipo de datos en el arreglo

print(miArreglo.dtype)

# Colocar siempre [] para crear un arreglo a partir de una lista

miArreglo2=np.array([3,6,7,90])