import time

class Receta:
    def __init__(self, nombre, ingredientes, pasos, zona, tiempo_preparacion=30):
        self.nombre = nombre
        self.tiempo_preparacion = tiempo_preparacion
        self.ingredientes = ingredientes
        self.pasos = pasos
        self.zona = zona

    def mostrar_receta(self):
        print(f"\nReceta: {self.nombre}")
        print(f"Tiempo de preparación: {self.tiempo_preparacion} minutos")
        print("Ingredientes:")
        for nombre, cantidad in self.ingredientes.items():
            print(f"- {nombre}: {cantidad} g")
        print("\nPasos:")
        for i, (paso, _) in enumerate(self.pasos, 1):
            print(f"{i}. {paso}")

    def cocinar(self, robot):
        if not robot.encendido:
            robot.encender()

        print(f"\n🧑‍🍳 ¡Comenzamos a preparar '{self.nombre}'!")

        print("\n📌 Estos son los ingredientes necesarios:")
        for ingrediente, cantidad in self.ingredientes.items():
            print(f"- {ingrediente}: {cantidad} g")

        input("\n👉 Pulsa Enter cuando hayas reunido todos los ingredientes.")

        for i, (paso, programa) in enumerate(self.pasos, 1):
            print(f"\n✅ Paso {i}: {paso}")
            input("Presiona Enter para iniciar este paso.")
            programa.iniciar_programa()
            print("⏳ Ejecutando...")
            time.sleep(2)  # Simula la duración del programa
            print("✓ ¡Paso completado!")

        robot.apagar()

        print(f"\n🎉 ¡Listo! La receta '{self.nombre}' está terminada. ¡Buen provecho!\n")
