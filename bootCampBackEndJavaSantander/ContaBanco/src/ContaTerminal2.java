import java.util.Scanner;

public class ContaTerminal2 {
    
    public static void main(String[] args) {
        Conta novaConta = new Conta();
        Scanner input = new Scanner(System.in);
        
        String /*agencia, nomeDoCliente,*/ menu;
        /*int numeroDaConta;
        double saldo;*/
        

        menu = ("""
        ################################    
        ########## Java Banck ##########
        ################################
        |           Digite ...          |
        |   [1] - Criar Conta           |
        |   [2] - Consultar Saldo       |
        |   [3] - Deposito              |
        |   [4] - Saque                 |
        |   [0] - Finalizar Atendimento.|
        |                               |
        #################################
        """
        );
        System.out.println(menu);
        int opcaoInicial = input.nextInt();

        System.out.println(opcaoInicial);

        if (opcaoInicial == 1) {
            System.out.println("Digite o nome: ");
            novaConta.setName(input.nextLine());
            
            System.out.println("Digite a agência: ");
            novaConta.setAgency(input.nextLine());

            System.out.println("Digite o número da conta: ");
            novaConta.setAccountNumber(input.nextInt());

            System.out.println("Digite o Deposito inicial: ");
            novaConta.setBalance(input.nextDouble());
            
            exibirDadosConta(novaConta.getName(), novaConta.getAgency(), novaConta.getAccountNumber(), novaConta.getBalance());
        }
            
    }

    public static void exibirDadosConta(String nome, String agencia, int numeroDaConta, double saldo) {
        System.out.printf("""
                Olá %s, obrigado por por criar uma conta no Java Bank!
                Sua Agência é %s,
                Sua Conta de número: %d
                E seu saldo inicial de: %.2f já está disponível para saque.
                """, nome, agencia, numeroDaConta, saldo);
    }
}


