package edu.jhoncostadev.servicosmensagem.app;

public class MSNMessenger extends ServicoMensagem{
    @Override
    public void enviarMensagem() {
        validarConexaoInterner();
        System.out.println("Enviando Mensagem pelo MSN Messenger ...");
    }

    @Override
    public void receberMensagem() {
        System.out.println("Recebendo Mensagem pelo MSN Messenger ...");
    }
}
