class MyThread extends Thread {
    public void run() {
        System.out.println("Java Thread Running");
    }
}

public class ThreadUsingClass {
    public static void main(String[] args) {
        new MyThread().start();
    }
}