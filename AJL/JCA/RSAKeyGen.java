import java.security.*;
import java.util.Base64;

public class RSAKeyGen {
    public static void main(String[] args) throws Exception {

        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
        keyGen.initialize(512);

        KeyPair pair = keyGen.generateKeyPair();

        String publicKey = Base64.getEncoder().encodeToString(pair.getPublic().getEncoded());

        String privateKey = Base64.getEncoder().encodeToString(pair.getPrivate().getEncoded());

        System.out.println("RSA Public Key: " + publicKey);
        System.out.println("RSA Private Key: " + privateKey);
    }
}