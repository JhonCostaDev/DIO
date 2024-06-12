import java.util.Scanner;
//import Account;

public class AccountTeste {
	public static void main(String[] args) {
	
	Scanner input = new Scanner(System.in);

	Account conta= new Account();

	System.out.println("Digite seu nome: ");
	String nomeUsuario = input.nextLine();

	conta.setName(nomeUsuario);


	System.out.println(conta.getName());

	}
}