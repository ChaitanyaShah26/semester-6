class LowBalanceException extends Exception {
    LowBalanceException(String msg) {
        super(msg);
    }
}

public class BankingException {
    public static void main(String[] args) {
        int balance = 500;

        try {
            if (balance < 1000) {
                throw new LowBalanceException("Minimum balance required");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}