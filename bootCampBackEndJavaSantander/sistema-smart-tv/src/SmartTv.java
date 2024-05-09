public class SmartTv {
    boolean on = false;
    int channel = 1;
    int volume = 25;

    // métodos que manipulam o estado
    public void ligar() {
        on = true;
    }

    public void desligar() {
        on = false;
    }

    public void volUp() {
        volume ++;
    }

    public void volDown() {
        volume --;
    }

    public void channelUp() {
        channel ++;
    }

    public void channelDown() {
        channel --;
    }

    public void manualChannel(int typeuser) {
        channel = typeuser;
    }

}
