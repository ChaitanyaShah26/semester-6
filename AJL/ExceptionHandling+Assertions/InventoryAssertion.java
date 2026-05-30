public class InventoryAssertion {
    public static void main(String[] args) {
        int stock = -5;

        assert stock >= 0 : "Stock cannot be negative";
        
        System.out.println("Stock is valid");
    }
}