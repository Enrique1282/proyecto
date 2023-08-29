texto ="gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
texto_final= ""

renglones = texto.split("&")
for contador, renglon in enumerate(renglones):
  renglon = renglon[0].upper() + renglon[1:]

  if contador == 0:
    renglon += "..."
  else:
    renglon = "─ " + renglon + "."

#SIN JOIN
#texto_final += renglon + "."

# CON JOIN
  renglones[contador] = renglon

texto_final = "\n".join(renglones)
print(texto_final)