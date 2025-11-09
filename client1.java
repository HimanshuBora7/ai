import java.io.*;
import java.net.*;

/**
 * A simple server that listens on port 6789.
 * It reads an integer from a client, computes its factorial,
 * and sends the result (as a long) back.
 */
public class client1 {

    public static void main(String[] args) {
        // Use try-with-resources to auto-close the ServerSocket
        try (ServerSocket serverSocket = new ServerSocket(6789)) {
            System.out.println("Factorial Server listening on port 6789...");

            while (true) {
                // Wait for a client to connect (this blocks)
                // Use try-with-resources to auto-close the client socket and streams
                try (Socket clientSocket = serverSocket.accept();
                        DataInputStream dis = new DataInputStream(clientSocket.getInputStream());
                        DataOutputStream dos = new DataOutputStream(clientSocket.getOutputStream())) {

                    System.out.println("Client connected: " + clientSocket.getInetAddress());

                    // 1. Read the number from the client
                    int number = dis.readInt();
                    System.out.println("Received number: " + number);

                    // 2. Compute the factorial
                    long result = computeFactorial(number);
                    System.out.println("Computed factorial: " + result);

                    // 3. Send the result (long) back to the client
                    dos.writeLong(result);
                    System.out.println("Sent result to client.");

                } catch (IOException e) {
                    System.err.println("Error handling client connection: " + e.getMessage());
                }
                // The client socket is closed here, and the loop waits for a new client
            }
        } catch (IOException e) {
            System.err.println("Server could not start on port 6789: " + e.getMessage());
        }
    }

    /**
     * Computes the factorial of a number.
     * Uses 'long' to handle larger results (up to 20!).
     * Returns -1 for negative input as factorial is undefined.
     */
    private static long computeFactorial(int n) {
        if (n < 0) {
            return -1; // Factorial is not defined for negative numbers
        }
        if (n == 0 || n == 1) {
            return 1;
        }

        long fact = 1;
        for (int i = 2; i <= n; i++) {
            fact = fact * i;
        }
        return fact;
    }
}