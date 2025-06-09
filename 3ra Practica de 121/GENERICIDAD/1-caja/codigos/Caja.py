class Caja:
    def __init__(self):
        self.contenido = None

    def guardar(self, nuevo_contenido):
        self.contenido = nuevo_contenido

    def obtener(self):
        return self.contenido

if __name__ == "__main__":
    caja_str = Caja()
    caja_str.guardar("Hola Mundo")

    caja_int = Caja()
    caja_int.guardar(42)

    print("Caja String:", caja_str.obtener())
    print("Caja Int:", caja_int.obtener())