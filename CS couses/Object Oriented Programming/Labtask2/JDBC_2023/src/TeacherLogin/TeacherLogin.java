package TeacherLogin;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

import static Sections.Sections.Sections;

public class TeacherLogin {
    public static void teacherLogin(Scanner scanner, Connection connection) throws SQLException {
        System.out.print("Enter email: ");
        String email = scanner.nextLine();

        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery("SELECT * FROM teacher WHERE email = '" + email + "'");
        if (!resultSet.next()) {
            System.out.println("Username not found.");
            statement.close();
            return;
        }

        System.out.print("Enter password: ");
        String password = scanner.nextLine();
        if (resultSet.getString("password").equals(password)) {
            System.out.println("Login successful.");
            boolean running = true;
            while (running) {
                System.out.println("1. Add Sections");
                System.out.println("2. View Sections");
                System.out.println("3. View Students in a Specific Section");
                System.out.println("4. Exit");
                System.out.print("Choose an option: ");
                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume newline character

                switch (choice) {
                    case 1 -> Sections(scanner, connection);
                    case 2 -> {
                        resultSet = statement.executeQuery("select * from sections");
                        while(resultSet.next()) {
                            System.out.print(resultSet.getString("name")+" ");
                            System.out.print(resultSet.getString("time")+" ");
                            System.out.print(resultSet.getInt("seats")+ " ");
                            System.out.println();
                        }
                    }
                    case 3 -> {
                        int sections_id = scanner.nextInt();
                        scanner.nextLine();
                        System.out.println("Name   &   ID");
                        resultSet = statement.executeQuery("select * from users WHERE sections_id = " + sections_id + " ");
                        while(resultSet.next()) {
                            System.out.print(resultSet.getString("name  ")+" ");
                            System.out.print(resultSet.getInt("  id")+" ");
                            System.out.println();
                        }
                    }
                    case 4 -> {
                        running = false;
                        System.out.println("Exiting...");
                    }
                    default -> System.out.println("Invalid choice. Please choose again.");
                }
            }
        } else {
            System.out.println("Incorrect password.");
        }
        statement.close();
    }
}
