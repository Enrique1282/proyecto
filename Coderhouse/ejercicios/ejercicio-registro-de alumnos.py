student = {}
registro_alumnos = input("¿Desea registrar un alumno nuevo? (SI/NO): ").upper()

contador = 0

while registro_alumnos == "SI":
    contador += 1
    alumno = {
        "nombre": input("ingrese su nombre: "),
        "apellido": input("ingrese su apellido: "),
        "carrera": input("ingrese la carrera a registrar: ")
    }
    valor = f"alumno_{contador}"
    student[valor] = alumno

    registro_alumnos = input("¿Desea seguir registrnado alumnos? (SI/NO): ").upper()
else:
    print("fin registro")


print(student)
