public class Metodos {

    public static void main(String[] args) {
        String firstName = "Jonathan";
        String lastName =  "Costa";

        String fullName = fullName(firstName, lastName); //Chamada do método.
        System.out.println(fullName);
    }
    //Isso é um método 
    public static String fullName (String firstName, String lastName){
        //return firstName.concat(" " + lastName);
        //return firstName + " " + lastName;
        //return firstName.concat(" ").concat(lastName);
        return "Nome Completo: " + firstName.concat(" ").concat(lastName);
    }
}