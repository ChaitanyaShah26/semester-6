public class BankSystemAssertion {

    static int processTransaction(int balance, int withdrawAmount) {
        balance = balance - withdrawAmount;

        assert balance >= 0 : "Balance became negative due to logic error";

        return balance;
    }

    public static void main(String[] args) {
        int balance = 1000;
        int withdrawAmount = 1500;

        balance = processTransaction(balance, withdrawAmount);

        System.out.println("Transaction completed. Balance: " + balance);
    }
}