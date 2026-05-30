import javax.crypto.Mac;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.util.Scanner;
import java.util.Base64;

public class MACDemo {

    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter message: ");
        String message = sc.nextLine();

        KeyGenerator keyGen = KeyGenerator.getInstance("HmacSHA256");
        SecretKey key = keyGen.generateKey();

        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(key);
        byte[] macResult = mac.doFinal(message.getBytes());

        System.out.println("Secret Key: " + Base64.getEncoder().encodeToString(key.getEncoded()));
        System.out.println("MAC Code  : " + Base64.getEncoder().encodeToString(macResult));

        Mac verifyMac = Mac.getInstance("HmacSHA256");
        verifyMac.init(key);
        byte[] verifyResult = verifyMac.doFinal(message.getBytes());

        if (java.util.Arrays.equals(macResult, verifyResult))
            System.out.println("Authentication: SUCCESS");
        else
            System.out.println("Authentication: FAILED");
    }
}