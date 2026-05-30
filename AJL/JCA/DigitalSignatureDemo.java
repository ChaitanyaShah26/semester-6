import java.security.*;
import java.util.Scanner;

public class DigitalSignatureDemo {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
        keyGen.initialize(1024);
        KeyPair pair = keyGen.generateKeyPair();

        System.out.print("Enter input message: ");
        String message = sc.nextLine();

        Signature sign = Signature.getInstance("SHA256withRSA");
        sign.initSign(pair.getPrivate());
        sign.update(message.getBytes());
        byte[] signature = sign.sign();

        System.out.println("Signature created");

        sign.initVerify(pair.getPublic());
        sign.update(message.getBytes());
        boolean verified = sign.verify(signature);

        System.out.println("Verified: " + verified);
    }
}