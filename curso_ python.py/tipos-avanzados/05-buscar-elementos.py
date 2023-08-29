mascotas = ["bono", "azi", "uma", "lali"]

print(mascotas.index("azi"))


# si no esta en la lista

mascotas = ["bono", "azi", "uma", "sandi", "lali"]

if "sandi" in mascotas:
   print(mascotas.index("sandi"))


# .count() para buscar cuantas veces esta repetido

mascotas = ["bono", "uma", "azi", "uma", "sandi", "lali", "uma", "uma"]
print(mascotas.count("uma"))

if "sandi" in mascotas:
   print(mascotas.index("sandi"))
