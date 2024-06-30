package edu.jhoncostadev.servicosmensagem.app;

public class FacebookMessenger extends ServicoMensagem{

    @Override
    public void enviarMensagem() {
        validarConexaoInterner();
        System.out.println("Enviando Mensagem pelo Facebook Messenger ...");
    }

    @Override
    public void receberMensagem() {
        System.out.println("Recebendo Mensagem pelo Facebook Messenger ...");
    }
}
