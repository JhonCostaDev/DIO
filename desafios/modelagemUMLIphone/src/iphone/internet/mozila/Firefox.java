package iphone.internet.mozila;

import iphone.internet.NavegadorInternet;

public class Firefox implements NavegadorInternet {

    @Override
    public void exibirPagina(String url) {
        System.out.println(" Firefox Conectando à Página: " + url);
    }

    @Override
    public void adicionarNovaAba() {
        System.out.println("Firefox Adicionando Nova Aba ...");
    }

    @Override
    public void atualizarPagina() {
        System.out.println("Firefox Atualizando à Página...");
    }
}
