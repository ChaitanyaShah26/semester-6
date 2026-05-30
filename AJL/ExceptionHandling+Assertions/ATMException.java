public class ATMException {
    public static void main(String[] args) {
        int balance = 5000;
        int withdraw = 7000;

        try {
            if (withdraw > balance) {
                throw new Exception("Insufficient Balance");
            }
            balance -= withdraw;
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}