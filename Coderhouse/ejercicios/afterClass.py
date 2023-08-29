# Ejercicios after

def convertidor(*args):
  if len(args) == 1:
    milimetros = args[0]
    # metro = int(milimetros / 1000)
    metro = milimetros // 1000
    centimetro = (milimetros % 1000) // 10
    milimetro = milimetros % 10
    return metro, centimetro, milimetro

  elif len(args) == 3:
    metros, centimetros, milimetros = args
    metro_milim= metros * 1000
    cent_milim= centimetros * 100
    return metro_milim + cent_milim + milimetros

  else:
    print("valores incorrectos")

print(convertidor(10513))
print(convertidor(10, 51, 3))
# 10 mt - 51 cm - 3 mm
