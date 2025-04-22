'''Un paciente quiere confirmar una cita con un médico. Tenemos una clase cita con un método paciente y un método doctor, lanzamos dos hilos independientes, uno para el paciente y otro para el médico. Para que el paciente reciba la confirmación de la cita debe confirmarla el doctor.
'''


import threading 
import time
import random

# Creamos un objeto Condition para sincronizar los hilos
condicion = threading.Condition()

class Cita:
    def __init__(self):
        self.cita_confirmada = False  # Variable compartida entre los hilos

    def paciente(self, nombre):
        print(f"El paciente {nombre} está esperando una cita.")
        with condicion:  # Adquiere el bloqueo asociado a la condición<
            while not self.cita_confirmada:  # Espera hasta que la cita se confirme
                condicion.wait()  # El hilo se bloquea esperando una notificación
            print(f"{nombre} tiene su cita confirmada.")

    def doctor(self, nombre, especialidad):
        print(f"{nombre}, de {especialidad}, está consultando su agenda.")
        time.sleep(2)  # Simulamos el tiempo que tarda el médico en comprobar la agenda
        hora = random.randint(8, 13)
        print("Agenda comprobada.")
        print(f"La hora de la cita es las {hora}:00.")
        with condicion:  # Adquiere el bloqueo asociado a la condición
            self.cita_confirmada = True  # Modifica la variable compartida
            condicion.notify()  # Notifica al hilo paciente que puede continuar

# Creamos la instancia de la clase
cita = Cita()

# Creamos y lanzamos los hilos para el paciente y el médico
hilo_paciente = threading.Thread(target=cita.paciente, args=("Pepe Pérez",))
hilo_doctor = threading.Thread(target=cita.doctor, args=("Dr. Juan Gómez", "Traumatología"))

hilo_paciente.start()
hilo_doctor.start()

# Esperamos a que ambos hilos terminen
hilo_paciente.join()
hilo_doctor.join()
