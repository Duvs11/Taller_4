import numpy as np

a=np.array([5,10,15,20,25])
print(a)

b=np.array([3,4,5,7,9])
print(b)

c=a-b
print(c)

# c=a/b
# c=b**2 (potencia 2)
# c=np.sin(b) (en NumPy están definidas las funciones trigonométricas)
# toma los argumentos de las funciones trigonométricas en radianes
# c=(b>6)
# print(c)
# devuelve true ó false
# c=a@b (producto punto de las matrices)
# b+=1 es igual que escribir b=b+1
# al operar arreglos puede cambiar el tipo de datos en ellos
# c=a.sum(), suma los elementos del arreglo
# c=a.min(), toma el menor elemento del arreglo
# c=a.sort(), organiza el arreglo
# c=a.mean(), saca la media del arreglo

d=np.array([[5,10,-1,20,25],[3,6,4,8,12]])
print(d)
print(d.sum())
# print(d.sum(axis=1))
# print(d.sum(axis=0))

print(np.sqrt(d))
# nan=NotasNumber, puede dar cuando toma una raíz negativa

e=np.array([[5,-10,-1,20,28],[3,6,4,8,12]])
f=np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(e)
print(f)
print(np.add(e,f))
# add suma elementos de dos arreglos
# np.round(), redondea los elementos a su entero más cercano
# se puede determinar la cantidad de décimales a las que redondea
# print(e.round(decimals=2)), redondea a 2 décimales
# print(np.ceil(e)), redondea al entero superior
# print(np.foor(e)), redondea al entero inferior
# print(e.max())
# print(np.gradient(a))
