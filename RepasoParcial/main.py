# Fundamentos de la Programación II - Unidad 1: Introducción a la Programación Orientada a Objetos

# ----------------------------------------------------------------------
# 1. ¿Qué es la Programación Orientada a Objetos (POO)?
# ----------------------------------------------------------------------
# Es un paradigma que modela el software en base a "objetos" que tienen
# atributos (datos) y métodos (funciones).
# Cada objeto es una instancia de una clase.
# Ejemplo:
# Clase: Estudiante
# Atributos: nombre, email, notas
# Métodos: agregar_nota, calcular_media

# ----------------------------------------------------------------------
# 2. Pilares de la POO
# ----------------------------------------------------------------------
# - Abstracción: ocultar los detalles complejos y mostrar solo lo esencial.
# - Encapsulamiento: proteger los datos dentro de una clase.
# - Herencia: crear nuevas clases a partir de otras.
# - Polimorfismo: usar métodos comunes en clases distintas.

# ----------------------------------------------------------------------
# 3. Tipos de Variables y Conversiones
# ----------------------------------------------------------------------
edad = 25                  # int
altura = 1.75             # float
es_persona = True         # bool
nombre = "Pepe"           # str

print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}")

# Conversión de tipos
print(float(edad))
print(int(altura))

# Colecciones
frutas = ["manzana", "banana", "cereza"]   # list
bebidas = ("café", "té", "agua")            # tuple
persona = {"nombre": "Ana", "edad": 30}    # dict

# ----------------------------------------------------------------------
# 4. Condicionales y Bucles
# ----------------------------------------------------------------------
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Bucle for
for fruta in frutas:
    print(fruta)

# Bucle while
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1

# ----------------------------------------------------------------------
# 5. Clases y Objetos
# ----------------------------------------------------------------------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Juan", 20)
persona1.saludar()

# Clase con métodos adicionales
class Circulo:
    def __init__(self, radio):
        self.radio = float(radio)

    def perimetro(self):
        return round(2 * 3.1416 * self.radio, 2)

    def area(self):
        return round(3.1416 * self.radio ** 2, 2)

c1 = Circulo(10)
print("Perímetro:", c1.perimetro())
print("Área:", c1.area())

# ----------------------------------------------------------------------
# 6. Atributos de clase vs instancia
# ----------------------------------------------------------------------
class AlumnoFundamentos:
    asignatura = "Fundamentos de la Programación II"  # Atributo de clase

    def __init__(self, nombre, apellido, notamedia):
        self.nombre = nombre
        self.apellido = apellido
        self.notamedia = max(0, min(10, notamedia))

    def mostrarNota(self):
        print(f"{self.nombre} {self.apellido} ha sacado un {self.notamedia} en {AlumnoFundamentos.asignatura}")

    def subirNota(self, nota):
        self.notamedia = round(min(10, self.notamedia + nota), 1)

    def bajarNota(self, nota):
        self.notamedia = round(max(0, self.notamedia - nota), 1)

alumno1 = AlumnoFundamentos("Pepe", "Pérez", 6)
alumno1.subirNota(2)
alumno1.mostrarNota()

# ----------------------------------------------------------------------
# 7. Métodos que llaman a otros métodos
# ----------------------------------------------------------------------
class CestaFruta:
    def __init__(self):
        self.dict_fruta = {}

    def addFrutaDict(self, fruta, n):
        if fruta in self.dict_fruta:
            self.dict_fruta[fruta] += n
        else:
            self.dict_fruta[fruta] = n

    def addFruta(self, fruta):
        self.addFrutaDict(fruta, 1)

    def addMoreFruta(self, fruta, n):
        self.addFrutaDict(fruta, n)

cesta = CestaFruta()
cesta.addFruta("manzana")
cesta.addMoreFruta("pera", 3)
print(cesta.dict_fruta)

# Fin del resumen de la Unidad 1

# ----------------------------------------------------------------------
# 8. Unidad 2: Encapsulación
# ----------------------------------------------------------------------
# El encapsulamiento permite ocultar los atributos internos de una clase.
# En Python, los atributos privados se declaran con dos guiones bajos (__)

class PersonaEncap:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")

persona = PersonaEncap("Ana", 22)
print(persona.get_nombre())
persona.set_nombre("Elena")
print(persona.get_nombre())

# Decorador @property
class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La base debe ser un entero positivo")
        self.__base = valor

    def area(self):
        return self.__base * self.__altura

r = Rectangulo(2, 3)
print("Área:", r.area())

# ----------------------------------------------------------------------
# 9. Unidad 2: Herencia
# ----------------------------------------------------------------------
# La herencia permite crear clases hijas que heredan atributos y métodos
# de clases padre.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def describir(self):
        print(f"{self.nombre}, {self.edad} años")

    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print(f"{self.nombre} dice: Guau")

perro = Perro("Rex", 4)
perro.describir()
perro.sonido()

