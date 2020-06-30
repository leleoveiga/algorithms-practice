while True:
  try:
    tempo = input()

    hora = int(tempo[0]) * 60
    minutos = int(tempo[2:4])
    total = hora + minutos
    atraso = max((total+60) - 480, 0)

    print("Atraso maximo: %d" % atraso)
  except EOFError:
    break
