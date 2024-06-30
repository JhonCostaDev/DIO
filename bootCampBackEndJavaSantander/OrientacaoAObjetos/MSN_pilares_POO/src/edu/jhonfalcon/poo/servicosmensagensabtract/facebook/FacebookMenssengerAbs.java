package edu.jhonfalcon.poo.servicosmensagensabtract.facebook;

import edu.jhonfalcon.poo.servicosmensagensabtract.ServicosMensagensAbstract;

public class FacebookMenssengerAbs extends ServicosMensagensAbstract {
    public void enviarMensagens() {
        validarContadoInternet();
        System.out.println("Enviando Mensagem pelo Facebook Messenger ...");

    }

    public void recebendoMensagens() {
        System.out.println("Recebendo Mensagem pelo Facebook Messenger ...");
        salvarHistoricaoMensagem();
    }

    private void validarContadoInternet() {
        System.out.println("Validando se está conectado...");
    }

    private void salvarHistoricaoMensagem() {
        System.out.println("Salvando o histórico de mensagens...");
    }


    @Override
    public void enviarMensagem() {

    }

    @Override
    public void receberMensagem() {

    }
}
