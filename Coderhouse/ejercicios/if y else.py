nombre= input("cual es su nombre: ")
nota1= float(input("ingrese su nota de matematicas: "))
nota2= float(input("ingrese su nota de fisica: "))
nota3=float(input("ingrese su nota de lengua: "))
promedio= (nota1 + nota2 + nota3) /3
if promedio >= 6:

    print('felicidades, "APROBASTE" con: ' , round(promedio,2))
print("fin")

