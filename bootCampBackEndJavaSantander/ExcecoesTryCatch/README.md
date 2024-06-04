# Estruturas excepcionais - Try / Catch

Ao executar o código java, diferentes erros podem ocorrer:
* erros de códificação feitors pelo progrador;
* erros devido a entrada de dados
* entre outros imprevistos.

Quando ocorre um erro, o java geralmente para e gera uma mensagem de erro. O termo técnico para essa ação é: **Java lançará um erro (Jogará um erro)**.
De forma interpretativa em java, um erro é algo irreparável, a aplicação trava ou é encerrada drasticamente. Já a exceção é um fluxo inesperado da aplicação.
Exemplos:
* querer dividir por zero;
* Querer abrir um arquivo que não existe;
* Tentar abrir uma conexão com banco de dados com usuário e senha incorretos.
Todos esses cenários e os demais que possam ocorrer não são erros, mais fluxos não previstos pela aplicação.
Essa é mais uma responsabilidade do desenvolvedor, prever situações semelhantes a estas e realizar o que é denominado de: **Tratamento de Exceções**.

## Mão na massa!
Código sem tratamento de exceção!
```java
import java.util.Scanner;
import java.util.Locale;

public class AboutMe {
    public static void main(String[] args) {
        
            Scanner input = new Scanner(System.in).useLocale(Locale.US);
            System.out.println("Digite seu nome: ");
            String nome = input.nextLine();

            System.out.println("Digite seu sobre nome: ");
            String sobreNome = input.nextLine();

            System.out.println("Digite sua idade: ");
            int idade = input.nextInt();

            System.out.println("Digite sua altura: ");
            double altura = input.nextDouble();

            System.out.printf("""
                    Seja Bem-Vindo:
                    %s %s
                    Idade: %d
                    Altura: %f
                    """, nome, sobreNome, idade, altura
            );
    }
}

```



## exceções que podem acontecer

* Não informar o nome e sobre nome;
* O valor idade ter um caractere NÃO numérico;
* O valor da altura ter uma vírgula ao invês de ser um ponto(Padrão Americano).

## Conhecendo algumas exceções já mapeadas
A linguagem java dispõe de uma vasta lista de classes que representam exceções:

| Nome | Causa |
|----|-----|
|**java.lang.NullPointerException**|Quando tentamos obter alguma informação de uma variável nula.
|**java.lang.ArithmeticException**|Quando tentamos dividir um valor por zero.|
|**java.sql.SQLException**| Quando existe algum erro relacionado a interação com banco de dados.|
|**java.io.FileNotFoundException**| Quand tentamos ler ou escrever em um arquivo que não existe.|

## Tratamento de exceções

E quando inevitavelmente ocorre uma exceção? Como nós desenvolvedores odemos ajustar o nosso algoritmo par amenizar o ocorrido?

### Try
A instrução **try** permite que você defina um bloco de código para ser testado quando a erros enquanto está sendo executado.

### Catch
A instrução **catch** permite definir um bloco de código a ser executado caso ocorra um erro no bloco **try**.

### Finally
A instrução **finally** permite definir um bloco de código a ser executado independente de ocorrer um erro ou não.

As palavras **try/catch** vêm em pares:
Estrutura de um blovo try e catch:

1. try {
2.	// bloco de código conforme esperado
3.}
4. catch(Exception e) {// precisamos saber qual exceção
//bloco de código que captura as exceções que podem acontecer.
//em caso de um fluxo não previsto.
}


Código com tratamento de excecão!!
```java
import java.util.Scanner;
import java.util.InputMismatchException;
import java.util.Locale;
public class AboutMe {
    public static void main(String[] args) {
        try {
            Scanner input = new Scanner(System.in).useLocale(Locale.US);
            System.out.println("Digite seu nome: ");
            String nome = input.nextLine();

            System.out.println("Digite seu sobre nome: ");
            String sobreNome = input.nextLine();

            System.out.println("Digite sua idade: ");
            int idade = input.nextInt();

            System.out.println("Digite sua altura: ");
            double altura = input.nextDouble();

            System.out.printf("""
                    Seja Bem-Vindo:
                    %s %s
                    Idade: %d
                    Altura: %f
                    """, nome, sobreNome, idade, altura
            );
        }
        catch (InputMismatchException e) {
            System.out.println("O Campo idade deve ser numérico");
            System.out.println("O Campo altura deve ser escrito com (.) ponto na sua  parte decimal");
        }
    }
}

```