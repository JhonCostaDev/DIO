public class BreakAndContinue {
    public static void main(String[] args) {
        //Break: interromper o laço de repetição
        for(int i = 0; i <= 10; i++) {
            if (i == 6) {
                //break; //com break ele para a contagem no laço da condição booleana
                continue; //com continue  ele pula  a contagem no laço da condição booleana
            }
            System.out.println(i);
        }

        // Continue: 
    }
}
