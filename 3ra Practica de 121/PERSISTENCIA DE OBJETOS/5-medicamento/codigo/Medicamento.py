from typing import List, Optional

class Medicamento:
    def __init__(self, nombre: str = "", cod_medicamento: int = 0, tipo: str = "", precio: float = 0.0):
        self.nombre = nombre
        self.cod_medicamento = cod_medicamento
        self.tipo = tipo
        self.precio = precio

    def leer(self):
        self.nombre = input("Nombre del medicamento: ")
        self.cod_medicamento = int(input("Código: "))
        self.tipo = input("Tipo (ej. Tos, Resfrio): ")
        self.precio = float(input("Precio: "))

    def mostrar(self):
        print(f"  Medicamento: {self.nombre} (Cod: {self.cod_medicamento}, Tipo: {self.tipo}, Precio: {self.precio:.2f} Bs.)")

    def get_tipo(self) -> str: return self.tipo
    def get_precio(self) -> float: return self.precio
    def get_nombre(self) -> str: return self.nombre

    def __str__(self): return f"Medicamento [Nombre: {self.nombre}, Tipo: {self.tipo}]"
    def __repr__(self): return self.__str__()


class Farmacia:
    def __init__(self, nombre_farmacia: str = "", sucursal: int = 0, direccion: str = ""):
        self.nombre_farmacia = nombre_farmacia
        self.sucursal = sucursal
        self.direccion = direccion
        self.nro_medicamentos = 0
        self.medicamentos: List[Medicamento] = []

    def leer(self):
        self.nombre_farmacia = input("\nNombre de la farmacia: ")
        self.sucursal = int(input("Número de sucursal: "))
        self.direccion = input("Dirección: ")
        num_meds = int(input("Cuántos medicamentos desea agregar: "))
        for i in range(num_meds):
            med = Medicamento()
            med.leer()
            self.medicamentos.append(med)
            self.nro_medicamentos += 1

    def mostrar(self):
        print(f"\n--- Farmacia: {self.nombre_farmacia} (Sucursal: {self.sucursal}) ---")
        print(f"  Dirección: {self.direccion}")
        print(f"  Número de medicamentos: {self.nro_medicamentos}")
        for med in self.medicamentos:
            med.mostrar()

    def get_direccion(self) -> str: return self.direccion
    def get_sucursal(self) -> int: return self.sucursal
    def get_medicamentos(self) -> List[Medicamento]: return self.medicamentos
    def busca_medicamento(self, nombre_med: str) -> Optional[Medicamento]:
        for med in self.medicamentos:
            if med.get_nombre().lower() == nombre_med.lower():
                return med
        return None


class ArchFarmacia:
    def __init__(self, na: str = ""):
        self.na = na
        self.farmacias: List[Farmacia] = []

    def crearArchivo(self): pass # Placeholder

    # a) Crear, leer y mostrar un Archivo de Farmacias - 'adicionar' handles creation/reading data.
    def adicionar(self):
        farmacia = Farmacia()
        farmacia.leer()
        self.farmacias.append(farmacia)

    # a) 'listar' handles displaying the archive.
    def listar(self):
        if not self.farmacias:
            print("\nNo hay farmacias en el archivo.")
            return
        print(f"\n--- Listado de Farmacias en '{self.na}' ---")
        for farmacia in self.farmacias:
            farmacia.mostrar()
        print("-------------------------------------")

    # The following methods are placed here as per diagram, operating on farmacias.
    def mostrarMedicamentosResfrios(self):
        print("\n--- Medicamentos para el Resfrio (todas las farmacias) ---")
        for farmacia in self.farmacias:
            for med in farmacia.get_medicamentos():
                if med.get_tipo().lower() == "resfrio":
                    print(f"  En {farmacia.nombre_farmacia} Sucursal {farmacia.sucursal}:")
                    med.mostrar()

    def precioMedicamentoTos(self) -> float:
        total_precio = 0.0
        for farmacia in self.farmacias:
            for med in farmacia.get_medicamentos():
                if med.get_tipo().lower() == "tos":
                    total_precio += med.get_precio()
        return total_precio

    def mostrarMedicamentosMenorTos(self):
        print("\n--- Medicamentos de Tos con Precio Menor a 50 Bs. (todas las farmacias) ---")
        for farmacia in self.farmacias:
            for med in farmacia.get_medicamentos():
                if med.get_tipo().lower() == "tos" and med.get_precio() < 50.0:
                    print(f"  En {farmacia.nombre_farmacia} Sucursal {farmacia.sucursal}:")
                    med.mostrar()


