num = [2, 4, 12, 64, 23, 14, 74, 89]

#num.sort()
#num.sort(reverse=True)

numeros2 = sorted(num)
print(num)
print(numeros2)


################

usuarios = [[1, "rober"], [5, "carlos"], [3, "lula"], [8, "felipe"]]
usuarios.sort()
print(usuarios)


usuarios = [["rober", 1], ["carlos", 5], ["lula", 3], ["felipe", 8]]
def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)
usuarios.sort(key=ordena, reverse=True)
print(usuarios)


# Funcion lamnda

usuarios.sort(key=lambda el: el[1], reverse=True)