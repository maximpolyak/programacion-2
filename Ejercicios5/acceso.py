import hashlib

# Excepciones personalizadas
class MenorEdadError(Exception):
    pass

class AccesoDenegadoError(Exception):
    pass

# Usuarios bloqueados
usuarios_bloqueados = {
    "usuario1": "bloqueado",
    "juan123": "bloqueado",
    "admin": "bloqueado"
}

def encriptar_clave(clave):
    return hashlib.sha1(clave.encode()).hexdigest()

def verificar_acceso():
    try:
        usuario = input("Introduce tu nombre de usuario: ")
        edad = int(input("Introduce tu edad: "))
        clave = input("Introduce tu clave: ")

        if edad < 18:
            raise MenorEdadError("Acceso denegado: el usuario es menor de edad.")

        if usuario in usuarios_bloqueados:
            raise AccesoDenegadoError(f"Acceso denegado: el usuario '{usuario}' está bloqueado.")

        clave_encriptada = encriptar_clave(clave)
        print(f"Acceso permitido. Clave encriptada (SHA1): {clave_encriptada}")

    except MenorEdadError as e:
        print("Error:", e)
    except AccesoDenegadoError as e:
        print("Error:", e)
    except ValueError:
        print("Error: la edad debe ser un número entero.")
    except Exception as e:
        print("Se ha producido un error inesperado:", type(e), "-", e)

verificar_acceso()
