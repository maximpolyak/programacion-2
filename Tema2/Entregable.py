import math

class CalculoGeometrico:
    """Superclase para calcular perímetro y área de figuras geométricas."""

    def __init__(self, *args):
        """Valida que todos los valores sean números positivos."""
        self._validar_valores(*args)

    def _validar_valores(self, *valores):
        """Valida que todos los valores sean números positivos."""
        for valor in valores:
            if not isinstance(valor, (int, float)) or valor <= 0:
                raise ValueError(f"El valor '{valor}' debe ser un número positivo.")

    def calcular_perimetro(self):
        """Método que se sobrescribirá en las subclases."""
        raise NotImplementedError("Este método debe ser implementado en la subclase.")

    def calcular_area(self):
        """Método que se sobrescribirá en las subclases."""
        raise NotImplementedError("Este método debe ser implementado en la subclase.")

# ---------------------- SUBCLASES ---------------------- #

class Circulo(CalculoGeometrico):
    """Clase para calcular el perímetro y área de un círculo."""

    def __init__(self, radio):
        super().__init__(radio)
        self.__radio = radio

    @property
    def radio(self):
        return self.__radio

    def calcular_perimetro(self):
        return round(2 * math.pi * self.__radio, 2)

    def calcular_area(self):
        return round(math.pi * self.__radio ** 2, 2)


class Triangulo(CalculoGeometrico):
    """Clase para calcular el perímetro y área de un triángulo equilátero."""

    def __init__(self, lado):
        super().__init__(lado)
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

    def calcular_perimetro(self):
        return round(self.__lado * 3, 2)

    def calcular_area(self):
        return round((math.sqrt(3) / 4) * self.__lado ** 2, 2)


class Cuadrado(CalculoGeometrico):
    """Clase para calcular el perímetro y área de un cuadrado."""

    def __init__(self, lado):
        super().__init__(lado)
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

    def calcular_perimetro(self):
        return round(self.__lado * 4, 2)

    def calcular_area(self):
        return round(self.__lado ** 2, 2)


class Rectangulo(CalculoGeometrico):
    """Clase para calcular el perímetro y área de un rectángulo."""

    def __init__(self, base, altura):
        super().__init__(base, altura)
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura

    def calcular_perimetro(self):
        return round(2 * (self.__base + self.__altura), 2)

    def calcular_area(self):
        return round(self.__base * self.__altura, 2)


# ---------------------- SEGUNDA PARTE: NUEVAS FIGURAS ---------------------- #

class Rombo(CalculoGeometrico):
    """Clase para calcular el perímetro y área de un rombo."""

    def __init__(self, diagonal_mayor, diagonal_menor):
        super().__init__(diagonal_mayor, diagonal_menor)
        self.__diagonal_mayor = diagonal_mayor
        self.__diagonal_menor = diagonal_menor

    @property
    def diagonal_mayor(self):
        return self.__diagonal_mayor

    @property
    def diagonal_menor(self):
        return self.__diagonal_menor

    def calcular_perimetro(self):
        """Aproxima el lado del rombo usando el Teorema de Pitágoras."""
        lado = math.sqrt((self.__diagonal_mayor / 2) ** 2 + (self.__diagonal_menor / 2) ** 2)
        return round(lado * 4, 2)

    def calcular_area(self):
        return round((self.__diagonal_mayor * self.__diagonal_menor) / 2, 2)


class PoligonoRegular(CalculoGeometrico):
    """Clase para calcular el perímetro y área de un polígono regular (pentágono a decágono)."""

    def __init__(self, lados, longitud):
        if not (5 <= lados <= 10):
            raise ValueError("El número de lados debe estar entre 5 y 10.")
        super().__init__(lados, longitud)
        self.__lados = lados
        self.__longitud = longitud

    @property
    def lados(self):
        return self.__lados

    @property
    def longitud(self):
        return self.__longitud

    def calcular_perimetro(self):
        return round(self.__lados * self.__longitud, 2)

    def calcular_area(self):
        """Usa la fórmula del área: (Perímetro * Apotema) / 2"""
        apotema = self.__longitud / (2 * math.tan(math.pi / self.__lados))
        return round((self.calcular_perimetro() * apotema) / 2, 2)


# ---------------------- PRUEBAS ---------------------- #

if __name__ == "__main__":
    # Círculo
    circulo = Circulo(5)
    print(f"Círculo - Perímetro: {circulo.calcular_perimetro()} | Área: {circulo.calcular_area()}")

    # Triángulo equilátero
    triangulo = Triangulo(3)
    print(f"Triángulo - Perímetro: {triangulo.calcular_perimetro()} | Área: {triangulo.calcular_area()}")

    # Cuadrado
    cuadrado = Cuadrado(4)
    print(f"Cuadrado - Perímetro: {cuadrado.calcular_perimetro()} | Área: {cuadrado.calcular_area()}")

    # Rectángulo
    rectangulo = Rectangulo(4, 6)
    print(f"Rectángulo - Perímetro: {rectangulo.calcular_perimetro()} | Área: {rectangulo.calcular_area()}")

    # Rombo
    rombo = Rombo(6, 4)
    print(f"Rombo - Perímetro: {rombo.calcular_perimetro()} | Área: {rombo.calcular_area()}")

    # Polígono Regular (Pentágono)
    poligono = PoligonoRegular(5, 4)
    print(f"Pentágono - Perímetro: {poligono.calcular_perimetro()} | Área: {poligono.calcular_area()}")

    # Control de errores
    try:
        poligono_invalido = PoligonoRegular(11, 4)  # Error: más de 10 lados
    except ValueError as e:
        print("Error:", e)

    try:
        rectangulo_invalido = Rectangulo(-4, 6)  # Error: valores negativos
    except ValueError as e:
        print("Error:", e)
