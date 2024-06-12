import java.util.Scanner;

public class CalculoSalario {
    public static void main(String[] args) {
        //Instância da classe Scanner para receber as entradas.
        Scanner input = new Scanner(System.in);
        //Mensagem incial
        System.out.println("Programa para cálculo de salário");
        
        //Receber os valores do usuário
        System.out.println("Digite o valor em Reais (R$) do Salário Bruto");
        double salario = input.nextDouble();
        System.out.println("Digite o valor em Reais (R$) do Benefício.");
        double beneficio = input.nextDouble();
        
        // Salario líquido recebe o método calculo de imposto mais o benefício
        double salarioLiquido = calculoImposto(salario) + beneficio;

        //Exibe o salário final.
        System.out.printf("Salario + Beneficio: R$%.2f\n", salarioLiquido);
    }

        //Método para calcular o imposto
    public static double calculoImposto(double salario) {
        
        double impostoFaixa1 = salario * 0.05;
        double impostoFaixa2 = salario * 0.1;
        double impostoFaixa3 = salario * 0.15;
        
        if(salario >= 0 && salario <= 1100.0) {
            return salario - impostoFaixa1;
        } else if(salario <= 2500.0) {
            return salario - impostoFaixa2;
        } else {
            return salario - impostoFaixa3;
        }
    }
}