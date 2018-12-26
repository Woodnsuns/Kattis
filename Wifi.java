import java.util.Scanner;
import java.util.Arrays;
import java.lang.Integer;

public class Wifi {
    public int[] arr;
    public int numOfWifi;
    public int numOfHouses;
    public int bound;
    public boolean debug = false;
    public Wifi(int numOfWifi, int numOfHouses) {
        this.arr = new int[numOfHouses];
        this.numOfWifi = numOfWifi;
        this.numOfHouses = numOfHouses;
    }

    public double setWifi() {
        if (debug) {
            for(int i = 0; i < this.numOfHouses; i++) {
                System.out.println(this.arr[i]);
            }
            
        }
        if (this.numOfHouses <= this.numOfWifi) {
            System.out.println("0.0");
            return 0;
        }
        return this.roundUp(this.binarySearch());
    }

    public double binarySearch() {
        double upper = this.arr[numOfHouses-1];
        double lower = 0;
        double bound = 0;
        int numOfGroups = 0;
        int head = 0;
        while ((upper - lower) > 0.01) {
            if (debug) {
                System.out.println("Bound now is " + bound);
                System.out.println("Upper is " + upper + " and lower is " + lower);
            }
            bound = (upper + lower) / 2;
            head = 0;
            numOfGroups = 1;
            for (int i = 1; i < numOfHouses; i++) {
                if ((this.arr[i] - this.arr[head]) > bound) {
                    numOfGroups ++;
                    head = i;
                }
                if (numOfGroups > this.numOfWifi) {
                    break;
                }
            }
            if (numOfGroups <= this.numOfWifi) {
            upper = bound;
            } else {
                lower = bound;
            }
        }
        return bound;
    }

    public double roundUp(double bound) {
        bound = bound / 2;
        double result = (Math.round(bound * 10)) / 10.0;
        
        System.out.println(result);
        return result;
    }

    public static void main(String[] args) {
        Wifi wifi;
        Scanner scanner = new Scanner(System.in);
        int numOfTests = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < numOfTests; i++) {
            wifi = new Wifi(scanner.nextInt(), scanner.nextInt());
            scanner.nextLine();
            for (int n = 0; n < wifi.numOfHouses; n++) {
                wifi.arr[n] = scanner.nextInt();
                scanner.nextLine();
            }
            Arrays.sort(wifi.arr);

            wifi.setWifi();
        }
        
    }
}