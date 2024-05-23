import java.util.Scanner;

public class Conta {
    String nome, numeroDaAgencia;
    int numeroDaConta;
    double saldo;

    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public void setNumeroDaAgencia(String numeroDaAgencia) {
        this.numeroDaAgencia = numeroDaAgencia;
    }

    public void setNumeroDaConta(int numeroDaConta) {
        this.numeroDaConta = numeroDaConta;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    //################# GET #######################
    
    public String getNome() {
        return nome;
    }
    
    public String getNumeroDaAgencia() {
        return numeroDaAgencia;
    }

    public int getNumeroDaConta() {
        return numeroDaConta;
    }

    public double getSaldo() {
        return saldo;
    }
}
