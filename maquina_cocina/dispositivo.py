from abc import ABC, abstractmethod

class DispositivoCocina(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def programar(self, programa, ingredientes):
        pass

    @abstractmethod
    def mostrar_recetas(self):
        pass
