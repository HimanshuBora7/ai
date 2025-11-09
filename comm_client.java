import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.Socket;

/**
 * A very simple client program that connects to the server,
 * sends one message, and waits for one reply.
 */
public class comm_client {

    public static void main(String[] args) {
        // Connect to the server on "localhost" (this machine) and port 6666
        String serverAddress = "127.0.0.1"; // "localhost"
        int port = 6666;

        System.out.println("Client: Connecting to " + serverAddress + " on port " + port + "...");

        // Use try-with-resources to automatically close the socket and streams
        try (
                // 1. Create a socket to connect to the server
                Socket socket = new Socket(serverAddress, port);

                // 2. Get streams to communicate with the server
                DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
                DataInputStream dis = new DataInputStream(socket.getInputStream())) {

            System.out.println("Client: Connected!");

            // 3. Send a message to the server
            System.out.println("Client: Sending message 'Hello Server!'...");
            dos.writeUTF("Hello Server!");
            dos.flush();

            // 4. Wait for and read the reply from the server
            String messageFromServer = dis.readUTF();
            System.out.println("Client: Received from server: '" + messageFromServer + "'");

        } catch (Exception e) {
            System.out.println("Client exception: " + e.getMessage());
            e.printStackTrace();
        }

        System.out.println("Client: Connection closed.");
    }
}