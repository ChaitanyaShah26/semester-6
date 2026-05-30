class PaymentGateway {}
class Database {}

public class DeadlockPrevented {

    static PaymentGateway pg = new PaymentGateway();
    static Database db = new Database();

    public static void main(String[] args) {

        Runnable task = () -> {
            synchronized (pg) {
                System.out.println(Thread.currentThread().getName() + ": Locked Payment Gateway");

                try { Thread.sleep(100); } catch(Exception e) {}

                synchronized (db) {
                    System.out.println(Thread.currentThread().getName() + ": Locked Database");
                }
            }
        };

        Thread t1 = new Thread(task, "Thread1");
        Thread t2 = new Thread(task, "Thread2");

        t1.start();
        t2.start();
    }
}