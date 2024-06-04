import java.util.Scanner;
import java.util.InputMismatchException;
import java.util.Locale;

public class AboutMe {
    public static void main(String[] args) {
        try {
            Scanner input = new Scanner(System.in).useLocale(Locale.US);
            System.out.println("Digite seu nome: ");
            String nome = input.nextLine();

            System.out.println("Digite seu sobre nome: ");
            String sobreNome = input.nextLine();

            System.out.println("Digite sua idade: ");
            int idade = input.nextInt();

            System.out.println("Digite sua altura: ");
            double altura = input.nextDouble();

            System.out.println("########RESULTADO##########");
            System.out.printf("""
                    Seja Bem-Vindo:
                    %s %s
                    Idade: %d
                    Altura: %f
                    """, nome, sobreNome, idade, altura
            );
        }
        catch (InputMismatchException e) {
            System.err.println("O Campo idade deve ser numérico");
            System.err.println("O Campo altura deve ser escrito com (.) ponto na sua  parte decimal");
        }
    }
}
