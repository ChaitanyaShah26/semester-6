import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.util.Scanner;

public class SimpleCipher {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter input text: ");
        String data = sc.nextLine();
        String keyString = "1234567887654321"; 

        SecretKeySpec key = new SecretKeySpec(keyString.getBytes(), "AES");

        // Encryption
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encrypted = cipher.doFinal(data.getBytes());
        String encryptedText = Base64.getEncoder().encodeToString(encrypted);
        System.out.println("Encrypted: " + encryptedText);

        // Decryption
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decrypted = cipher.doFinal(Base64.getDecoder().decode(encryptedText));
        System.out.println("Decrypted: " + new String(decrypted));
    }
}