salario = float(input())

imposto1 = min(salario - 2000, 1000) * 0.08
imposto2 = min(salario - 3000, 1500) * 0.18
imposto3 = (salario - 4500) * 0.28

final = 0

if imposto1 > 0:
    final += imposto1
if imposto2 > 0:
    final += imposto2
if imposto3 > 0:
    final += imposto3

if final == 0:
    print("Isento")
else:
    print("R$ %.2f" % final)