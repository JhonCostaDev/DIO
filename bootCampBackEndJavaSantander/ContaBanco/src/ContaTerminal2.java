import java.util.Scanner;

public class ContaTerminal2 {
    
    public static void main(String[] args) {
        Conta novaConta = new Conta();
        Scanner input = new Scanner(System.in);
        
        String menu;
        
        
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
            System.out.println("Digite seu nome:"); 
            novaConta.setNome(input.next());

            System.out.println("Digite o numero da agência");
            novaConta.setNumeroDaAgencia(input.next());

            System.out.println("Digite o número da conta: ");
            novaConta.setNumeroDaConta( input.nextInt());

            System.out.println("Digite o valor do depósito inicial: ");
            novaConta.setSaldo(input.nextDouble());

            System.out.println("Conta criada com sucesso!");

            exibirDadosConta(novaConta.getNome(), novaConta.getNumeroDaAgencia(), novaConta.getNumeroDaConta(), novaConta.getSaldo());
        }
            
    }

    public static void exibirDadosConta(String nome, String agencia, int numeroDaConta, double saldo) {
        System.out.printf("""
                #################################################
                Olá %s, obrigado por por criar uma conta no Java Bank!
                Sua Agência é %s,
                Sua Conta de número: %d
                E seu saldo inicial de: R$ %.2f já está disponível para saque.
                #################################################
                """, nome, agencia, numeroDaConta, saldo);
    }
}


