import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Random;

public class MaxMinScheduler {

    private static class VM implements Comparable<VM> {
        int id;
        int load;

        public VM(int id, int load) {
            this.id = id;
            this.load = load;
        }

        @Override
        public int compareTo(VM other) {
            return Integer.compare(other.load, this.load);
        }

        @Override
        public String toString() {
            return "VM" + id + " (Load: " + load + ")";
        }
    }

    private static class Server {
        int id;
        int currentLoad;
        List<Integer> assignedVmIds;

        public Server(int id) {
            this.id = id;
            this.currentLoad = 0;
            this.assignedVmIds = new ArrayList<>();
        }

        public void assignVM(int vmId, int vmLoad) {
            this.assignedVmIds.add(vmId);
            this.currentLoad += vmLoad;
        }

        @Override
        public String toString() {
            return "Server " + id + " (Total Load: " + currentLoad + ") -> VMs: " + assignedVmIds;
        }
    }

    public void schedule(List<VM> vmList, int numServers) {

        Collections.sort(vmList);

        PriorityQueue<Server> serverQueue = new PriorityQueue<>(
                (a, b) -> Integer.compare(a.currentLoad, b.currentLoad));

        Map<Integer, Server> serverMap = new HashMap<>();

        for (int i = 0; i < numServers; i++) {
            Server server = new Server(i);
            serverQueue.add(server);
            serverMap.put(i, server);
        }

        System.out.println("\n--- Scheduling Process ---");
        for (VM vm : vmList) {
            Server minLoadServer = serverQueue.poll();

            minLoadServer.assignVM(vm.id, vm.load);
            System.out.println("Assigning " + vm + " to Server " + minLoadServer.id);

            serverQueue.add(minLoadServer);
        }

        System.out.println("\n--- Final VM Mappings ---");
        for (int i = 0; i < numServers; i++) {
            System.out.println(serverMap.get(i));
        }
    }

    public static void main(String[] args) {
        int numServers = 4;
        int numVMs = 7;

        if (numServers <= 2 || numServers > 5) {
            System.out.println("Error: Number of servers must be > 2 and <= 5.");
            return;
        }
        if (numVMs <= 2) {
            System.out.println("Error: Number of VMs must be > 2.");
            return;
        }
        if (numVMs <= numServers) {
            System.out.println("Error: Number of VMs must be greater than the number of servers for this test.");
            return;
        }

        List<VM> vmList = new ArrayList<>();
        Random rand = new Random();
        for (int i = 0; i < numVMs; i++) {
            int load = 100 + rand.nextInt(900);
            vmList.add(new VM(i, load));
        }

        System.out.println("--- Max-Min Scheduler Initial State ---");
        System.out.println("Number of Servers: " + numServers);
        System.out.println("Number of VMs: " + numVMs);
        System.out.println("VMs to Schedule (Unsorted):");
        for (VM vm : vmList) {
            System.out.println("  " + vm);
        }

        MaxMinScheduler scheduler = new MaxMinScheduler();
        scheduler.schedule(vmList, numServers);
    }
}