import java.sql.*;
import java.util.Scanner;

import static Sections.Sections.*;
import static StudentRegistration.StudentRegistration.*;
import static StudentLogin.StudentLogin.*;
import static TeacherLogin.TeacherLogin.*;

public class JDBCPractice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/jdbc-summer-23", "root", "root");
            Statement statement = connection.createStatement();

            Scanner scanner = new Scanner(System.in);
            boolean running = true;

            while (running) {
                System.out.println("1. Register");
                System.out.println("2. Student Login");
                System.out.println("3. Teacher Login");
                System.out.println("4. Exit");
                System.out.print("Choose an option: ");
                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume newline character

                switch (choice) {
                    case 1 -> studentRegistration(scanner, connection);
                    case 2 -> studentLogin(scanner, connection);
                    case 3 -> teacherLogin(scanner, connection);
                    case 4 -> {
                        running = false;
                        System.out.println("Exiting...");
                    }
                    default -> System.out.println("Invalid choice. Please choose again.");
                }
            }

            statement.close();
            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
//        try {
//            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/jdbc-summer-23", "root", "root");
//            Statement statement = con.createStatement();
//            printDatabase(con, statement);
//            System.out.println("1........................");
//            System.out.println("Please enter id");
//            int id = sc.nextInt();
//            sc.nextLine();
//            System.out.println("Please enter name");
//            String name = sc.nextLine();
//            System.out.println("Please enter department");
//            String dept = sc.nextLine();
//            String query = "Insert into students (id, name, dept) values(?, ?, ?)";
//            PreparedStatement preparedStatement = con.prepareStatement(query);
//            preparedStatement.setInt(1, id);
//            preparedStatement.setString(2, name);
//            preparedStatement.setString(3, dept);
//            preparedStatement.executeUpdate();
//            System.out.println("2........................");
//            printDatabase(con, statement);
//            con.close();
//        }
//        catch (Exception e) {
//            System.err.println(e);
//        }
//
//    }
//
//    public static void printDatabase(Connection con, Statement statement) throws Exception {
//        ResultSet resultSet = statement.executeQuery("select * from students");
//        while(resultSet.next()) {
//            System.out.print(resultSet.getInt("id")+" ");
//            System.out.print(resultSet.getString("name")+" ");
//            System.out.print(resultSet.getString("dept")+ " ");
//            System.out.println();
//        }
//    }

}
