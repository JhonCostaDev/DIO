public class CaixaEletronico2 {
    public static void main(String[] args) throws Exception {
        double saldo = 150;
        double valorSolicitado = 75.5;
       /* Estrutura condicional simples
            A estrutura condicional simples verifica apenas uma condição e executa um bloco de código caso essa condição seja verdadeira. Mas, caso a condição seja falsa, o bloco de código é simplesmente ignorado. A sintaxe geralmente segue o formato:
        */

        if (valorSolicitado < saldo)
            saldo -= valorSolicitado;
            
            System.out.println(saldo);
    }
}

