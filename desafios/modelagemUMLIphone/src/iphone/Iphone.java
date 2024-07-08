package iphone;

import iphone.internet.NavegadorInternet;
import iphone.musica.ReprodutorMusical;
import iphone.telefone.AparelhoTelefonico;

public class Iphone implements NavegadorInternet, ReprodutorMusical, AparelhoTelefonico {
    @Override
    public void exibirPagina(String url) {
        System.out.println("Safari Conectando à Página: " + url);
    }

    @Override
    public void adicionarNovaAba() {
        System.out.println("Safari Adicionando Nova Aba ...");
    }

    @Override
    public void atualizarPagina() {
        System.out.println("Safari Atualizando à Página...");
    }

    @Override
    public void tocar() {
        System.out.println("Iphone Music Tocando Musica");
    }

    @Override
    public void Pausar() {
        System.out.println("Iphone Music Pausando Musica");
    }

    @Override
    public void selecionarMusica(String musica) {
        System.out.println("Iphone Music Musica Selecionada: " + musica);
    }

    @Override
    public void ligar() {
        System.out.println("IPhone Ligando ...");
    }

    @Override
    public void atender() {
        System.out.println("IPhone Atendendo ...");
    }

    @Override
    public void iniciarCorreioVoz() {
        System.out.println("IPhone Iniciando Correio de Voz ...");
    }
}
