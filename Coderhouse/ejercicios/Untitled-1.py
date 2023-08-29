nombre= input("Hola, cual es tu nombre?: ")
nota1=float(input("ingrese su primer nota: "))
nota2=float(input("ingrese su segunda nota: "))
nota3=float(input("ingrese su tercer nota: "))
nota1= nota1* 0.30
nota2= nota2* 0.5
nota3= nota3* 0.20
promedio= nota1 + nota2 + nota3
if promedio >=6:
    print("felicitaciones", nombre, "has 'Aprobado' con: ", round(promedio,2))
else:
   print("suerte en la proxima")