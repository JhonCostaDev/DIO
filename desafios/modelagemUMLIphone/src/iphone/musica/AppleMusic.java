package iphone.musica;

public class AppleMusic implements ReprodutorMusical{
    @Override
    public void tocar() {
        System.out.println("Apple Music Tocando Musica");
    }

    @Override
    public void Pausar() {
        System.out.println("Apple Music Pausando Musica");
    }

    @Override
    public void selecionarMusica(String musica) {
        System.out.println("Apple Music Musica Selecionada: " + musica);
    }
}
