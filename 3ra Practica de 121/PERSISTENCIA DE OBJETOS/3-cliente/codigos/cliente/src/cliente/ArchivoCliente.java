package cliente;
//ArchivoCliente.java
import java.util.ArrayList;
import java.util.List;

public class ArchivoCliente { // Asegúrate de que la clase sea pública
 private String nomA;
 private List<Cliente> clientes;

 public ArchivoCliente(String nomA) {
     this.nomA = nomA;
     this.clientes = new ArrayList<>();
 }

 public void crearArchivo() { /* Marcador de posición */ }

 // a) Implementar el diagrama de clases (incluyendo guardaCliente)
 public void guardaCliente(Cliente c) {
     if (buscarCliente(c.getId()) == null) { // Evita duplicados por ID
         this.clientes.add(c);
         System.out.println("Cliente guardado: " + c.getNombre() + " (ID: " + c.getId() + ")");
     } else {
         System.out.println("Cliente con ID " + c.getId() + " ya existe. No se guardó.");
     }
 }

 // b) Implementa buscarCliente(int c) a través del id.
 public Cliente buscarCliente(int idCliente) {
     for (Cliente cliente : this.clientes) {
         if (cliente.getId() == idCliente) {
             return cliente;
         }
     }
     return null;
 }

 // c) Implementa buscarCelularCliente(int c), que devuelva los datos del cliente junto al número de celular.
 public Cliente buscarCelularCliente(int idCliente) {
     Cliente cliente = buscarCliente(idCliente);
     if (cliente != null) {
         System.out.println("Datos del Cliente (ID: " + idCliente + "): " + cliente.getNombre() + ", Celular: " + cliente.getTelefono());
     } else {
         System.out.println("Cliente con ID " + idCliente + " no encontrado.");
     }
     return cliente;
 }

 // Método auxiliar para listar todos los clientes (para demostración)
 public void listarClientes() {
     if (clientes.isEmpty()) {
         System.out.println("\nNo hay clientes en el archivo.");
         return;
     }
     System.out.println("\n--- Clientes en " + nomA + " ---");
     for (Cliente cliente : clientes) {
         System.out.println(cliente);
     }
     System.out.println("--------------------------");
 }

 public static void main(String[] args) {
     ArchivoCliente miArchivoClientes = new ArchivoCliente("ClientesVIP");
     miArchivoClientes.crearArchivo();

     // a) Implementación de clases y guardaCliente
     Cliente cl1 = new Cliente(101, "Sofia Ramirez", 77712345);
     Cliente cl2 = new Cliente(102, "Diego Torres", 60123456);
     Cliente cl3 = new Cliente(103, "Laura Castro", 70098765);
     miArchivoClientes.guardaCliente(cl1);
     miArchivoClientes.guardaCliente(cl2);
     miArchivoClientes.guardaCliente(cl3);
     miArchivoClientes.guardaCliente(new Cliente(102, "Duplicado", 11111111)); // Intento de añadir duplicado

     miArchivoClientes.listarClientes();

     // b) Buscar cliente por ID
     System.out.println("\n--- Buscando cliente por ID ---");
     Cliente clienteEncontrado = miArchivoClientes.buscarCliente(102);
     if (clienteEncontrado != null) {
         System.out.println("Cliente encontrado por ID: " + clienteEncontrado);
     } else {
         System.out.println("Cliente con ID 102 no encontrado.");
     }

     clienteEncontrado = miArchivoClientes.buscarCliente(999); // Cliente no existente
     if (clienteEncontrado != null) {
         System.out.println("Cliente encontrado por ID: " + clienteEncontrado);
     } else {
         System.out.println("Cliente con ID 999 no encontrado.");
     }

     // c) Buscar celular de cliente por ID
     System.out.println("\n--- Buscando celular de cliente por ID ---");
     miArchivoClientes.buscarCelularCliente(101);
     miArchivoClientes.buscarCelularCliente(555); // Cliente no existente
 }
}