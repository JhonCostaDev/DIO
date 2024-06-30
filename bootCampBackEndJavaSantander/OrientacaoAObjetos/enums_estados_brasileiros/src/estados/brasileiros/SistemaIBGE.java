package estados.brasileiros;

public class SistemaIBGE {
    public static void main(String [] args) {
        for(EstadosBrasileiros est: EstadosBrasileiros.values()) {
            System.out.println(est.getSigla() + " -" + est.getNome());
        }

    }
}
