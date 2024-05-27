public class ContadorDeDogs {
    public static void main(String[] args) {
        int cachorros = 0;
        
        for(int entrou = 1; entrou <= 10; entrou++){ 
            if(entrou == 1){
                System.out.printf("Entrou: %d cachorro\n", entrou);
                cachorros ++;
            }else {
                System.out.printf("Entraram: %d cachorros\n", entrou);
                cachorros ++;
            }
        }

        System.out.printf("Entraram ao todo %d cachorros!", cachorros);
    }
}