if __name__ == "__main__":
    mi_archivo_farmacias = ArchFarmacia("MiFarmaciaCentral")
    mi_archivo_farmacias.crearArchivo()

    # a) Crear, leer y mostrar un Archivo de Farmacias - Adding sample data for demonstration
    farmacia1 = Farmacia("Farmacorp", 1, "Av. Siempre Viva 123")
    farmacia1.medicamentos.append(Medicamento("Aspirina", 1, "Analgesico", 15.0))
    farmacia1.medicamentos.append(Medicamento("Jarabe Tos", 2, "Tos", 35.0))
    farmacia1.medicamentos.append(Medicamento("Grifriex", 3, "Resfrio", 25.0))
    farmacia1.nro_medicamentos = len(farmacia1.medicamentos)
    mi_archivo_farmacias.farmacias.append(farmacia1)

    farmacia2 = Farmacia("Farmacia del Pueblo", 2, "Calle Larga 456")
    farmacia2.medicamentos.append(Medicamento("Ibuprofeno", 4, "Analgesico", 20.0))
    farmacia2.medicamentos.append(Medicamento("Antitusivo Forte", 5, "Tos", 55.0))
    farmacia2.medicamentos.append(Medicamento("Golpex", 6, "Tos", 40.0)) # Key medication for (c)
    farmacia2.nro_medicamentos = len(farmacia2.medicamentos)
    mi_archivo_farmacias.farmacias.append(farmacia2)

    farmacia3 = Farmacia("Farmacia Central", 3, "Plaza Principal 789")
    farmacia3.medicamentos.append(Medicamento("Paracetamol", 7, "Analgesico", 10.0))
    farmacia3.medicamentos.append(Medicamento("Vick Vapo", 8, "Resfrio", 30.0))
    farmacia3.medicamentos.append(Medicamento("Golpex", 9, "Tos", 38.0)) # Another Golpex for (c)
    farmacia3.nro_medicamentos = len(farmacia3.medicamentos)
    mi_archivo_farmacias.farmacias.append(farmacia3)

    print("\n--- Contenido Inicial del Archivo de Farmacias ---")
    mi_archivo_farmacias.listar()

    # b) Mostrar los medicamentos para la tos, de la Sucursal numero X
    sucursal_x = 2
    print(f"\n--- Medicamentos para la tos de la Sucursal {sucursal_x} ---")
    found_in_sucursal = False
    for farmacia in mi_archivo_farmacias.farmacias:
        if farmacia.get_sucursal() == sucursal_x:
            found_in_sucursal = True
            found_tos_meds = False
            for med in farmacia.get_medicamentos():
                if med.get_tipo().lower() == "tos":
                    med.mostrar()
                    found_tos_meds = True
            if not found_tos_meds:
                print(f"No hay medicamentos para la tos en la Sucursal {sucursal_x}.")
            break
    if not found_in_sucursal:
        print(f"Sucursal número {sucursal_x} no encontrada.")

    # c) Mostrar el número de sucursal y su dirección que tienen el medicamento “Golpex”.
    print("\n--- Sucursales con el medicamento 'Golpex' ---")
    golpex_found = False
    for farmacia in mi_archivo_farmacias.farmacias:
        if farmacia.busca_medicamento("Golpex"):
            print(f"Sucursal: {farmacia.get_sucursal()}, Dirección: {farmacia.get_direccion()}")
            golpex_found = True
    if not golpex_found:
        print("Ninguna sucursal tiene el medicamento 'Golpex'.")

    # Example calls for other methods from ArchFarmacia (as per diagram)
    # mi_archivo_farmacias.mostrarMedicamentosResfrios()
    # print(f"\nPrecio total de medicamentos para la tos: {mi_archivo_farmacias.precioMedicamentoTos():.2f} Bs.")
    # mi_archivo_farmacias.mostrarMedicamentosMenorTos()