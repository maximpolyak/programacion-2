import time 
#Holaaaa
#Hi nigga 
class RobotCocina:
    def _init_(self):
        print("Robot de cocina listo para usar.")

    def batir(self):
        print("El robot está batiendo los ingredientes.")

    def bañar(self):
        print("El robot está bañando los alimentos con salsa o cobertura.")

    def calentar(self):
        print("El robot está calentando la preparación.")

    def freír(self):
        print("El robot está friendo los alimentos.")

    def amasar(self):
        print("El robot está amasando la masa.")

class Programas:
    def __init__(self):
        


# Recetas 

class Receta:
    def __init__(self, nombre, tiempo_preparacion,):
        self.nombre = nombre
        self.tiempo_preparacion = tiempo_preparacion
        self.ingredientes = []
        self.pasos = []

    def añadir_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
        print(f"Ingrediente '{ingrediente.nombre}' agregado a la receta {self.nombre}")

    def mostrar_receta(self):
        print(f"\nReceta: {self.nombre}")
        print(f"Tiempo de preparación: {self.tiempo_preparacion} minutos")
        print("Ingredientes:")
    for ingrediente in self.ingredientes:
        print(f"- {ingrediente.nombre}: {ingrediente.cantidad} {ingrediente.unidad}")
    print("\nPasos:")
    for i, (paso, _) in enumerate(self.pasos, 1):
        print(f"{i}. {paso}")

    


