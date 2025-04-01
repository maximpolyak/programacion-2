import time
import threading

def viajar():
    print("Está listo para viajar")
    time.sleep(4)
    print("Ha llegado")

def contestar_mensajes():
    print("Está listo para contestar mensajes")
    time.sleep(2)
    print("Ha acabado")

#viajar()
#contestar_mensajes()

threading.Thread(target=viajar).start()
threading.Thread(target=contestar_mensajes).start()
