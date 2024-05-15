public class AboutMe {
    public static void main(String[] args) {
		String name = args [0];
		String lastName = args [1];
		int age = Integer.valueOf(args[2]);
		double height = Double.valueOf(args[3]); // double.valueOf is used because the args are get in form of Strings

		System.out.println("Hello, My name is " + name + " " + lastName);
		System.out.println("My age is " + age + " years old.");
		System.out.println("My height is " + height);
	}
}
