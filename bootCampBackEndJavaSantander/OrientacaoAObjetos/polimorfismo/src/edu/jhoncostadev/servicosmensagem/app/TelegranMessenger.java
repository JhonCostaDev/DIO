package edu.jhoncostadev.servicosmensagem.app;

public class TelegranMessenger extends ServicoMensagem{

    @Override
    public void enviarMensagem() {
        validarConexaoInterner();
        System.out.println("Enviando Mensagem pelo Telegran Messenger ...");
    }

    @Override
    public void receberMensagem() {
        System.out.println("Recebendo Mensagem pelo Telegran Messenger ...");
    }
}
