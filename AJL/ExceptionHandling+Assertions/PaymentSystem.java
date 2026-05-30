public class PaymentSystem {
    static void processPayment(int amount) throws Exception {
        if (amount <= 0) {
            throw new Exception("Invalid payment amount");
        }
        System.out.println("Payment Successful");
    }

    public static void main(String[] args) {
        try {
            processPayment(-500);
        } catch (Exception e) {
            System.out.println("Payment Failed: " + e.getMessage());
        } finally {
            System.out.println("Transaction Attempt Completed");
        }
    }
}