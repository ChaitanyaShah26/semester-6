public class ServerCrashError {
    static void process() {
        process(); // infinite call
    }

    public static void main(String[] args) {
        process();
    }
}