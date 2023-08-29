punto = {"x": 45, "y": 100}
print(punto)
print(punto["x"])
print(punto["y"])


punto["z"] = 74
print(punto)


usuarios = [
    {"id": 1, "nombre": "chanchito"},
    {"id": 2, "nombre": "feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])