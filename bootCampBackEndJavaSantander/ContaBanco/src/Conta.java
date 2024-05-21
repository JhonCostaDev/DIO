import java.util.Scanner;

public class Conta {
    String name, agency;
    int accountNumber;
    double balance;

    public void setName(String name) {
        this.name = name;
    }
    
    public void setAgency(String agency) {
        this.agency = agency;
    }

    public void setAccountNumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    //################# GET #######################
    
    public String getName() {
        return name;
    }
    
    public String getAgency() {
        return agency;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public double getBalance() {
        return balance;
    }
}
