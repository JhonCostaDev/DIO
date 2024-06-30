package edu.jhonfalcon.poo.servicosmensagens;

public class ServicosMensagens {
    public void enviarMensagens() {
        validarContadoInternet();
        System.out.println("Enviando Mensagem  ...");
    }

    public void recebendoMensagens() {
        System.out.println("Recebendo Mensagem  ...");
        salvarHistoricaoMensagem();
    }

    private void validarContadoInternet() {
        System.out.println("Validando se está conectado...");
    }

    private void salvarHistoricaoMensagem() {
        System.out.println("Salvando o histórico de mensagens...");
    }

}
