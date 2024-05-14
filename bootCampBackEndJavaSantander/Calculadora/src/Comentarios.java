public class Comentarios {
    public static void main(String[] args) {
        // <- comentário de uma linha

        /* <- comentário de mais de uma linha
         * 
         */
    }
    /**
     * Estas duas entrelinhas acima é para identificar que você pretende elaborar um comentário a nível de documentação.
     */
    public void metodo() {
        // desenvolver código aqui!
    }

    //Exemplo de código mal declarado

    public int somaMultiplica (int n, int x, String m){
        int r = 0; // r é igual ao resultado

        if(m == "M") { // M é igual a multiplicação
            
            r = n * x;
        } else {// se não soma mesmo
            r = n + x;
        }
        return r;
    }
}