# Herencia múltiple
class Alimentacion:
    def __init__(self, tipo):
        self.tipo = tipo

    def describir_alimentacion(self):
        print(f"Tipo de alimentación: {self.tipo}")

class Gato(Animal, Alimentacion):
    def __init__(self, nombre, edad, tipo):
        Animal.__init__(self, nombre, edad)
        Alimentacion.__init__(self, tipo)

    def sonido(self):
        print(f"{self.nombre} dice: Miau")

gato = Gato("Michi", 3, "carnívoro")
gato.describir()
gato.sonido()
gato.describir_alimentacion()

# Encapsulación + Herencia con @property
class AnimalProp:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

class Sapo(AnimalProp):
    def croar(self):
        print(f"{self.nombre} croa")

s = Sapo("Ojazos")
s.croar()

# Fin de Unidad 2: Encapsulación y Herencia

# ----------------------------------------------------------------------
# 10. Unidad 3: Polimorfismo
# ----------------------------------------------------------------------
# Polimorfismo: capacidad de un objeto de comportarse de distintas formas.
# En Python, se manifiesta especialmente gracias al duck typing.

# Ejemplo básico:
class Pato:
    def hablar(self):
        print("¡Cua, Cua!")

class Perro:
    def hablar(self):
        print("¡Guau, Guau!")

class Gato:
    def hablar(self):
        print("¡Miau, Miau!")

animales = [Pato(), Perro(), Gato()]
for animal in animales:
    animal.hablar()

# Esto es posible aunque no haya herencia, porque todos tienen el método "hablar"

# ----------------------------------------------------------------------
# 11. Duck Typing
# ----------------------------------------------------------------------
# "Si camina como un pato y suena como un pato, es un pato"
# Lo importante no es el tipo, sino los métodos que implementa.

def llamar_hablar(x):
    x.hablar()

llamar_hablar(Pato())  # ¡Cua, Cua!
llamar_hablar(Perro()) # ¡Guau, Guau!

# ----------------------------------------------------------------------
# 12. Polimorfismo de operadores
# ----------------------------------------------------------------------
print(2 + 5)          # 7 (suma de enteros)
print("2" + "5")      # "25" (concatenación)
print("2" * 5)        # "22222" (repetición de cadena)

# Sobrecarga del operador + en clases personalizadas:
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Punto(2, 3)
p2 = Punto(5, 1)
print(p1 + p2)  # (7, 4)

# ----------------------------------------------------------------------
# 13. Polimorfismo de métodos
# ----------------------------------------------------------------------
# La misma función puede comportarse de manera distinta según el tipo:
print(len("cadena"))      # 6
print(len([1, 2, 3]))      # 3
print(len({1: "a", 2: "b"})) # 2

# ----------------------------------------------------------------------
# 14. Polimorfismo de subtipos (herencia)
# ----------------------------------------------------------------------
class Animal:
    def hablar(self):
        print("Sonido genérico")

class Vaca(Animal):
    def hablar(self):
        print("¡Muuu, Muuu!")

animal = Animal()
animal.hablar()
vaca = Vaca()
vaca.hablar()

# ----------------------------------------------------------------------
# 15. Overriding y Overloading
# ----------------------------------------------------------------------
# Overriding: redefinir un método de la clase padre en la hija
class A:
    def metodo(self):
        print("Método de clase A")

class B(A):
    def metodo(self):
        print("Método sobrescrito en clase B")

b = B()
b.metodo()  # Método sobrescrito en clase B

# Overloading en Python: se simula con *args o validación manual de argumentos
class Ser:
    def mover(self, ser=None):
        if ser == "humano":
            print("anda")
        elif ser == "mosca":
            print("vuela")
        elif ser == "serpiente":
            print("repta")
        else:
            print("No se reconoce el ser")

s = Ser()
s.mover("mosca")  # vuela
s.mover("alien")   # No se reconoce el ser

# Fin de Unidad 3: Polimorfismo

# ----------------------------------------------------------------------
# 16. Unidad 4: Abstracción
# ----------------------------------------------------------------------
# La abstracción consiste en ocultar los detalles internos y mostrar solo lo esencial.
# Nos permite trabajar con interfaces más simples mientras la complejidad está escondida.

# Beneficios:
# - Código más legible y modular
# - Más fácil de mantener
# - Fomenta la reutilización

# ----------------------------------------------------------------------
# 17. Abstracción mediante funciones
# ----------------------------------------------------------------------
def average(lista):
    return sum(lista) / len(lista)

def max_difference(lista):
    return max(lista) - min(lista)

print("Edad promedio:", average([19,21,23,30,25,18,22,23,22,18]))
print("Máx. dif edad:", max_difference([19,21,23,30,25,18,22,23,22,18]))

# ----------------------------------------------------------------------
# 18. Abstracción mediante generadores
# ----------------------------------------------------------------------
def generador_simple():
    yield 1
    yield 2
    yield 3

