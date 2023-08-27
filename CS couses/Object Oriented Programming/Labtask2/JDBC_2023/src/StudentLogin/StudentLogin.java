package StudentLogin;

import java.sql.*;
import java.util.Scanner;

import static Sections.Sections.Sections;

public class StudentLogin {
    public static void studentLogin(Scanner scanner, Connection connection) throws SQLException {
        System.out.print("Enter email: ");
        String email = scanner.nextLine();

        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery("SELECT * FROM users WHERE email = '" + email + "'");
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
                System.out.println("1. View Sections");
                System.out.println("2. Select Section");
                System.out.println("3. Exit");
                System.out.print("Choose an option: ");
                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume newline character

                switch (choice) {
                    case 1 -> {
                        resultSet = statement.executeQuery("select * from sections");
                         while(resultSet.next()) {
                                System.out.print(resultSet.getString("name")+" ");
                                System.out.print(resultSet.getString("time")+" ");
                                System.out.print(resultSet.getInt("seats")+ " ");
                                System.out.println();
                            }
                    }
                    case 2 -> {
                        int sections_id=0;
                        resultSet = statement.executeQuery("SELECT sections_id FROM users WHERE email = '" + email + "'");
                        resultSet.next();
                            if (resultSet.getInt("sections_id") == sections_id) {
                                sections_id = scanner.nextInt();
                                scanner.nextLine();
                                resultSet = statement.executeQuery("select seats from sections WHERE id = " + sections_id + " ");
                                while (resultSet.next()) {
                                    if (1 <= sections_id && sections_id <= 10 && resultSet.getInt("seats") != 0) {
                                        String insertStudentInfoQuery = "UPDATE users SET sections_id = ? WHERE email = " + email + " ";
                                        PreparedStatement insertStudentInfoStatement = connection.prepareStatement(insertStudentInfoQuery);
                                        insertStudentInfoStatement.setInt(1, sections_id);
                                        insertStudentInfoStatement.executeUpdate();
                                        String sectionSeatReduction = "UPDATE sections SET seats = seats-? WHERE id = " + sections_id + " ";
                                        PreparedStatement seatInfo = connection.prepareStatement(sectionSeatReduction);
                                        seatInfo.setInt(1, 1);
                                        seatInfo.executeUpdate();
                                    }
                                    else {
                                        System.out.println("Section not available");

                                    }
                                }
                            }
                            
                            else {
                                System.out.println("You've been already enrolled in a section");
                            }



                    }
                    case 3 -> {
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
