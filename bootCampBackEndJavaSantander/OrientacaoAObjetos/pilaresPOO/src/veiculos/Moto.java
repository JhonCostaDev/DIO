package veiculos;

public class Moto extends Veiculo{
    public void ligar() {
        verificarCambio();
        verificarCombustivel();
        System.out.println("Veículo Ligado!");
    }
}
