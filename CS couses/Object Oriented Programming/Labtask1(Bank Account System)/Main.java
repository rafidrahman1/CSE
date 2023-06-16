import java.util.ArrayList;
import java.util.List;

public class Main {
    private static List<BankAccount> accounts = new ArrayList<>();

    public static void createAccountCheck(int accountNumber, String accountHolderName) {
        BankAccount account = new CheckingAccount(accountNumber, accountHolderName, 20);
        accounts.add(account);
        System.out.println("Checking account created: " + accountNumber);
    }

    public static void createAccountSave(int accountNumber, String accountHolderName) {
        BankAccount account = new SavingsAccount(accountNumber, accountHolderName, 2.5);
        accounts.add(account);
        System.out.println("Savings account created: " + accountNumber);
    }

    public static void main(String[] args) {

         createAccountSave(123459, "Haha");
         accounts.get(0).deposit(10);
         accounts.get(0).withdraw(20);
         accounts.get(0).displayAccountInfo();
         System.out.println();
        
         createAccountCheck(339980, "Rafid Rahman");
         accounts.get(1).deposit(20);
         accounts.get(1).withdraw(10);
         accounts.get(1).displayAccountInfo();
         System.out.println();

         createAccountCheck(223344, "Rahman");
         accounts.get(2).deposit(30);
         accounts.get(2).withdraw(51);
         accounts.get(2).displayAccountInfo();
         System.out.println();

        accounts.remove(0);
        accounts.get(1).getBalance();
        

        


    }
}
