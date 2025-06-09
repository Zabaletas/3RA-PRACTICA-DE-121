class Catalogo:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def buscar(self, indice):
        if 0 <= indice < len(self.elementos):
            return self.elementos[indice]
        raise IndexError("Índice fuera de rango")

if __name__ == "__main__":
    catalogo_libros = Catalogo()
    catalogo_libros.agregar("Cien años de soledad")
    catalogo_libros.agregar("1984")
    print("Libro en posición 0:", catalogo_libros.buscar(0))

    catalogo_productos = Catalogo()
    catalogo_productos.agregar(100)
    catalogo_productos.agregar(200)
    print("Producto en posición 1:", catalogo_productos.buscar(1))