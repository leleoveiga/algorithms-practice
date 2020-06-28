n = int(input())
ano = int(n/365)
n -= ano * 365
mes = int(n/30)
n -= mes * 30
dias = n

print("%d ano(s)" % ano)
print("%d mes(es)" % mes)
print("%d dia(s)" % dias)
