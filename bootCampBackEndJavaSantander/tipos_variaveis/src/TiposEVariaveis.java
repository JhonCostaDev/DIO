public class TiposEVariaveis {
    public static void main(String[] args) throws Exception {
        //exemplo de declaração de variáveis.
        int idade; //
        int anoDeFabricacao = 2021;
        double salarioMinimo = 2.500;

        //Peculiaridade

        byte idade2 = 123;
        short ano = 2021;
        int cep = 21070333; // se começar com zero, talvez tenha que ser outro tipo.
        long cpf = 98765432109L;//se começar com zero, talvez tenha que ser outro tipo.
        float pi = 3.14F; // Tem q terminar com F no final.
        double salario = 1275.33;

        //Conportamento em converção de tipos

        short numeroCurto = 1;
        int numeroNormal = numeroCurto;
        //short numeroCurto2 = numeroNormal;
        short numeroCurto2 = (short)numeroNormal;

        //CONSTANTES

        final double VALOR_DE_PI = 3.145;



    }
}
