package edu.jhonfalcon.poo.servicosmensagensabtract.telegran;

import edu.jhonfalcon.poo.servicosmensagensabtract.ServicosMensagensAbstract;

public class TelegranMenssengerAbs extends ServicosMensagensAbstract {
    public void enviarMensagens() {
        validarContadoInternet();
        System.out.println("Enviando Mensagem pelo Telegran Messenger ...");
    }

    public void recebendoMensagens() {
        System.out.println("Recebendo Mensagem pelo Telegran Messenger ...");
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
