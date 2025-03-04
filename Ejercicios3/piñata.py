import random

class Chuche:
    def __init__(self, tipo, descripcion):
        self.tipo = tipo
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.tipo} de {self.descripcion}"

class Pinata:
    TIPOS_CHUCHES = [
        ("Caramelo", ["limón", "naranja", "melón"]),
        ("Chicle", ["fresa", "menta"]),
        ("Piruleta", ["fresa", "limón"]),
        ("Gominola", ["osito", "melocotón"]),
        ("Regaliz", ["negro", "rojo"])
    ]

    def __init__(self, forma, num_chuches):
        self.forma = forma
        self.chuches = self.rellenar(num_chuches)

    def rellenar(self, cantidad):
        """Genera una lista aleatoria de chuches"""
        lista_chuches = []
        for _ in range(cantidad):
            tipo, opciones = random.choice(self.TIPOS_CHUCHES)
            descripcion = random.choice(opciones)
            lista_chuches.append(Chuche(tipo, descripcion))
        return lista_chuches

    def __str__(self):
        descripcion = f"Mi piñata es un {self.forma} con {len(self.chuches)} chuches\n"
        descripcion += "\n".join(f"- {chuche}" for chuche in self.chuches)
        return descripcion

# Ejemplo de uso
pinata = Pinata("burro", 20)
print(pinata)
