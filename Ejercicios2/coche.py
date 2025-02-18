class Coche:
    precio_litro = 1.5  # Precio del litro de combustible
    
    def __init__(self, marca, modelo, ano, color, deposito, consumo):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color
        self.deposito = deposito
        self.consumo = consumo
        self.combustible_actual = 0
    
    def mostrar_info(self):
        return f'{self.marca} {self.modelo} ({self.ano}), Color: {self.color}, Depósito: {self.deposito}L, Consumo: {self.consumo}L/100km'
    
    def pintar(self, nuevo_color):
        self.color = nuevo_color
        print(f'El coche ha sido pintado de {nuevo_color}')
    
    def estado_combustible(self):
        km_disponibles = (self.combustible_actual / self.consumo) * 100
        return f'Combustible actual: {self.combustible_actual}L, Puede recorrer {km_disponibles:.2f} km'
    
    def añadir_combustible(self):
        cantidad_anadida = self.deposito - self.combustible_actual
        coste = cantidad_anadida * self.precio_litro
        self.combustible_actual = self.deposito
        return f'Añadidos {cantidad_anadida}L, Precio: {coste:.2f}€'
    
    def viajar(self, km):
        combustible_necesario = (km / 100) * self.consumo
        repostajes = combustible_necesario // self.deposito
        if combustible_necesario % self.deposito != 0:
            repostajes += 1
        return f'Para viajar {km} km necesitará repostar {int(repostajes)} veces.'
