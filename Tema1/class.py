import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.perimetro = 2 * math.pi * radio
        self.area = math.pi * radio ** 2

    def obtener_perimetro(self):
        return self.perimetro
    
    def obtener_area(self):
        return self.area
    
print("Hola Mundo")
radioCirculo = float(input("Introduce el radio del circulo:"))
circulo1 = Circulo(radioCirculo)
print(f"El perimetro del circulo es: {circulo1.obtener_perimetro()}")
print(f"El area del circulo es: {circulo1.obtener_area()}")
    
    