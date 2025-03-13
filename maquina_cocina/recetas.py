
import time
class Receta:
    def __init__(self, nombre, tiempo_preparacion):
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


    def cocinar(self):
        print(f"\n¡Comenzaremos la receta {self.nombre}!")
        self.robot.encender()  # Mirar el nombre del método
        print("Estos son los ingredientes que necesitaremos:")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente}") # pedir la lista de ingredientes 
        print("\n¡Siguiente paso!:")
        for i, (paso, accion) in enumerate(self.pasos, 1):
            print(f"\nPaso {i}: {paso}")
        if accion:
            accion()
        time.sleep(2)
        print("✓ ¡Paso completado!")
        self.robot.apagar()
        print(f"\n¡Listo! Hemos terminado la receta: {self.nombre}. ¡Que aproveche!")


class Ingrediente(Receta):
    def __init__(self, nombre, cantidad, unidad):
        self. nombre = nombre 
        self.cantidad = cantidad 
        self.unidad = unidad 

    def __str__(self):
        return f"{self.nombre} ({self.cantidad} {self.unidad})"
    
    
