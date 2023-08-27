import java.sql.*;
import java.util.Scanner;

public class RegistrationSystemWithDatabase {
    public static void main(String[] args) {
        try {
            Class.forName("org.sqlite.JDBC");
            Connection connection = DriverManager.getConnection("jdbc:sqlite:user.db");
            Statement statement = connection.createStatement();
            statement.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)");

            Scanner scanner = new Scanner(System.in);
            boolean running = true;

            while (running) {
                System.out.println("1. Register");
                System.out.println("2. Login");
                System.out.println("3. Exit");
                System.out.print("Choose an option: ");
                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume newline character

                switch (choice) {
                    case 1:
                        registerUser(scanner, connection);
                        break;
                    case 2:
                        loginUser(scanner, connection);
                        break;
                    case 3:
                        running = false;
                        System.out.println("Exiting...");
                        break;
                    default:
                        System.out.println("Invalid choice. Please choose again.");
                }
            }

            statement.close();
            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void registerUser(Scanner scanner, Connection connection) throws SQLException {
        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery("SELECT * FROM users WHERE username = '" + username + "'");
        if (resultSet.next()) {
            System.out.println("Username already exists.");
            statement.close();
            return;
        }

        System.out.print("Enter password: ");
        String password = scanner.nextLine();
        statement.executeUpdate("INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')");
        System.out.println("Registration successful.");
        statement.close();
    }

    private static void loginUser(Scanner scanner, Connection connection) throws SQLException {
        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery("SELECT * FROM users WHERE username = '" + username + "'");
        if (!resultSet.next()) {
            System.out.println("Username not found.");
            statement.close();
            return;
        }

        System.out.print("Enter password: ");
        String password = scanner.nextLine();
        if (resultSet.getString("password").equals(password)) {
            System.out.println("Login successful.");
        } else {
            System.out.println("Incorrect password.");
        }
        statement.close();
    }
}
