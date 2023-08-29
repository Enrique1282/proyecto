numeros = [1, 2, 3]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)

# * acumula en una lista

primero, *otros = numeros
print(primero)
print(primero, otros)

# si quiero obtener 2 numeros de la lista
numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros = numeros
print(primero, segundo, otros)


# para tomar el primer y ultimo elemento de la lista

numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, *otros, ultimo = numeros
print(primero, ultimo, otros)


# para tomar el segundo y penultimo elemento de la lista
numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, penu, ultimo = numeros
print(segundo, penu, otros)

