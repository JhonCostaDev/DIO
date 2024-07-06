package edu.jhonfalcon.poo;

import edu.jhonfalcon.poo.servicosmensagens.facebook.FacebookMenssenger;
import edu.jhonfalcon.poo.servicosmensagens.msn.MSNMenssenger;
import edu.jhonfalcon.poo.servicosmensagens.telegran.TelegranMenssenger;
import edu.jhonfalcon.poo.servicosmensagensabtract.facebook.FacebookMenssengerAbs;
import edu.jhonfalcon.poo.servicosmensagensabtract.msn.MSNMenssengerAbs;
import edu.jhonfalcon.poo.servicosmensagensabtract.telegran.TelegranMenssengerAbs;

public class ComputadorPedrinho {
    public static void main(String[] args) {

        System.out.println("-------------------MSN Menssenger----------------------");
        MSNMenssenger msn = new MSNMenssenger();

        //msn.validarContadoInternet(); ENCAPSULAMENTO
        msn.enviarMensagens();
        msn.recebendoMensagens();

        System.out.println("-------------------Facebook Menssenger----------------------");
        FacebookMenssenger faceB = new FacebookMenssenger();
        faceB.enviarMensagens();
        faceB.recebendoMensagens();
        
        System.out.println("---------------------Telegran Menssenger--------------------");
        TelegranMenssenger teleG = new TelegranMenssenger();
        teleG.enviarMensagens();
        teleG.recebendoMensagens();

        System.out.println("--------------------UTILIZANDO ABSTRAÇÃO--------------------");

        MSNMenssengerAbs msnAbs = new MSNMenssengerAbs();
        msnAbs.enviarMensagens();
        msnAbs.recebendoMensagens();

        System.out.println("-------------------Facebook Menssenger----------------------");
        FacebookMenssengerAbs faceBAbs = new FacebookMenssengerAbs();
        faceBAbs.enviarMensagens();
        faceBAbs.recebendoMensagens();

        System.out.println("---------------------Telegran Menssenger--------------------");
        TelegranMenssengerAbs teleGAbs = new TelegranMenssengerAbs();
        teleGAbs.enviarMensagens();
        teleGAbs.recebendoMensagens();

    }
}
