class NewThread extends Thread {
    public void run() {
        System.out.println(Thread.currentThread().getName());
    }
}

public class MultiThread {
    public static void main(String[] args) {
        NewThread t1 = new NewThread();
        NewThread t2 = new NewThread();

        t1.start();
        t2.start();
    }
}