import java.net.*;

/**
 * A simple Java program to demonstrate the InetAddress class.
 * It displays the IP address and hostname for both the
 * local machine and a specified remote machine (e.g., "www.google.com").
 */
public class server2 {

    public static void main(String[] args) {
        try {
            // 1. Get and display local machine information
            InetAddress localMachine = InetAddress.getLocalHost();
            System.out.println("--- Local Machine ---");
            System.out.println("Hostname: " + localMachine.getHostName());
            System.out.println("IP Address: " + localMachine.getHostAddress());
            System.out.println(); // Add a blank line for readability

            // 2. Get and display remote machine information
            // We'll use "www.google.com" as an example remote host
            String remoteHostName = "www.google.com";
            InetAddress remoteMachine = InetAddress.getByName(remoteHostName);

            System.out.println("--- Remote Machine (" + remoteHostName + ") ---");
            System.out.println("Hostname: " + remoteMachine.getHostName());
            System.out.println("IP Address: " + remoteMachine.getHostAddress());

            // You can also get all IPs associated with a hostname
            System.out.println("\nAll IPs for " + remoteHostName + ":");
            InetAddress[] allIps = InetAddress.getAllByName(remoteHostName);
            for (InetAddress ip : allIps) {
                System.out.println("  -> " + ip.getHostAddress());
            }

        } catch (UnknownHostException e) {
            // This exception is thrown if the hostname (local or remote)
            // could not be resolved.
            System.err.println("Error: Could not resolve host.");
            System.err.println(e.getMessage());
        }
    }
}