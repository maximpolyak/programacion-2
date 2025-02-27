import random

class Ahorcado:
    def __init__(self):
        """Inicializa el juego con una palabra aleatoria y los intentos disponibles."""
        self.__intentos = 6
        self.__letras = []
        self.__encontradas = []
        self.__palabras = []

        # Cargar palabras desde archivo
        try:
            with open("./Tema2/ahorcado_palabras.txt", "r", encoding="utf-8") as archivo:
                self.__palabras = [line.strip() for line in archivo.readlines()]
        except FileNotFoundError:
            print("No se encontró el archivo de palabras. Se usará una por defecto.")
            self.__palabras = ["ballena", "elefante", "computadora"]

        # Selección de palabra aleatoria
        self.__palabra = random.choice(self.__palabras) if self.__palabras else "ballena"
        self.__letras = ['_'] * len(self.__palabra)

    def __coincidencia(self, letra: str) -> bool:
        """Busca si la letra está en la palabra y la revela."""
        if letra in self.__palabra:
            for i, w in enumerate(self.__palabra):
                if w == letra:
                    self.__letras[i] = letra
                    self.__encontradas.append(letra)
            return True
        return False

    def __dibujar(self):
        """Muestra la figura del ahorcado según los intentos restantes."""
        figuras = [
            "________\n|   |\n|   O\n|  |||\n|   /|\n|",
            "________\n|   |\n|   O\n|  |||\n|   |\n|",
            "________\n|   |\n|   O\n|  ||\n|\n|",
            "________\n|   |\n|   O\n|   |\n|\n|",
            "________\n|   |\n|   O\n|\n|\n|",
            "________\n|   |\n|\n|\n|\n|"
        ]
        print(figuras[self.__intentos])

    def jugar(self):
        """Inicia la partida y gestiona el flujo del juego."""
        print(f"Encuentra la palabra: {' '.join(self.__letras)}")

        while self.__intentos > 0:
            letra = input("Escribe una letra: ").lower()

            if len(letra) != 1 or not letra.isalpha():
                print("Por favor, introduce una única letra válida.")
                continue

            if letra in self.__encontradas:
                print("Ya has adivinado esta letra. Intenta otra.")
                continue

            if self.__coincidencia(letra):
                print(f"¡Bien! {' '.join(self.__letras)}")
                if ''.join(self.__letras) == self.__palabra:
                    print(f"¡Enhorabuena! La palabra era {self.__palabra}")
                    return
            else:
                self.__intentos -= 1
                print(f"No, lo siento. Intentos restantes: {self.__intentos}")
                self.__dibujar()

        print(f"Lo siento, has perdido. La palabra era {self.__palabra}")

# Ejecutar el juego
partida = Ahorcado()
partida.jugar()
