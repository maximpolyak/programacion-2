class Libro:
    def __init__(self, titulo, autor, publicacion):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
    
    def mostrar_info(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Año: {self.publicacion}'
