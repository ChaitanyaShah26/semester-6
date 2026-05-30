class Order extends Thread {
    public void run() {
        System.out.println("Order Placed");
        try { Thread.sleep(2000); } catch(Exception e) {}
    }
}

class Payment extends Thread {
    public void run() {
        System.out.println("Payment Done");
        try { Thread.sleep(2000); } catch(Exception e) {}
    }
}

class Delivery extends Thread {
    public void run() {
        System.out.println("Delivery Started");
        try { Thread.sleep(2000); } catch(Exception e) {}
    }
}

public class FoodAppMultithreading {
    public static void main(String[] args) throws Exception {
        long start = System.currentTimeMillis();

        Order t1 = new Order();
        Payment t2 = new Payment();
        Delivery t3 = new Delivery();

        t1.start();
        t2.start();
        t3.start();

        t1.join();
        t2.join();
        t3.join();

        long end = System.currentTimeMillis();
        System.out.println("Total Time: " + (end - start));
    }
}