import java.security.MessageDigest;
import java.util.Scanner;

public class SimpleHash {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter input text: ");
        String input = sc.nextLine();

        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hash = md.digest(input.getBytes());

        System.out.print("Hash: ");
        for (byte b : hash) {
            System.out.printf("%02x", b);
        }
    }
}