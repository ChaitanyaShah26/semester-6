import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.util.Base64;

public class AESKeyGen {
    public static void main(String[] args) throws Exception {

        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey key = keyGen.generateKey();

        String encodedKey = Base64.getEncoder().encodeToString(key.getEncoded());
        System.out.println("AES Key: " + encodedKey);
    }
}