import java.util.Scanner;

public class SelecaoCandidatos {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double salarioBase = 2000.0;

        System.out.println("Digite a pretenção salarial do candidato:");

        double salarioPretendido = input.nextDouble();

        if(salarioBase > salarioPretendido) {
            System.out.println("LIGAR PARA O CANDIDADO");
        } else if(salarioBase == salarioPretendido) {
            System.out.println("LIGAR PARA O CANDIDATO COM CONTRA PROPOSTA");
        } else {
            System.out.println("AGUARDANDO RESULTADO DOS DEMAIS CANDIDATOS");
        }

    }
}
