public class ExemploForArrays {
    public static void main(String[] args) {
        String alunos[] = {"Maria", "José", "Bernando", "Gisele", "Janderly"};

        //for para iterar elementos do array

        for(int i = 0; i < alunos.length; i++){
            System.out.println("O aluno no índice " + i + " é: " + alunos[i]);
        }
        System.out.println("&777777&&&&&&&&");
        // Exemplo for each

        String frutas[] = {"Goiaba", "Banana", "Maçã", "Pera", "Aceroala"};

        for(String fruta : frutas) {
            System.out.println(fruta);
        }
    }
}
