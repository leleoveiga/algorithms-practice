x = int(input())

horas = int(x/3600)
x -= horas*3600
minutos = int(x/60)
x -= minutos*60
segundos = int(x)

print(str(horas) + ":" + str(minutos) + ":" + str(segundos))
