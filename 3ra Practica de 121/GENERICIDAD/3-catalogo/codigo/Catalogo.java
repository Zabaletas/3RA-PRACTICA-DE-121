import java.util.ArrayList;
import java.util.List;

public class Catalogo<T> {
    private List<T> elementos;

    public Catalogo() {
        this.elementos = new ArrayList<>();
    }

    public void agregar(T elemento) {
        elementos.add(elemento);
    }

    public T buscar(int indice) {
        if (indice >= 0 && indice < elementos.size()) {
            return elementos.get(indice);
        }
        throw new IndexOutOfBoundsException("Índice fuera de rango");
    }

    public static void main(String[] args) {
        Catalogo<String> catalogoLibros = new Catalogo<>();
        catalogoLibros.agregar("Cien años de soledad");
        catalogoLibros.agregar("1984");
        System.out.println("Libro en posición 0: " + catalogoLibros.buscar(0));

        Catalogo<Integer> catalogoProductos = new Catalogo<>();
        catalogoProductos.agregar(100);
        catalogoProductos.agregar(200);
        System.out.println("Producto en posición 1: " + catalogoProductos.buscar(1));
    }
}