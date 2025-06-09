class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        raise Exception("Pila vacía")

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        print("Contenido de la pila (tope → base):")
        for elemento in reversed(self.elementos):
            print(elemento)

if __name__ == "__main__":
    pila_enteros = Pila()
    pila_enteros.apilar(10)
    pila_enteros.apilar(20)
    pila_enteros.apilar(30)
    print("Desapilado:", pila_enteros.desapilar())
    pila_enteros.mostrar()

    pila_strings = Pila()
    pila_strings.apilar("Python")
    pila_strings.apilar("Java")
    pila_strings.apilar("C++")
    print("Desapilado:", pila_strings.desapilar())
    pila_strings.mostrar()