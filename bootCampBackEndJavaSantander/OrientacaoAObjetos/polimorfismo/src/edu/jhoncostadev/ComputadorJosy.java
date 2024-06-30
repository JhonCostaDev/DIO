package edu.jhoncostadev;

import edu.jhoncostadev.servicosmensagem.app.ServicoMensagem;
import edu.jhoncostadev.servicosmensagem.app.MSNMessenger;
import edu.jhoncostadev.servicosmensagem.app.FacebookMessenger;
import edu.jhoncostadev.servicosmensagem.app.TelegranMessenger;

public class ComputadorJosy {
    public static void main(String[] args) {
        ServicoMensagem servicoMensagem = null;
        /*
        * Não se sabe qual app
        * mas qualquer um deverá enviar e receber mensagens
        * */

        String escolheApp = "fbm";

        if (escolheApp == "msn") {
            servicoMensagem = new MSNMessenger();
        } else if(escolheApp.equals("fbm")) {
            servicoMensagem = new FacebookMessenger();
        } else if (escolheApp.equals("tlg")) {
            servicoMensagem = new TelegranMessenger();
        }
        servicoMensagem.enviarMensagem();
        servicoMensagem.receberMensagem();
    }
}
