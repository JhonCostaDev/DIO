import java.util.Scanner;

public class ContaBancaria {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);

        String menu = """
               ==============================
               ======== BANCO JAVA ==========
               ==============================

                         BEM VINDO
               ESCOLHA UMA DAS OPÇÕES ABAIXO:
                    1 - DEPOSITO
                    2 - SAQUE
                    3 - EXIBIR SALDO
                    0 - SAIR
               """;
        
        System.out.println(menu);
        int opcao = input.nextInt(); 
        do {
            int a = movimentacao(opcao);
        }while(a == 0);
        
    }

    public static int movimentacao(int opcao) {
        Scanner input = new Scanner(System.in);
        double saldo = 0;


        switch (opcao) {
            case 1:
                System.out.println("Digite o valor em Reais R$ a ser depositado: ");
                saldo += input.nextDouble();
                System.out.printf("Saldo atual: R$%.1f\n", saldo);
                break;
            case 2:
            System.out.println("Digite o valor em Reais R$ a ser sacado: ");
            double saque = input.nextDouble();

            if(saque > saldo){
                System.out.println("Saldo insuficiente");
            } else {
                saldo -= saque;
                System.out.println("Transação autorizada");
                System.out.printf("Valor solicitado: R$%.2f\n", saque);
                System.out.println("Saldo Atual");
            }
            System.out.printf("Saldo atual: R$%.1f\n", saldo);
                break;
            case 3:
            System.out.printf("Saldo Atual: R$%.2f\n", saldo);
                break;
            case 0:
                
                break;
        
            default:
            System.out.println("Opção Inválida, tente novamente");
                break;
        }
       
    }
}
