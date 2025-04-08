from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Mascota(ABC):
    def __init__(self, nombre, edad, ultima_visita):
        self._nombre = nombre
        self._edad = edad
        self._ultima_visita = ultima_visita  # tipo datetime
        self._animal = None
        self._tipo = None

    def _presentar(self):
        return f"{self._nombre} es un {self._animal} de {self._edad} años."

    @abstractmethod
    def _visitar_veterinario(self):
        pass

    @abstractmethod
    def _obtener_tipo(self):
        pass

    def detallar_mascota(self):
        return (
            f"{self._presentar()}\n"
            f"Tipo/Raza: {self._obtener_tipo()}\n"
            f"Próxima visita al veterinario: {self._visitar_veterinario().strftime('%Y-%m-%d')}"
        )


class Perro(Mascota):
    def __init__(self, nombre, edad, raza, ultima_visita):
        super().__init__(nombre, edad, ultima_visita)
        self._animal = "Perro"
        self._tipo = raza
        self.__frecuencia_meses = 6

    def _obtener_tipo(self):
        return self._tipo

    def _visitar_veterinario(self):
        return self._ultima_visita + timedelta(days=30 * self.__frecuencia_meses)


class Gato(Mascota):
    def __init__(self, nombre, edad, raza, ultima_visita):
        super().__init__(nombre, edad, ultima_visita)
        self._animal = "Gato"
        self._tipo = raza
        self.__frecuencia_meses = 6

    def _obtener_tipo(self):
        return self._tipo

    def _visitar_veterinario(self):
        return self._ultima_visita + timedelta(days=30 * self.__frecuencia_meses)


class Loro(Mascota):
    def __init__(self, nombre, edad, especie, ultima_visita):
        super().__init__(nombre, edad, ultima_visita)
        self._animal = "Loro"
        self._tipo = especie
        self.__frecuencia_meses = 12

    def _obtener_tipo(self):
        return self._tipo

    def _visitar_veterinario(self):
        return self._ultima_visita + timedelta(days=30 * self.__frecuencia_meses)
