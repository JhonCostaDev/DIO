package br.edu.jhon.SelecaoCandidatos;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class SelecaoCandidatos {
    public static void main(String[] args) {
        String[] candidatos = {"FELIPE", "MARCIA", "JULIA", "PAULO", "AUGUSTO", "MONICA", "FABRICIO",
                "MIRELA", "DANIELA", "JORGE"};
        double[] salarioPretendido = {1800.0, 2200.0, 1900.0, 2000.0, 2500.0, 1960.0, 2500.0,
                3000.0, 1980.0, 2000.0};
    /*
        System.out.printf("""
                Candidato   |   Salário
                %s          |   %.2f
                """, candidatos[0], salarioPretendido[0]);
    */
        selecao(candidatos, salarioPretendido);

    }

    public static void selecao(String[] candidato, double[] salario ) {
        double salarioBase = 2000.0;
        int maxCandidatos = 5;

        for (int i = 0; i < salario.length; i++) {
            if (salarioBase > salario[i]) {
                System.out.printf("Salario menor: %s\n", candidato[i]);
                maxCandidatos --;
            } else if (salarioBase == salario[i]){
                System.out.printf("Salario Igual: %s\n", candidato[i]);
                maxCandidatos --;
            } else {
                System.out.printf("Salario Maior: %s\n", candidato[i]);
            }
        }

        System.out.println(maxCandidatos);
    }
}