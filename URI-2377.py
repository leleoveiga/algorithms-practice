distancia, pedagio = list(map(int, input().split()))
custoKm, custoPadrao  = list(map(int, input().split()))
custoTotal = int(distancia/pedagio)*custoPadrao + distancia*custoKm
print(custoTotal)
