from typing import List, Optional

class Cliente:
    def __init__(self, id: int, nombre: str, telefono: int):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def get_id(self) -> int: return self.id
    def get_nombre(self) -> str: return self.nombre
    def get_telefono(self) -> int: return self.telefono

    def __str__(self):
        return f"Cliente [id={self.id}, nombre={self.nombre}, telefono={self.telefono}]"

class ArchivoCliente:
    def __init__(self, nomA: str):
        self.nomA = nomA
        self.clientes: List[Cliente] = []

    def crearArchivo(self): pass # Placeholder

    # a) Implementar el diagrama de clases (including guardaCliente)
    def guardaCliente(self, c: Cliente):
        if self.buscarCliente(c.get_id()) is None: # Avoid duplicates by ID
            self.clientes.append(c)

    # b) Implementa buscarCliente(int c) a través del id.
    def buscarCliente(self, id_cliente: int) -> Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.get_id() == id_cliente:
                return cliente
        return None

    # c) Implementa buscarCelularCliente(int c), que devuelva los datos del cliente junto al número de celular.
    def buscarCelularCliente(self, id_cliente: int) -> Optional[Cliente]:
        cliente = self.buscarCliente(id_cliente)
        if cliente:
            print(f"Cliente (ID: {id_cliente}): {cliente.get_nombre()}, Celular: {cliente.get_telefono()}")
        return cliente

if __name__ == "__main__":
    mi_archivo_clientes = ArchivoCliente("ClientesVIP")
    mi_archivo_clientes.crearArchivo()

    # a) Implementación de clases y guardaCliente
    cl1 = Cliente(101, "Sofia Ramirez", 77712345)
    cl2 = Cliente(102, "Diego Torres", 60123456)
    cl3 = Cliente(103, "Laura Castro", 70098765)
    mi_archivo_clientes.guardaCliente(cl1)
    mi_archivo_clientes.guardaCliente(cl2)
    mi_archivo_clientes.guardaCliente(cl3)
    mi_archivo_clientes.guardaCliente(Cliente(102, "Duplicado", 11111111)) # Attempt to add duplicate

    # b) Buscar cliente por ID
    cliente_encontrado = mi_archivo_clientes.buscarCliente(102)
    if cliente_encontrado:
        print(f"Cliente encontrado por ID: {cliente_encontrado}")
    else:
        print("Cliente con ID 102 no encontrado.")

    # c) Buscar celular de cliente por ID
    cliente_con_celular = mi_archivo_clientes.buscarCelularCliente(101)
    if cliente_con_celular is None:
        print("Cliente con ID 101 no encontrado para buscar celular.")