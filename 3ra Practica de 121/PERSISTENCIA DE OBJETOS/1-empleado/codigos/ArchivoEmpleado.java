// ArchivoEmpleado.java
import java.util.ArrayList;
import java.util.List;

public class ArchivoEmpleado {
    private final String nomA; // Mark as final if not intended to change after creation
    private final List<Empleado> empleados; // Use final for collections if the reference doesn't change

    public ArchivoEmpleado(String nomA) {
        this.nomA = nomA;
        this.empleados = new ArrayList<>();
        // System.out.println("ArchivoEmpleado '" + nomA + "' creado."); // Removed for cleaner output
    }

    public void crearArchivo() { /* Placeholder for file creation logic */ }

    // a) Implementa el método guardarEmpleado(Empleado e) para almacenar empleados.
    public void guardarEmpleado(Empleado e) {
        this.empleados.add(e);
        System.out.println("Empleado guardado: " + e.getNombre());
    }

    // b) Implementa buscaEmpleado(String n) a traves del nombre, para ver los datos del Empleado n.
    public Empleado buscaEmpleado(String n) {
        for (Empleado empleado : this.empleados) {
            if (empleado.getNombre().equalsIgnoreCase(n)) {
                return empleado;
            }
        }
        return null;
    }

    // c) Implementa mayorSalario(float sueldo), que devuelva al primer empleado con sueldo mayor al ingresado.
    public Empleado mayorSalario(float sueldo) {
        for (Empleado empleado : this.empleados) {
            if (empleado.getSalario() > sueldo) {
                return empleado;
            }
        }
        return null;
    }

    // Helper method to list all employees for demonstration
    public void listarEmpleados() {
        if (empleados.isEmpty()) {
            System.out.println("\nNo hay empleados en el archivo.");
            return;
        }
        System.out.println("\n--- Empleados en " + nomA + " ---");
        for (Empleado empleado : empleados) {
            System.out.println(empleado);
        }
        System.out.println("--------------------------");
    }

    public static void main(String[] args) {
        ArchivoEmpleado miArchivo = new ArchivoEmpleado("EmpleadosDelMes");
        miArchivo.crearArchivo();

        // Create some employees
        Empleado emp1 = new Empleado("Juan Perez", 30, 50000.0f);
        Empleado emp2 = new Empleado("Maria Lopez", 25, 65000.0f);
        Empleado emp3 = new Empleado("Carlos Garcia", 35, 52000.0f);
        Empleado emp4 = new Empleado("Ana Rodriguez", 28, 70000.0f);

        // a) Guardar empleados
        miArchivo.guardarEmpleado(emp1);
        miArchivo.guardarEmpleado(emp2);
        miArchivo.guardarEmpleado(emp3);
        miArchivo.guardarEmpleado(emp4);

        miArchivo.listarEmpleados();

        // b) Buscar empleado
        System.out.println("\n--- Buscando empleado ---");
        String nombreBuscar = "Maria Lopez";
        Empleado encontrado = miArchivo.buscaEmpleado(nombreBuscar);
        if (encontrado != null) {
            System.out.println("Empleado encontrado: " + encontrado);
        } else {
            System.out.println("Empleado '" + nombreBuscar + "' no encontrado.");
        }

        nombreBuscar = "Pedro Gomez";
        encontrado = miArchivo.buscaEmpleado(nombreBuscar);
        if (encontrado != null) {
            System.out.println("Empleado encontrado: " + encontrado);
        } else {
            System.out.println("Empleado '" + nombreBuscar + "' no encontrado.");
        }

        // c) Mayor salario
        System.out.println("\n--- Buscando empleado con salario mayor ---");
        float sueldoLimite = 60000.0f;
        Empleado empleadoMayorSalario = miArchivo.mayorSalario(sueldoLimite);
        if (empleadoMayorSalario != null) {
            System.out.println("Primer empleado con salario mayor a " + sueldoLimite + ": " + empleadoMayorSalario);
        } else {
            System.out.println("No se encontró ningún empleado con salario mayor a " + sueldoLimite);
        }

        sueldoLimite = 80000.0f;
        empleadoMayorSalario = miArchivo.mayorSalario(sueldoLimite);
        if (empleadoMayorSalario != null) {
            System.out.println("Primer empleado con salario mayor a " + sueldoLimite + ": " + empleadoMayorSalario);
        } else {
            System.out.println("No se encontró ningún empleado con salario mayor a " + sueldoLimite);
        }
    }
}