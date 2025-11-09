import java.io.*;
import java.net.*;
import java.util.Scanner;

public class client3 {
    public static void main(String[] args) {
        try {
            System.out.println("enter a non negative number to find the factorial ");
            Scanner sc = new Scanner(System.in);
            int num = sc.nextInt();
            Socket socket = new Socket("localhost", 6789);
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
            DataInputStream dis = new DataInputStream(socket.getInputStream());
            System.out.println("Connected to the server ");

            dos.writeInt(num);
            System.out.println("Sent number " + num);
            int num1 = dis.readInt();
            System.out.println("Received number " + num1);

        } catch (Exception e) {
        }
    }
}
