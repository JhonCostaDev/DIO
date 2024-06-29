package veiculos;

public class Autodromo {
    public static void main(String[] args) {
        Carro fusca = new Carro();
        fusca.setNome("Fusca");
        fusca.setMarca("VolksWagen");
        fusca.setModelo("beatle");
        fusca.setAnoFabricacao("1975");
        fusca.setAnoModelo("1976");
        fusca.imprimirInformacoes();
        fusca.ligar();

        Moto titan = new Moto();
        titan.setNome("Titan");
        titan.setMarca("Honda");
        titan.setModelo("150");
        titan.setAnoFabricacao("2021");
        titan.setAnoModelo("2022");
        titan.imprimirInformacoes();
        titan.ligar();

    }
}
