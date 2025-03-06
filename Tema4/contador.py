def contar_hasta(n):
    contador = 0
    while contador < n:
        contador += 1
        yield contador

for num in contar_hasta(3):
    print(num)