package iphone.telefone;

public class Phone implements AparelhoTelefonico{
    @Override
    public void ligar() {
        System.out.println("Phone Ligando ...");
    }

    @Override
    public void atender() {
        System.out.println("Phone Atendendo ...");
    }

    @Override
    public void iniciarCorreioVoz() {
        System.out.println("Phone Iniciando Correio de Voz ...");
    }
}
