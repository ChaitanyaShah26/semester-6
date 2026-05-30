public class BankAssertion {
    public static void main(String[] args) {
        int balance = 500;

        assert balance >= 0;
        
        System.out.println("Balance is valid");
    }
}