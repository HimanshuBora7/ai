
// A simple class with a shared method
class SharedResource {

    // A shared counter
    private int counter = 0;

    // A separate lock object
    private final Object lock = new Object();

    public void incrementCounter() {
        // Using a synchronized block ensures that only one thread
        // can access the critical section (the counter increment) at a time.
        synchronized (lock) {
            System.out.println(Thread.currentThread().getName() + " is incrementing...");
            counter++;
            System.out.println(Thread.currentThread().getName() + " new counter value: " + counter);

            // Adding a small sleep to make the race condition more likely
            // if synchronization were not used.
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public int getCounter() {
        return counter;
    }
}

// A runnable task that accesses the shared resource
class WorkerThread implements Runnable {
    private SharedResource resource;

    public WorkerThread(SharedResource resource) {
        this.resource = resource;
    }

    @Override
    public void run() {
        for (int i = 0; i < 3; i++) {
            resource.incrementCounter();
        }
    }
}

// Main class to run the demo
public class synchro {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Synchronized Block Demo");

        // Create one instance of the shared resource
        SharedResource sharedResource = new SharedResource();

        // Create two threads that share the same resource
        Thread t1 = new Thread(new WorkerThread(sharedResource), "Thread-1");
        Thread t2 = new Thread(new WorkerThread(sharedResource), "Thread-2");

        // Start the threads
        t1.start();
        t2.start();

        // Wait for both threads to finish
        t1.join();
        t2.join();

        System.out.println("Final counter value: " + sharedResource.getCounter());
        System.out.println("Expected final value (2 threads * 3 increments): 6");
        System.out.println("--- Demo Finished ---");
    }
}