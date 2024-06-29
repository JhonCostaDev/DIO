package veiculos;

public class Carro extends Veiculo{


    public void ligar() {
        verificarCambio();
        verificarCombustivel();
        System.out.println("Carro Ligado!");
    }


}
