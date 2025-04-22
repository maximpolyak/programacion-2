'''Vamos a hacer procesos para retirar y depositar fondos. Cada uno de los procesos realiza mil operaciones con valor 1€ sobre un depósito inicial de 100€.
'''

import multiprocessing

def sacar_fondos(saldo):
    for _ in range(1000):
        saldo.value -= 1

def depositar_fondos(saldo):
    for _ in range(1000):
        saldo.value += 1

def hacer_transacciones():
    #saldo inicial -> almacenar en la memoria compartida para que sea accesible para los distintos procesos
    saldo = multiprocessing.Value("i", 100)

    #creamos dos procesos, para sacar y depositar
    proceso1 = multiprocessing.Process(target=sacar_fondos, args=(saldo,))
    proceso2 = multiprocessing.Process(target=depositar_fondos, args=(saldo,))

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

    print(f"Saldo final tras transacciones: {saldo.value}")

if __name__ == "__main__":
    #vamos a ejecutar 5 veces el proceso de hacer transacciones
    for _ in range(10):
        hacer_transacciones()
