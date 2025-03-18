from abc import ABC, abstractmethod

class Alexa(ABC):

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def cambiar_estado(self):
        pass


class TV(Alexa):
    def __init__(self):
        self.encendida = False

    def encender(self):
        self.encendida = True
        print("TV encendida, mostrando canal principal.")

    def apagar(self):
        self.encendida = False
        print("TV apagada.")

    def cambiar_estado(self):
        if self.encendida:
            print("Cambiando al siguiente canal.")
        else:
            print("La TV está apagada. No se puede cambiar de canal.")


class ReproductorMusica(Alexa):
    def __init__(self):
        self.sonando = False

    def encender(self):
        self.sonando = True
        print("Reproductor de música encendido, reproduciendo canción.")

    def apagar(self):
        self.sonando = False
        print("Reproductor de música apagado.")

    def cambiar_estado(self):
        if self.sonando:
            print("Pausando la canción actual.")
            self.sonando = False
        else:
            print("Reanudando la canción.")
            self.sonando = True


class Luces(Alexa):
    def __init__(self):
        self.estado = False

    def encender(self):
        self.estado = True
        print("Luces encendidas.")

    def apagar(self):
        self.estado = False
        print("Luces apagadas.")

    def cambiar_estado(self):
        self.estado = not self.estado
        print(f"Luces {'encendidas' if self.estado else 'apagadas'} (cambio de estado).")


class ControlTemperatura(Alexa):
    def __init__(self):
        self.temperatura = 22  # Temperatura inicial por defecto

    def encender(self):
        print(f"Control de temperatura encendido, ajustado a {self.temperatura}ºC.")

    def apagar(self):
        print("Control de temperatura apagado.")

    def cambiar_estado(self):
        self.temperatura += 1
        print(f"Temperatura aumentada a {self.temperatura}ºC.")


class Rumba(Alexa):
    def __init__(self):
        self.limpiando = False

    def encender(self):
        self.limpiando = True
        print("Rumba encendida, empezando limpieza.")

    def apagar(self):
        self.limpiando = False
        print("Rumba apagada, regresando a la base.")

    def cambiar_estado(self):
        if self.limpiando:
            print("Pausando limpieza.")
            self.limpiando = False
        else:
            print("Reanudando limpieza.")
            self.limpiando = True


# Ejemplo de uso
dispositivos = [TV(), ReproductorMusica(), Luces(), ControlTemperatura(), Rumba()]

for dispositivo in dispositivos:
    dispositivo.encender()
    dispositivo.cambiar_estado()
    dispositivo.apagar()
    print("---")