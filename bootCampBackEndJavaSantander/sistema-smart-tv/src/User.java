
public class User {
    public static void main(String[] args)  throws Exception{
    SmartTv smartTv = new SmartTv();
        System.out.println("Tv Ligada: " + smartTv.on);
        System.out.println("Canal Primário: " + smartTv.channel);
        System.out.println("Volume atual: " + smartTv.volume);


        smartTv.ligar();
        System.out.println("Tv Ligada: " + smartTv.on);

        smartTv.desligar();
        System.out.println("Tv Ligada: " + smartTv.on);

        smartTv.volUp();
        smartTv.volUp();
        smartTv.volDown();
        System.out.println("Volume atual: " + smartTv.volume);

        smartTv.channelUp();
        smartTv.channelUp();
        smartTv.channelUp();
        smartTv.channelDown();
        System.out.println("Canal atual: " + smartTv.channel);

        smartTv.manualChannel(10);
        System.out.println("Canal atual: " + smartTv.channel);
    }
}