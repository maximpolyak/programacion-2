'''Dada una lista de números, devolver la lista con los elementos incrementados en 1. Para ello, tenemos una función incrementar, que además nos informa del id del proceso que realiza el cálculo.
'''

import multiprocessing
import os

def incremento(num):
    print(f"Proceso de trabajo para {num}: {os.getpid()}")
    return (num + 1)

if __name__ == "__main__":
    lista_num = [n for n in range(10)]

    result = []
    for n in lista_num:
        result.append(incremento(n))
    print(result)
    