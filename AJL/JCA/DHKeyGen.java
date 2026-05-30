import java.security.*;
import java.util.Base64;

public class DHKeyGen {
    public static void main(String[] args) throws Exception {

        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("DH");
        keyGen.initialize(512);

        KeyPair pair = keyGen.generateKeyPair();

        String publicKey = Base64.getEncoder().encodeToString(pair.getPublic().getEncoded());

        String privateKey = Base64.getEncoder().encodeToString(pair.getPrivate().getEncoded());

        System.out.println("DH Public Key: " + publicKey);
        System.out.println("DH Private Key: " + privateKey);
    }
}