// Checked Exception (File handling)
import java.io.*;

public class CheckedException {
    public static void main(String[] args) {
        try {
            FileReader fr = new FileReader("data.txt");
        } catch (Exception e) {
            System.out.println("File not found");
        }
    }
}