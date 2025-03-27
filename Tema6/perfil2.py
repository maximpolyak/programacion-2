from memory_profiler import profile

@profile
def asignar_memoria():
    #asignar memoria …
    memo_a = [i for i in range(10000)]
    #asignar memoria …
    memo_b = [i**2 for i in range(10000)]
    #asignar memoria …
    memo_c = [i**3 for i in range(10000)]
    #asignar memoria …
    memo_d = [(i**2)**2 for i in range(100000)]
    memo_a = None
    #memo_d = None
    del memo_d
    #return memo_a, memo_b, memo_c, memo_d

if __name__ == "__main__":
    asignar_memoria()