gen = generador_simple()
print(next(gen))
print(next(gen))
print(next(gen))

# Generador con bucle:
def contar_hasta(n):
    for i in range(1, n+1):
        yield i

for num in contar_hasta(3):
    print(num)

# Generador con expresión:
cuadrados = (x**2 for x in range(5))
for n in cuadrados:
    print(n)

# ----------------------------------------------------------------------
# 19. Abstracción mediante comprensiones
# ----------------------------------------------------------------------
lista1 = [x for x in range(5)]
lista2 = [x+10 for x in range(5)]
lista3 = [x**2 * 10 for x in range(5)]
lista4 = [x+1 for x in range(10) if x > 0 and x % 2 == 0]

print(lista1)
print(lista2)
print(lista3)
print(lista4)

# Set comprehension:
palabra = "ballenato"
set1 = {a for a in palabra if a != "t"}
print(set1)

# Dict comprehension:
claves = ['nombre', 'edad', 'ciudad']
valores = ['Amelia', 30, 'Barcelona']
dict1 = {k: v for k, v in zip(claves, valores)}
print(dict1)

# ----------------------------------------------------------------------
# 20. Abstracción mediante clases abstractas
# ----------------------------------------------------------------------
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        import math
        return math.pi * self.radio**2

    def perimetro(self):
        import math
        return 2 * math.pi * self.radio

c = Circulo(5)
print(c.area())
print(c.perimetro())

# ----------------------------------------------------------------------
# 21. Decoradores (Function wrappers)
# ----------------------------------------------------------------------
def midecorador(func):
    def wrapper():
        print("Antes de ejecutar")
        func()
        print("Después de ejecutar")
    return wrapper

@midecorador
def saluda():
    print("Hola desde dentro de la función")

saluda()

# Decorador que mide tiempo de ejecución:
import time

def time_counter(func):
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, "tardó", end - start)
        return result
    return wrap

@time_counter
def countdown(n):
    while n > 0:
        n -= 1

countdown(1000000)

# Fin de Unidad 4: Abstracción

# ----------------------------------------------------------------------
# 22. Unidad 5: Tratamiento de excepciones
# ----------------------------------------------------------------------
# Las excepciones permiten gestionar errores sin que se detenga el programa.
# Las excepciones se lanzan automáticamente o manualmente con `raise`.

# ----------------------------------------------------------------------
# 23. Excepciones automáticas
# ----------------------------------------------------------------------
# Ejemplos:
a = 1; b = 0
# print(a / b)  # ZeroDivisionError

# print(2 + "2")  # TypeError

# ----------------------------------------------------------------------
# 24. Capturar excepciones con try-except
# ----------------------------------------------------------------------
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Error: no se puede dividir por 0")

try:
    y = 2 + "3"
except TypeError:
    print("Error: no se pueden sumar tipos distintos")

# Múltiples except
try:
    z = 2 + "2"
except ZeroDivisionError:
    print("División entre cero")
except TypeError:
    print("Error de tipo")
except Exception as e:
    print("Error inesperado:", type(e))

# Uso de else y finally
try:
    resultado = 10 / 2
except Exception:
    print("Algo ha fallado")
else:
    print("Todo bien, resultado:", resultado)
finally:
    print("Fin del bloque try-except")

# ----------------------------------------------------------------------
# 25. Lanzar excepciones manualmente con raise
# ----------------------------------------------------------------------
# raise TipoDeError("mensaje")

# raise ValueError("Este es un error de valor")

# ----------------------------------------------------------------------
# 26. Crear excepciones personalizadas
# ----------------------------------------------------------------------
class MiErrorPersonal(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

try:
    raise MiErrorPersonal("Algo salió mal")
except MiErrorPersonal as e:
    print("Error capturado:", e.mensaje)

# Otra forma: pasando diccionario
class MiErrorConDetalles(Exception):
    pass

try:
    raise MiErrorConDetalles({"msg": "Error crítico", "code": 500})
except MiErrorConDetalles as e:
    detalles = e.args[0]
    print("Mensaje:", detalles["msg"])
    print("Código:", detalles["code"])

# ----------------------------------------------------------------------
# 27. Uso de assert
# ----------------------------------------------------------------------
# assert condición
# Si la condición es falsa, lanza AssertionError

assert(1 + 1 == 2)  # No lanza error
# assert(1 + 1 == 3)  # AssertionError

# Comprobación en funciones
def suma_enteros(a, b):
    assert isinstance(a, int)
    assert isinstance(b, int)
    return a + b

print(suma_enteros(2, 3))
# print(suma_enteros(2.0, 3.0))  # AssertionError

# Comprobación con clases
class Animal:
    pass

class Perro(Animal):
    pass

firulais = Perro()
assert isinstance(firulais, Animal)  # OK
# assert isinstance(firulais, str)  # AssertionError

# Fin de Unidad 5: Tratamiento de excepciones