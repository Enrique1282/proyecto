# def saludo(persona,city):
#     print(f"hola! {persona}, bienvenido a {city}")

# nombre="Juan Perez"
# ciudad="Santa Fe"

# saludo(nombre,city)


# n1 = float(input("ingrese un numero: "))
# n2 = float(input("ingrese un numero: "))

# def es_multiplo():
#     if n1 % n2 == 0.0 or n2 % n1 == 0.0:
#         print( "si son multiplos")
#     else:
#         print("no es multiplo")
# es_multiplo()


#Escribir una función que reciba una muestra de números en una lista y devuelva su media.

# n = [2, 8, 10, 20, 46, 100]
# def media():
#     print(f"La media es, {x}")
#     return media
# x = sum(n) / 6
# media()



# Recibirá un año por parámetro
# Imprimirá “El año año es bisiesto” si el año es bisiesto
# Imprimirá “El año año no es bisiesto” si el año no es bisiesto
# Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

age = int(input("ingrese un ano: "))

def es_bisiesto():
    if age % 4 == 0:
        if age % 100 == 0:
            if age % 400 ==0:
                return True
                   
            else:
                return False
        else:
            return True
    else:
        return False
        
resultado = es_bisiesto()
print(resultado)
