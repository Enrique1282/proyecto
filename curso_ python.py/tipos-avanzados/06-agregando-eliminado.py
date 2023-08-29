# Agregar elementos

mascotas = ["bono", "azi", "uma", "sandi", "lali"] 
mascotas.insert(1, "melvin")
mascotas.append("laligera")
print(mascotas)


# Eliminar elementos
mascotas.remove("laligera")
mascotas.pop(1)
del mascotas[0]
mascotas.clear()
print(mascotas)