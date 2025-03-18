class Programa:
    def __init__(self, nombre, descripcion, tiempo_operacion=60):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tiempo_operacion = tiempo_operacion

    def iniciar_programa(self):
        print(f"Iniciando programa: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Duración: {self.tiempo_operacion} segundos")
