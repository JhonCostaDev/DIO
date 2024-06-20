using System;

public class CalculoSalario {
    public static void Main() {
         //Receber os valores do usuário
        float salarioBruto = float.Parse(Console.ReadLine());
        float beneficio = float.Parse(Console.ReadLine());

        float valorImposto = 0;

        if(salarioBruto >= 0 && salarioBruto <= 1100) {
            valorImposto = 0.05F * salarioBruto;
        } else if(salarioBruto >= 1100 && salarioBruto <= 2500) {
            valorImposto = 0.1F * salarioBruto;
        } else {
            valorImposto = 0.15F * salarioBruto;
        }
        // Calcula e imprime

        float saida = salarioBruto - valorImposto + beneficio;
        Console.WriteLine(saida.ToString("0.00"));

    }
}