package iphone.musica;

public class Spotify implements ReprodutorMusical{
    @Override
    public void tocar() {
        System.out.println("Spotify Tocando Musica...");
    }

    @Override
    public void Pausar() {
        System.out.println("Spotify Pausando Musica");
    }

    @Override
    public void selecionarMusica(String musica) {
        System.out.println("Spotify Musica Selecionada: " + musica);
    }
}
