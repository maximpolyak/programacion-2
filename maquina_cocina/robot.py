import recetas from recetas;
import programas from programas;

class RobotCocina:

    programas = []
    recetas = []

    def __init__(self):
        self.encendido = False
        self.programas = [
            batir = Programa("batir", "Mezcla y airea los ingredientes." ),
            bañar = Programa("bañar", "Cubre los alimentos con salsa."),
            calentar = Programa("calentar","Sube la temperatura de la preparación."),
            freir = Programa("freir","Cocina los alimentos sumergidos en aire caliente."),
            amasar = Programa("amasar","Mezcla y trabaja la masa hasta conseguir la textura deseada.")

        ]
        self.recetas = [
            
        ]
    



    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("El robot de cocina se ha encendido.")
        else:
            print("El robot ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("El robot de cocina se ha apagado.")
        else:
            print("El robot ya está apagado.")

    def estado(self):
        return "Encendido" if self.encendido else "Apagado"
    
    def avisos(self, mensaje):
        print(mensaje)

