import java.security.SecureRandom;

public class SecureRandomDemo {
    public static void main(String[] args) {

        SecureRandom random = new SecureRandom();
        byte[] bytes = new byte[16];
        random.nextBytes(bytes);

        System.out.print("Random Bytes: ");
        for (byte b : bytes) {
            System.out.printf("%02x", b);
        }
    }
}