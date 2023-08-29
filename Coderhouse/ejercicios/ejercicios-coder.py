# resultado = ""

# num = list(range(100))
# par = num[1::2]
# impar = num[0::]

# while True:
#     if not resultado:
#         resultado = input("ingrese numero impar: ")
#         if resultado == "impar":
#            break
#         resultado = int(resultado)
            
#     if resultado == "impar":
#         resultado = par[1::2]
#         break
#     else:
#         print("operacion no valida")
    
#     print("tu num es {resultado}")


num = list(range(101))
print(num[1::2])
print(sum(num[1::2]))
