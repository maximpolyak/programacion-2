from rectangulo import Rectangulo
from libro import Libro
from cuenta_bancaria import CuentaBancaria
from coche import Coche

# Pruebas
print("--- Rectángulo ---")
r = Rectangulo(10, 5)
print("Área:", r.area())
print("Perímetro:", r.perimetro())

print("\n--- Libro ---")
l = Libro("1984", "George Orwell", 1949)
print(l.mostrar_info())

print("\n--- Cuenta Bancaria ---")
cb = CuentaBancaria("Juan Pérez", 1000)
cb.depositar(500)
cb.retirar(200)
print(cb.mostrar_saldo())

print("\n--- Coche ---")
c = Coche("Volkswagen", "Beetle", 2020, "Rojo", 50, 5)
print(c.mostrar_info())
c.pintar("Azul")
print(c.estado_combustible())
print(c.añadir_combustible())
print(c.viajar(1500))