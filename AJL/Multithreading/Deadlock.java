class PaymentGateway {}
class Database {}

public class Deadlock {

    static PaymentGateway pg = new PaymentGateway();
    static Database db = new Database();

    public static void main(String[] args) {

        Thread t1 = new Thread(() -> {
            synchronized (pg) {
                System.out.println("Thread1: Locked Payment Gateway");

                try { Thread.sleep(100); } catch(Exception e) {}

                synchronized (db) {
                    System.out.println("Thread1: Locked Database");
                }
            }
        });

        Thread t2 = new Thread(() -> {
            synchronized (db) {
                System.out.println("Thread2: Locked Database");

                try { Thread.sleep(100); } catch(Exception e) {}

                synchronized (pg) {
                    System.out.println("Thread2: Locked Payment Gateway");
                }
            }
        });

        t1.start();
        t2.start();
    }
}