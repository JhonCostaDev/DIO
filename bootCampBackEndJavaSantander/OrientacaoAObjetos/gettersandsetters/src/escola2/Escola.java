package escola2;

import java.util.Scanner;

public class Escola {
    public static void main(String[] args) {
        String [] aluno01 = listaAlunos();
        Aluno felipe = new Aluno(aluno01[0], aluno01[1]);
        
        felipe.setEndereco(aluno01[2]);


        System.out.println("-----------------------------------");
        System.out.printf("""
                Nome: %s
                Idade: %s
                Endereço: %s
                """, felipe.getNome(),felipe.getIdade(),felipe.getEndereco());
        System.out.println("-----------------------------------");
    }

    public static String [] listaAlunos() {
        Scanner input = new Scanner(System.in);
        

        System.out.println("Digite o nome do aluno");
        String nome = input.nextLine();

        System.out.println("Digite a idade do aluno");
        String idade = input.nextLine();

        System.out.println("Digite o endereço do aluno");
        String endereco = input.nextLine();
        
        String aluno[] = {nome, idade, endereco};
        input.close();
        return aluno;
    }
}
