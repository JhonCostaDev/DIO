package edu.jhonfalcon.poo.servicosmensagensabtract.msn;

import edu.jhonfalcon.poo.servicosmensagensabtract.ServicosMensagensAbstract;

public class MSNMenssengerAbs extends ServicosMensagensAbstract {

    @Override
    public void enviarMensagem() {

    }

    @Override
    public void receberMensagem() {

    }

    public void enviarMensagens() {
        validarContadoInternet();
        System.out.println("Enviando Mensagem pelo MSN Messenger ...");
    }


    public void recebendoMensagens() {
        System.out.println("Recebendo Mensagem pelo MSN Messenger ...");
        salvarHistoricaoMensagem();
    }


    private void validarContadoInternet() {
        System.out.println("Validando se está conectado...");
    }

    private void salvarHistoricaoMensagem() {
        System.out.println("Salvando o histórico de mensagens...");
    }



}
