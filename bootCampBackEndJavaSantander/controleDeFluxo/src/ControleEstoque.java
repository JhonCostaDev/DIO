public class ControleEstoque {
    public static void main(String[] args) {
        int estoque = 100;

        if (estoque > 80) {
            System.out.println("Quantidade de produtos suficiente");
        } else if(estoque < 80 && estoque > 50) {
            System.out.println("Avaliar a possibilidade de novo pedido");
        } else {
            System.out.println("Realizar novo pedido");
        }

    }
}
