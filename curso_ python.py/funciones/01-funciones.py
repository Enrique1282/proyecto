# def hola():
#     print("hola mundo")
#     print("ultimate python")
# hola()


def hola(nombre, apellido):
    print("hola mundo")
    print(f"Bienvenido {nombre} {apellido}")

hola("Nicolas", "Perez")
hola("chanchito", "feliz")


# parametros opcionales

def hola(nombre, apellido="feliz"):
    print("hola mundo")
    print(f"Bienvenido {nombre} {apellido}")

hola("Nicolas", "Perez")
hola("chanchito")
