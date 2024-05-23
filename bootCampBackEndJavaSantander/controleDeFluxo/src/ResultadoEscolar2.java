public class ResultadoEscolar2 {
    public static void main(String[] args) {
        double nota = 5;
        /* Condicional aninhada

        */
        if(nota < 5) {
            System.out.println("reprovado");

        } else if(nota >= 5 && nota < 7) {
            System.out.println("Recuperação");
        } else {
            System.out.println("Aprovado");
        }
    }
}
