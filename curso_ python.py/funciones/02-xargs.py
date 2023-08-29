def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(4, 8, 9)
suma(15, 45, 15, 32, 78)
suma(2, 5)