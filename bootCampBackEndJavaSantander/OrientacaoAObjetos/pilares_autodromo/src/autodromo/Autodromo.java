package autodromo;

public class Autodromo {
    public static void main(String[] args) {
        Carro fusca = new Carro();
        fusca.setChassi("S23984-98B");
        fusca.ligar();

        Moto cg150 = new Moto();
        cg150.setChassi("YBt2698-90C"); //Atributo que não existe na classe Moto, mas que foi herdado da classe Veiculo.
        cg150.ligar();

    }
}
