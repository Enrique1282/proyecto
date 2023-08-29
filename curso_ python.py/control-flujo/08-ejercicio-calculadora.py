print("Bienvenido a la calculadora")
print("para salir escribe salir")
print("las operaciones son suma, resta, multi, div")

resultado = ""
while  True:
    if resultado "":
        resultado = input("ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese una operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicar":
        resultado *= n2
    elif op.lower() == "dividir":
        resultado /= n2
    else:
        print("operacion no valida")
        
    print(f"El resultado es : {resultado}")