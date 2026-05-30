public class OrderSystemAssertion {

    static void processOrder(int quantity, int pricePerItem) {

        int totalPrice = quantity * pricePerItem;
        assert quantity > 0 : "Invalid order quantity";
        assert totalPrice >= 0 : "Invalid price calculation";

        System.out.println("Order processed. Total price: " + totalPrice);
    }

    public static void main(String[] args) {
        processOrder(0, 500);
    }
}