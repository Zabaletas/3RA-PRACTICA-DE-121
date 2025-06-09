// Empleado.java
public class Empleado {
    private final String nombre; // Mark as final if not intended to change after creation
    private final int edad;     // Mark as final
    private final float salario;  // Mark as final

    public Empleado(String nombre, int edad, float salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public float getSalario() {
        return salario;
    }

    @Override
    public String toString() {
        return "Empleado [nombre=" + nombre + ", edad=" + edad + ", salario=" + String.format("%.2f", salario) + "]";
    }
}