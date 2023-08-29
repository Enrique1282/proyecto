lista1 = [1,2,3,4,5]
lista2 = [6,7,8]

combinada = [*lista1, *lista2]
print(combinada)

combinada = ["hola", *lista1, "mundo", *lista2, "chanchito"]
print(combinada)


punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "hola mundo", **punto2, "z": 50} 
print(nuevoPunto)