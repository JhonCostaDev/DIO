public class Operadores {
    public static void main(String[] args) throws Exception {
        int number = 10;
        
        System.out.println(number);

        //number = - number;

        // Incremento

        number ++;
        System.out.println(number);
        //pre-incremento
        System.out.println(++ number);
        //pos-incremento
        System.out.println(number ++);

        // Decremento
         number --;
         System.out.println(number);


         //Negar expressões booleanas

         boolean verdade = true;
         System.out.println( verdade);
         System.out.println(!verdade);

         //Ternario

         int a, b;

         a = 5;
         b = 6;

         String result = "";
         /*if (a == b)
            result = "Verdadeiro";
        else
            result = "Falso";

        System.out.println(result);
        */
        result = a==b ? "Verdadeiro" : "Falso";
        System.out.println(result);

        //Relacionais
        System.out.println("===========================");

        int number1 = 122;
        int number2 = 132;
        String letter1 = "A";
        String letter2 = "a";

        boolean greatThan = number1 > number2;
        boolean equal = number1 == number2;
        boolean different = number1 != number2;
        boolean lessThan = number1 < number2;
        boolean greatThanOrEqual = number1 >= number2;
        boolean lessThanOrEqual = number1 <= number2;

        boolean sameLetter = letter1 == letter2;

        System.out.println(greatThan);
        System.out.println(greatThanOrEqual);
        System.out.println(equal);
        System.out.println(different);
        System.out.println(lessThan);
        System.out.println(lessThanOrEqual);
        System.out.println(sameLetter);

        System.out.println("===========================");
        System.out.println("==========Operadores Lógicos========");

        boolean condicao1 = true;
        boolean condicao2 = false; 

        if (condicao1 && !condicao2) {
            System.out.println("Verdadeiro");
        } else {
            System.out.println("Falso");
        }

        if (condicao1 || condicao2) {
            System.out.println("Verdadeiro");
        } else {
            System.out.println("Falso");
        }
    }
}
