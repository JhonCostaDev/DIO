public class WhileDoWhile {
    public static void main(String[] args) {
        //While: Testa a condição antes de executar o código
        /*João recebeu 50 reais de mesada para gastar com doces, enquanto o valor de 50 reais não for atingindo, ele continuará a colocar itens em sua cesta de compras.
         * 
         */

        // double valorDoce = 5.75;
        // double carteiraJoao = 50;

        // int cesta = 0;

        // while(cesta * valorDoce <= carteiraJoao) {
        //     cesta++;//incremento para quebra do laço.
        // }

        // System.out.println("Quantidade de doces:  " + cesta + " unidades");

        // System.out.println("************************************************");

        //do-while

        
        int mentira = 0;
        do {
            System.out.println("É mentira");
            mentira ++;
        } while(mentira < 5);

        System.out.println("Agora é verdade");

    }
}
