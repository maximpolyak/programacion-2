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


#clase viajar - superclase
class Viajar():
    
    def __init__(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia

    def recorrer(self):
        print(f"Viajar desde {self.origen} a {self.destino}, distancia {self.distancia} km")

    def tiempo_recorrer(self):
        pass

    def detallar_viaje(self):
        pass
