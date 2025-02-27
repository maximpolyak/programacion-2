import re
from datetime import datetime

class Persona:
    def __init__(self, nombre, apellido, email, genero, fecha_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__genero = genero
        self.__email = email
        self.__fecha_nacimiento = fecha_nacimiento
        self.__validar_email()

    # Getters y Setters usando @property
    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def genero(self):
        return self.__genero

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        """Valida y actualiza el email."""
        patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(patron_email, nuevo_email):
            raise ValueError("Correo electrónico no válido")
        self.__email = nuevo_email

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @property
    def edad(self):
        """Calcula la edad a partir de la fecha de nacimiento."""
        hoy = datetime.today()
        fecha_nac = datetime.strptime(self.__fecha_nacimiento, "%d-%m-%Y")
        return hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))

    def __validar_email(self):
        """Verifica que el email tenga un formato válido en el constructor."""
        patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(patron_email, self.__email):
            raise ValueError(f"El email {self.__email} no es válido")

    def obtener_datos(self):
        """Devuelve los datos de la persona en un string."""
        return f"{self.nombre} {self.apellido}, {self.edad} años, {self.email}, Género: {self.genero}"


# ---------------------- SUBCLASE EMPLEADO ---------------------- #
class Empleado(Persona):
    CATEGORIAS = {
        "logística": 2000,
        "repartidor": 1800,
        "atención al cliente": 1900,
        "administrativo": 2100,
        "encargado": 2500
    }

    def __init__(self, nombre, apellido, email, genero, fecha_nacimiento, categoria):
        super().__init__(nombre, apellido, email, genero, fecha_nacimiento)
        
        if not (18 <= self.edad <= 66):
            raise ValueError("La edad del empleado debe estar entre 18 y 66 años")

        if categoria not in self.CATEGORIAS:
            raise ValueError("Categoría profesional no válida")

        self.__categoria = categoria

    @property
    def categoria(self):
        return self.__categoria

    @property
    def sueldo(self):
        return self.CATEGORIAS[self.__categoria]

    def obtener_datos(self):
        return f"{super().obtener_datos()}, Categoría: {self.categoria}, Sueldo: {self.sueldo}€"


# ---------------------- SUBCLASE CLIENTE ---------------------- #
class Cliente(Persona):
    def __init__(self, nombre, apellido, email, genero, fecha_nacimiento, pedidos):
        super().__init__(nombre, apellido, email, genero, fecha_nacimiento)
        
        if self.edad < 18:
            raise ValueError("El cliente debe ser mayor de edad")

        self.__pedidos = pedidos

    @property
    def pedidos(self):
        return self.__pedidos

    @property
    def categoria_cliente(self):
        """Asigna una categoría al cliente según el número de pedidos."""
        if self.__pedidos == 0:
            return "nuevo"
        elif self.__pedidos <= 5:
            return "ocasional"
        else:
            return "consolidado"

    def obtener_datos(self):
        return f"{super().obtener_datos()}, Cliente {self.categoria_cliente}, Pedidos: {self.__pedidos}"


# ---------------------- PRUEBAS ---------------------- #
if __name__ == "__main__":
    # Creación de un empleado válido
    empleado = Empleado("Juan", "Pérez", "juan@mail.com", "hombre", "10-05-1990", "encargado")
    print(empleado.obtener_datos())

    # Creación de un cliente válido
    cliente = Cliente("Ana", "Gómez", "ana@mail.com", "mujer", "15-08-1985", 6)
    print(cliente.obtener_datos())

    # Intento de crear un empleado con edad no válida (esto dará error)
    try:
        empleado_invalido = Empleado("Carlos", "López", "carlos@mail.com", "hombre", "10-05-2010", "repartidor")
    except ValueError as e:
        print("Error:", e)

    # Intento de crear un cliente menor de edad (esto dará error)
    try:
        cliente_invalido = Cliente("Sofía", "Ramírez", "sofia@mail.com", "mujer", "15-08-2010", 2)
    except ValueError as e:
        print("Error:", e)
