'''Ejercicio
Se entregará en un archivo apellido_nombre.py (sin caracteres especiales) en la tarea habilitada en el aula virtual a tal efecto. Las entregas fuera de plazo no serán evaluadas.

1- Definir subclases Tren, Autobus y Bicicleta: 
    - heredan de la superclase viajar
    - tienen un método propio para indicar en que vehículo se hace el viaje
    - sobrescriben el método tiempo_recorrer para devolver el tiempo del recorrido en minutos, teniendo en cuenta que en tren la velocidad media es de 120 km/h, en autobús de 80 km/h y en bicicleta de 20 km/h
    - los objetos instanciados a partir de estas clases únicamente pueden llamar al método detallar viaje, que incluirá una impresión del métodos recorrer, el vehículo utilizado y el tiempo estimado de recorrido. Debe instanciarse al menos un objeto de cada subclase.

2- En base a los detalles del apartado anterior, encapsular los atributos y métodos que se estime oportuno, manteniendo la funcionalidad.

3- Considerar si en la lógica del ejercicio se deben definir métodos abstractos. En caso afirmativo incluirlos, en caso negativo justificar la respuesta en un comentario en el archivo a entregar.
'''

from abc import ABC, abstractmethod

class Viajar(ABC):
    def __init__(self, origen, destino, distancia):
        self.__origen = origen
        self.__destino = destino
        self.__distancia = distancia

    def __recorrer(self):
        print(f"Viajar desde {self.__origen} a {self.__destino}, distancia {self.__distancia} km")

    def _get_distancia(self):
        return self.__distancia

    @abstractmethod
    def _vehiculo(self):
        pass

    @abstractmethod
    def _tiempo_recorrer(self):
        pass

    def detallar_viaje(self):
        self.__recorrer()
        print(f"Vehículo: {self._vehiculo()}")
        print(f"Tiempo estimado: {self._tiempo_recorrer()} minutos")


class Tren(Viajar):
    def _vehiculo(self):
        return "Tren"

    def _tiempo_recorrer(self):
        return round((self._get_distancia() / 120) * 60)


class Autobus(Viajar):
    def _vehiculo(self):
        return "Autobús"

    def _tiempo_recorrer(self):
        return round((self._get_distancia() / 80) * 60)


class Bicicleta(Viajar):
    def _vehiculo(self):
        return "Bicicleta"

    def _tiempo_recorrer(self):
        return round((self._get_distancia() / 20) * 60)


# Instanciación
tren1 = Tren("Madrid", "Toledo", 75)
autobus1 = Autobus("Valencia", "Alicante", 170)
bici1 = Bicicleta("Parque", "Centro", 10)

tren1.detallar_viaje()
print()
autobus1.detallar_viaje()
print()
bici1.detallar_viaje()

'''
Justificación del uso de abstracción:
Se ha definido la clase Viajar como clase abstracta porque representa un concepto general que no se puede instanciar por sí solo. Los métodos _vehiculo y _tiempo_recorrer se han declarado abstractos ya que su implementación depende del transporte concreto.
'''

