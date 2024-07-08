package iphone.internet.google;

import iphone.internet.NavegadorInternet;

public class Chrome implements NavegadorInternet {
    public void exibirPagina(String url){
        System.out.println(" Chrome Conectando à Página: " + url);
    }

    public void adicionarNovaAba() {
        System.out.println("Chrome Adicionando Nova Aba ...");
    }

    public void atualizarPagina(){
        System.out.println("Chrome Atualizando à Página...");
    }
}
