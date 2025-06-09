package cliente;

//Cliente.java
public class Cliente { // Asegúrate de que la clase sea pública
 private int id;
 private String nombre;
 private int telefono;

 public Cliente(int id, String nombre, int telefono) {
     this.id = id;
     this.nombre = nombre;
     this.telefono = telefono;
 }

 public int getId() { return id; }
 public String getNombre() { return nombre; }
 public int getTelefono() { return telefono; }

 @Override
 public String toString() {
     return "Cliente [id=" + id + ", nombre=" + nombre + ", telefono=" + telefono + "]";
 }
}