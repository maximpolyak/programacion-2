import requests

def descargar_archivo(url, nombre_archivo):
    try:
        respuesta = requests.get(url, timeout=100)
        respuesta.raise_for_status
        with open(nombre_archivo,'wb') as archivo:
            archivo.write(respuesta.content)
        return "Descarga completada"
    except requests.HTTPError:
        return "Error HTTP"
    except requests.Timeout:
        return "Timeout"
    except requests.RequestException as e:
        return type(e)