package escola;

import java.util.Scanner;

public class Escola {
    public static void main(String[] args) {
        Aluno felipe = new Aluno();
        /*felipe.setNome("Felipe");
        felipe.setIdade(32);
        felipe.setEndereco("Avenida das consolações 500");
        */
        String [] aluno01 = listaAlunos();

        felipe.setNome(aluno01[0]);
        felipe.setIdade(aluno01[1]);
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
