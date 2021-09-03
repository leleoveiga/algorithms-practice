n = int(input())

for i in range(1,3):
  print(i)

for i in range(n):
  data1, data2 = input().split()

  ano1 = int(data1[0:4])
  mes1 = int(data1[5:7])
  dia1 = int(data1[8:10])

  ano2 = int(data2[0:4])
  mes2 = int(data2[5:7])
  dia2 = int(data2[8:10])

  dias = 0

  for i in range(ano1, ano2+1):
    if (i%400 == 0) or (i%4 == 0 and i%100 != 0):
      dias += 366
    else:
      dias += 365

  meses = [31, 28, ]
  
  dias += abs(mes1-mes2) * 30



  print(ano2,mes2,dia2)