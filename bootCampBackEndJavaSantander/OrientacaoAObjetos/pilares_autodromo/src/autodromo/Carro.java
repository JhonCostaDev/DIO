package autodromo;

public class Carro extends Veiculo{


    public void ligar() {
        conferirCambio();               //Método que não precisa ser visto ENCAPSULAMENTO
        conferirCombustivel();          //Método que não precisa ser visto ENCAPSULAMENTO
        System.out.println("Carro ligado");
    }

    private void conferirCombustivel(){ //
        System.out.println("Conferindo Combustível...");
    }

    private void conferirCambio(){
        System.out.println("Conferindo Câmbio...");
    }
}
