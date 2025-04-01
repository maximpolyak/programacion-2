#Tenemos 11 entradas disponibles para el teatro, y sólo se pueden comprar de 2 en 2. Hay seis personas esperando para comprar entradas a la vez.
#- Crear una clase VenderEntrada que recibirá como argumento el número de entradas disponibles.
#- Al crear los hilos pasaremos el número de entradas a comprar como argumento
import threading

class VenderEntrada:
    def __init__(self, entradas_disponibles):
        self.entradas = entradas_disponibles
        self.lock = threading.Lock()

    def vender(self, cliente, cantidad):
        with self.lock:
            if self.entradas >= cantidad:
                self.entradas -= cantidad
                print(f"{cliente} compró {cantidad} entrada(s). Quedan {self.entradas}.")
            elif self.entradas > 0:
                print(f"{cliente} quiso comprar {cantidad}, pero solo quedaban {self.entradas}. No se realizó la compra.")
            else:
                print(f"{cliente} quiso comprar {cantidad}, pero no quedan entradas.")

class VentaEntradas(threading.Thread):
    def __init__(self, sistema_venta, cliente, cantidad):
        threading.Thread.__init__(self)
        self.sistema_venta = sistema_venta
        self.cliente = cliente
        self.cantidad = cantidad

    def run(self):
        self.sistema_venta.vender(self.cliente, self.cantidad)

# --- Código principal ---

clientes = [
    {"nombre": "Pepe", "entradas": 1},
    {"nombre": "Maria", "entradas": 3},
    {"nombre": "Luis", "entradas": 2},
    {"nombre": "Jorge", "entradas": 1},
    {"nombre": "Sara", "entradas": 2},
    {"nombre": "Alba", "entradas": 3}
]

sistema = VenderEntrada(entradas_disponibles=11)

hilos = []

for cliente in clientes:
    hilo = VentaEntradas(sistema, cliente["nombre"], cliente["entradas"])
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()
