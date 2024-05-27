public class ExemploFor {
    public static void main(String[] args) throws Exception {
        
        for(int i = 0; i <= 10; i++){
            System.out.println(i + 1);
        }
        System.out.println("%%%%%%%%%%%%%%%%%%%%%%%%");
        //For para iterar Arrays
        
        String alunos[] = {"Pedro", "Julia", "Gabriela", "Matias", "Paula"};
        
        for(int i = 0; i < alunos.length; i++){
            System.out.printf("O aluno no indice %d é %s\n", i, alunos[i]);
        }
        System.out.println("%%%%%%%%%%%%%%%%%%%%%%%%");
        // FOR EACH - ITERAÇÃO BASEADA NOS ELEMENTOS DA COLEÇÃO
        
        for(String aluno:alunos) {
            System.out.println(aluno);
        }

    }
}
