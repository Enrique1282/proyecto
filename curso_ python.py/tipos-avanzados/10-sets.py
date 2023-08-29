# set significa grupo o conjunto

#primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)


# transformar lista a set

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

# operador de union | (alt + 124)
print(primer | segundo)

#operador de interseccion &
print(primer & segundo)

#operador de diferencia - (menos)
print(primer - segundo)

# operador de diferencia simetrica ^ (alt + 94)
print(primer ^ segundo)


if 5 in segundo:
    print("Hola Mundo")