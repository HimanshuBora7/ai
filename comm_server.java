import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * A very simple server program that waits for a client to connect,
 * receives one message, and sends one reply.
 */
public class comm_server {

    public static void main(String[] args) {
        // The server listens on this port
        int port = 6666;

        System.out.println("Server: Waiting for a client to connect on port " + port + "...");

        // Use try-with-resources to automatically close the sockets
        try (
                // 1. Create a server socket
                ServerSocket serverSocket = new ServerSocket(port);

                // 2. Wait for a client connection (this blocks)
                Socket clientSocket = serverSocket.accept();

                // 3. Get streams to communicate with the client
                DataInputStream dis = new DataInputStream(clientSocket.getInputStream());
                DataOutputStream dos = new DataOutputStream(clientSocket.getOutputStream())) {

            System.out.println("Server: Client connected!");

            // 4. Read the message from the client
            String messageFromClient = dis.readUTF();
            System.out.println("Server: Received from client: '" + messageFromClient + "'");

            // 5. Send a reply back to the client
            dos.writeUTF("Hello Client, I received your message!");
            dos.flush();
            System.out.println("Server: Sent reply to client.");

        } catch (Exception e) {
            System.out.println("Server exception: " + e.getMessage());
            e.printStackTrace();
        }

        System.out.println("Server: Shutting down.");
    }
}
