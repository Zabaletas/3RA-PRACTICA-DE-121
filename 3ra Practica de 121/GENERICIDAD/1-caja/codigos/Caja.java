public class Caja<T> {
    private T contenido;

    public void guardar(T nuevoContenido) {
        this.contenido = nuevoContenido;
    }

    public T obtener() {
        return this.contenido;
    }

    public static void main(String[] args) {
        Caja<String> cajaString = new Caja<>();
        cajaString.guardar("Hola Mundo");

        Caja<Integer> cajaInt = new Caja<>();
        cajaInt.guardar(42);

        System.out.println("Caja String: " + cajaString.obtener());
        System.out.println("Caja Int: " + cajaInt.obtener());
    }
}