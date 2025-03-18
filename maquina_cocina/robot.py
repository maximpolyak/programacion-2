from dispositivo import DispositivoCocina
from programa import Programa
from receta import Receta

class RobotCocina(DispositivoCocina):
    def __init__(self):
        self.encendido = False
        self.programas = {
            "batir": Programa("batir", "Mezcla y airea ingredientes."),
            "bañar": Programa("bañar", "Cubre alimentos con salsa."),
            "calentar": Programa("calentar", "Aumenta la temperatura."),
            "freir": Programa("freir", "Fríe alimentos con aceite."),
            "amasar": Programa("amasar", "Trabaja masas para pan o pasteles.")
        }

        self.recetas = [
            Receta(
                "Pechuga en Salsa",
                {"Pechuga pollo": 200, "Champiñones": 150, "Nata": 200, "Cebolla": 100, "Ajo": 10},
                [("Freír la pechuga hasta dorarla", self.programas["freir"]),
                 ("Calentar cebolla, ajo y champiñones", self.programas["calentar"]),
                 ("Bañar con salsa de champiñones", self.programas["bañar"])],
                "Zona Salado", tiempo_preparacion=25
            ),
            Receta(
                "Sopa de Verduras",
                {"Zanahoria": 100, "Patatas": 150, "Caldo pollo": 500, "Cebolla": 50},
                [("Calentar el caldo con verduras", self.programas["calentar"])],
                "Zona Caliente", tiempo_preparacion=15
            ),
            Receta(
                "Bizcocho",
                {"Harina": 200, "Azúcar": 150, "Huevos": 3, "Leche": 100, "Mantequilla": 80, "Levadura": 10},
                [("Batir huevos con azúcar", self.programas["batir"]),
                 ("Amasar harina con levadura", self.programas["amasar"]),
                 ("Hornear mezcla", self.programas["calentar"])],
                "Zona Postres", tiempo_preparacion=40
            )
        ]

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("Robot encendido.")
        else:
            print("El robot ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("Robot apagado.")
        else:
            print("El robot ya estaba apagado.")

    def programar(self, programa, ingredientes):
        if not self.encendido:
            print("Error: el robot está apagado. Debes encenderlo antes de ejecutar un programa.")
            return

        if programa in self.programas:
            print(f"Programando '{programa}' con ingredientes: {ingredientes}")
            self.programas[programa].iniciar_programa()
        else:
            print(f"Programa '{programa}' no disponible.")

    def mostrar_recetas(self):
        for receta in self.recetas:
            receta.mostrar_receta()

    def cocinar_receta(self, nombre_receta):
        if not self.encendido:
            print("Error: el robot está apagado. Debes encenderlo primero para cocinar.")
            return

        receta_encontrada = next((r for r in self.recetas if r.nombre.lower() == nombre_receta.lower()), None)
        if receta_encontrada:
            receta_encontrada.cocinar(self)
        else:
            print(f"No existe la receta '{nombre_receta}'.")

