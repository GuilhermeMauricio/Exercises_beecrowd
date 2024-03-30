n = int(input())
horas = n//3600
n %= 3600
minutos = n //60
n %= 60

print(f"{horas}:{minutos}:{n}")