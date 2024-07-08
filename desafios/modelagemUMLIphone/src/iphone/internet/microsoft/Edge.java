package iphone.internet.microsoft;

import iphone.internet.NavegadorInternet;

public class Edge implements NavegadorInternet {

    @Override
    public void exibirPagina(String url) {
        System.out.println(" Edge Conectando à Página: " + url);
    }

    @Override
    public void adicionarNovaAba() {
        System.out.println("Edge Adicionando Nova Aba ...");
    }

    @Override
    public void atualizarPagina() {
        System.out.println("Edge Atualizando à Página...");
    }
}
