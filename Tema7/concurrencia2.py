import time
import threading

class Cafetera(threading.Thread):

    def __init__(self, nombre):
        self.nombre = nombre
        threading.Thread.__init__(self)

    def run(self):
        bloqueo.acquire()
        print(f"Preparando cafe para {self.nombre}.")
        time.sleep(1)
        print(f"{self.nombre} puedes recoger tu cafe.")
        bloqueo.release()


clientes = ["Pepe", "Maria", "Luis", "Jorge", "Sara", "Alba", "Javier"]

bloqueo = threading.Lock()

for cliente in clientes:
    Cafetera(nombre=cliente).start()
    print(f"Hilos activos: {threading.active_count()}")