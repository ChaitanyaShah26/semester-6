class TicketBooking {
    int seats = 1;

    void bookTicket(String user) {
        if (seats > 0) {
            System.out.println(user + " is booking ticket...");
            seats--;
            System.out.println(user + " successfully booked!");
        } else {
            System.out.println(user + " failed to book ticket");
        }
    }
}

public class ConcurrentExecution {
    public static void main(String[] args) {
        TicketBooking obj = new TicketBooking();

        Thread t1 = new Thread(() -> obj.bookTicket("User1"));
        Thread t2 = new Thread(() -> obj.bookTicket("User2"));

        t1.start();
        t2.start();
    }
}