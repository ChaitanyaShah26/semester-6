class FoodApp {
    static void order() {
        System.out.println("Order Placed");
        try { Thread.sleep(2000); } catch(Exception e) {}
    }

    static void payment() {
        System.out.println("Payment Done");
        try { Thread.sleep(2000); } catch(Exception e) {}
    }

    static void delivery() {
        System.out.println("Delivery Started");
        try { Thread.sleep(2000); } catch(Exception e) {}
    }

    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        order();
        payment();
        delivery();

        long end = System.currentTimeMillis();
        System.out.println("Total Time: " + (end - start));
    }
}