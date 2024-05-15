import java.util.Locale;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in).useLocale(Locale.US);// .Locale.Us manterá a convenção americada de uso de caracteres.
        System.out.println("Type your name: ");
        String name = input.nextLine();
        
        System.out.println("Type your last name: ");
		String lastName = input.nextLine();

        System.out.println("Type your age: ");
		int age = input.nextInt();

        System.out.println("Type your height: ");
		double height = input.nextDouble(); 

		System.out.println("Hello, My name is " + name + " " + lastName);
		System.out.println("My age is " + age + " years old.");
		System.out.println("My height is " + height);
    }
}
