import java.util.*;

class NoDriverAvailableException extends Exception {
    public NoDriverAvailableException(String message) {
        super(message);
    }
}

class InvalidLocationException extends Exception {
    public InvalidLocationException(String message) {
        super(message);
    }
}

public class RideBookingSystem {

    static void bookRide(String location, int availableDrivers)
            throws NoDriverAvailableException, InvalidLocationException {

        if (location == null || location.isEmpty()) {
            throw new InvalidLocationException("Invalid pickup location");
        }

        if (availableDrivers == 0) {
            throw new NoDriverAvailableException("No drivers available nearby");
        }

        System.out.println("Ride booked successfully at " + location);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter location: ");
        String location = sc.nextLine();    
        System.out.println("Enter no. of drivers: ");
        int drivers = sc.nextInt();         

        try {
            System.out.println("Requesting ride...");
            bookRide(location, drivers);
        }

        catch (InvalidLocationException e) {
            System.out.println("Location Error: " + e.getMessage());
        }

        catch (NoDriverAvailableException e) {
            System.out.println("Booking Error: " + e.getMessage());
        }

        catch (Exception e) {
            System.out.println("Unexpected Error: " + e.getMessage());
        }

        finally {
            System.out.println("Closing ride request session...");
        }
    }
}