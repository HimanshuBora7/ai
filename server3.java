import java.io.*;
import java.net.*;

public class server3 {
    public static void main(String[] args) {
        try {

            ServerSocket ss = new ServerSocket(6789);
            System.out.println("Server is listing on " + ss.getLocalPort());

            while (true) {
                Socket clientsocket = ss.accept();
                DataOutputStream dos = new DataOutputStream(clientsocket.getOutputStream());
                DataInputStream dis = new DataInputStream(clientsocket.getInputStream());

                System.out.println("Client connected " + clientsocket.getInetAddress());
                int num1 = dis.readInt();
                System.out.println("recived number " + num1);
                num1 *= 10;
                dos.writeInt(num1);
            }
        } catch (Exception e) {
        }

    }
}
