import time

#definimos el decorador
def time_counter(func):
    def wrap(*args,**kwargs):
        start = time.time()
        #llamamos a la función a envolver
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrap

@time_counter
def countdown(n):
    while n > 0:
        n -= 1

countdown(5)
countdown(1000) 