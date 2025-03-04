import math

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        """Simplifica la fracción usando el máximo común divisor"""
        gcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= gcd
        self.denominador //= gcd

    def __add__(self, other):
        """Sobrecarga del operador + para sumar fracciones"""
        nuevo_num = self.numerador * other.denominador + other.numerador * self.denominador
        nuevo_den = self.denominador * other.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __sub__(self, other):
        """Sobrecarga del operador - para restar fracciones"""
        nuevo_num = self.numerador * other.denominador - other.numerador * self.denominador
        nuevo_den = self.denominador * other.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __str__(self):
        """Representación en forma de cadena"""
        return f"{self.numerador} / {self.denominador}"

# Ejemplo de uso
f1 = Fraccion(1, 2)
f2 = Fraccion(3, 4)

print(f"{f1} + {f2} = {f1 + f2}")
print(f"{f1} - {f2} = {f1 - f2}")
