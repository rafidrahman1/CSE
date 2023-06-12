import java.util.ArrayList;
import java.util.List;

public class Main {
    private static List<BankAccount> accounts = new ArrayList<>();

    public static void createAccount(int accountNumber, String accountHolderName) {
        BankAccount account = new SavingsAccount(accountNumber, accountHolderName, 2.5);
        accounts.add(account);
        System.out.println("Savings account created: " + accountNumber);
    }

    public static void main(String[] args) {
        createAccount(123456, "John Doe");
        accounts.get(0).deposit(1000.0);
        accounts.get(0).withdraw(500.0);
        accounts.get(0).displayAccountInfo();
        System.out.println();

        BankAccount account = new CheckingAccount(987654, "Jane Smith", 1000.0);
        accounts.add(account);
        System.out.println("Checking account created: " + account.getAccountNumber());
        account.deposit(2000.0);
        account.withdraw(3000.0);
        account.displayAccountInfo();
    }
}
