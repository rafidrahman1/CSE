public abstract class BankAccount {
    private int accountNumber;
    private String accountName;
    double balance;

    public BankAccount(int accountNumber, String accountName) {
        this.accountNumber = accountNumber;
        this.accountName = accountName;
        this.balance = 0.0;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public String getAccountName() {
        return accountName;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount);
    }

    public abstract void withdraw(double amount);

    public void displayAccountInfo() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Account Name: " + accountName);
        System.out.println("Balance: " + balance);
    }
}