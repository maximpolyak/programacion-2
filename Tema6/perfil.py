from memory_profiler import profile

@profile
def asignar_memoria():
    #asignar memoria a una lista con un rango amplio de números
    memo_a = [i for i in range(10000)]
    #asignar memoria a una lista con un rango amplio cuadrados de números
    memo_b = [i**2 for i in range(10000)]
    #asignar memoria a una lista con un rango amplio cubos de números
    memo_c = [i**3 for i in range(10000)]
    #asignar memoria a una lista con un rango amplio cuadrados de números
    memo_d = [(i**2)**2 for i in range(10000)]

    return memo_a, memo_b, memo_c, memo_d

if __name__ == "__main__":
    asignar_memoria()