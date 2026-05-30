class LoginSystem {
    static void validate(String password) throws Exception {
        if (password.length() < 6) {
            throw new Exception("Weak Password");
        }
    }

    public static void main(String[] args) {
        try {
            validate("123");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}