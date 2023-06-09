import java.util.Arrays;

class Elevator implements Comparable<Elevator> {
    int major;
    int minor;
    int revision;
    String str;

    public Elevator(String elevator) {
        // Split the elevator string by '.' and parse the parts
        String[] div = elevator.split("\\.");
        // Store the original elevator string
        this.str = elevator;
        // Extract the major version
        major = Integer.parseInt(div[0]);
        // Extract the minor version if present, otherwise set it to -1
        minor = div.length > 1 ? Integer.parseInt(div[1]) : -1;
        // Extract the revision version if present, otherwise set it to -1
        revision = div.length > 2 ? Integer.parseInt(div[2]) : -1;
    }

    @Override
    public int compareTo(Elevator o) {
        // Compare elevators based on major, minor, and revision versions
        if (this.major < o.major) return -1;
        if (this.major > o.major) return 1;
        if (this.minor < o.minor) return -1;
        if (this.minor > o.minor) return 1;
        if (this.revision < o.revision) return -1;
        if (this.revision > o.revision) return 1;
        return 0;
    }
}

class Solution {
    public static String[] solution(String[] l) {
        int len = l.length;
        Elevator[] els = new Elevator[len];
        for (int i = 0; i < len; i++) {
            els[i] = new Elevator(l[i]);
        }
        // Sort the elevators based on their versions using the compareTo method
        Arrays.sort(els);
        // Create a new string array to store the sorted elevator strings
        String[] finals = new String[len];
        for (int i = 0; i < len; i++) {
            finals[i] = els[i].str;
        }
        return finals;
    }

    public static void main(String[] args) {
        String[] l1 = {"1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"};
        System.out.println(Arrays.toString(Solution.solution(l1)));

        String[] l2 = {"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"};
        System.out.println(Arrays.toString(Solution.solution(l2)));
    }
}
