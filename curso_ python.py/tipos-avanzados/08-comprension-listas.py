usuarios = [["rober", 1], ["carlos", 5], ["lula", 3], ["felipe", 8]]

nombres =[]
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)


# map
nombres =[usuario[0] for usuario in usuarios]
print(nombres)


# filtrar - filter
nombres =[usuario for usuario in usuarios if usuario[1]>2]
nombres =[usuario[0] for usuario in usuarios if usuario[1]>2]
print(nombres)