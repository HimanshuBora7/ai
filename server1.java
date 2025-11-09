import java.io.*;
import java.net.*;
import java.util.Scanner;

/**
 * A simple client that connects to the FactorialServer on localhost:6789.
 * It prompts the user for a number, sends it to the server,
 * reads the factorial result (as a long), and prints it.
 */
public class server1 {

    public static void main(String[] args) {
        // Use try-with-resources to auto-close the Scanner
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter a non-negative number to find its factorial: ");
            int number = scanner.nextInt();

            if (number < 0) {
                System.out.println("Factorial is not defined for negative numbers.");
                return;
            }

            // Connect to the server on localhost, port 6789
            // Use try-with-resources to auto-close the socket and streams
            try (Socket socket = new Socket("localhost", 6789);
                    DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
                    DataInputStream dis = new DataInputStream(socket.getInputStream())) {

                System.out.println("Connected to server...");

                // 1. Send the number to the server
                dos.writeInt(number);
                System.out.println("Sent number: " + number);

                // 2. Receive the factorial result (long) from the server
                long result = dis.readLong();
                System.out.println("Received result...");

                // 3. Print the result
                System.out.println("Factorial of " + number + " is: " + result);

            } catch (UnknownHostException e) {
                System.err.println("Host unknown: localhost");
            } catch (IOException e) {
                System.err.println("Could not connect to server (is it running?): " + e.getMessage());
            }
        } catch (Exception e) {
            System.err.println("Invalid input. Please enter an integer.");
        }
    }
}
