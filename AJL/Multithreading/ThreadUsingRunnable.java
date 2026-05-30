class A extends Thread {
    public void run() {
        System.out.println("Thread class method");
    }
}

class B implements Runnable {
    public void run() {
        System.out.println("Runnable method");
    }
}

public class ThreadUsingRunnable {
    public static void main(String[] args) {
        A t1 = new A();
        t1.start();

        Thread t2 = new Thread(new B());
        t2.start();
    }
}