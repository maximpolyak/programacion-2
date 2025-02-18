class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        print(f'Saldo antes: {self.saldo}€')
        self.saldo += cantidad
        print(f'Depositado: {cantidad}€ | Saldo después: {self.saldo}€')
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print('Fondos insuficientes')
        else:
            print(f'Saldo antes: {self.saldo}€')
            self.saldo -= cantidad
            print(f'Retirado: {cantidad}€ | Saldo después: {self.saldo}€')
    
    def mostrar_saldo(self):
        return f'Saldo actual: {self.saldo}€'