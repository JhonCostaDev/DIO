package usuario;

import iphone.Iphone;
import iphone.internet.NavegadorInternet;
import iphone.internet.google.Chrome;
import iphone.internet.microsoft.Edge;
import iphone.internet.mozila.Firefox;
import iphone.musica.AppleMusic;
import iphone.musica.ReprodutorMusical;
import iphone.musica.Spotify;

public class IphoneUsuario {
    public static void main(String[] args) {
        System.out.println("-----------------------------");
        //acessarInternet("chrome", "https://wikipedia.com");
        System.out.println("-----------------------------");

        //ouvirMusica("spotify", "sweet of mine");
        //System.out.println("-----------------------------");


        Iphone ph = new Iphone();
        ph.selecionarMusica("November Rain");

    }
    
    public static void acessarInternet(String navagador, String url) {
        NavegadorInternet nav = null;

        if (navagador.equals("chrome")) {
            nav = new Chrome();
        } else if (navagador.equals("firefox")) {
            nav = new Firefox();
        } else if (navagador.equals("edge")) {
            nav = new Edge();
        }

        nav.exibirPagina(url);
        nav.adicionarNovaAba();
        nav.atualizarPagina();
    }

    public static void ouvirMusica(String app, String musica){
        ReprodutorMusical musicPlayer = null;

        if(app.equals("appleM")) {
            musicPlayer = new AppleMusic();
        }else if(app.equals("spotify")) {
            musicPlayer = new Spotify();
        }

        musicPlayer.selecionarMusica(musica);
        musicPlayer.Pausar();
        musicPlayer.tocar();

    }
}

