import java.util.Scanner;
public class CatFeast {
    public int numOfCats;
    public Cat[] cats;
    public int[][] route;
    public boolean debug = false;
    public CatFeast(int numOfCats) {
        this.numOfCats = numOfCats;
        this.cats = new Cat[numOfCats];
        this.route = new int[numOfCats][numOfCats];
        for (int i = 0; i < numOfCats; i++) {
            this.cats[i] = new Cat();
            for (int n = 0; n < numOfCats; n++) {
                if (i == n) {
                    this.route[i][n] = 0;
                    continue;
                }
                this.route[i][n] = -1;
            }
        }
        cats[0].distance = 0;
        cats[0].previous = 0;  
    }

    public void changeRoute(int current, int previous, int oldPrevious, int distance) {
        if (debug) {
            System.out.println("changing route for cat " + current);
            System.out.println("oldPrevious = " + oldPrevious);
        }
        if (oldPrevious != -1) {
            route[oldPrevious][current] = -1;
        }
        route[previous][current] = distance;
        if (debug) {
            debugger();
        }
    }

    public int sumMl() {
        int finalMl = 0;
        for (int i = 0; i < this.numOfCats; i++) {
            for (int n = 0; n < this.numOfCats; n++) {
                if (this.route[i][n] != -1) {
                    finalMl += this.route[i][n];
                }
            }
        }
        if (debug) {
            System.out.println(finalMl);
        }
        return finalMl;
    }

    public void debugger() {
        for (int i = 0; i < this.numOfCats; i++) {
            for (int n = 0; n < this.numOfCats; n++) {
                System.out.printf(this.route[i][n] + " ");
            }
            System.out.println("\n");
        }
    }

    public static void main(String[] args) {
        boolean debug = false;
        CatFeast cf;
        Scanner scan = new Scanner(System.in);
        int numOfTests = scan.nextInt();
        scan.nextLine();
        int numOfMl;
        int numOfCats;
        int result;
        for (int i = 0; i < numOfTests; i++) {
            numOfMl = scan.nextInt();
            numOfCats = scan.nextInt();
            if (numOfCats > numOfMl) {
                System.out.println("no");
                continue;
            }
            scan.nextLine();
            cf = new CatFeast(numOfCats);
            int head;
            int tail;
            int dist;
            int numOfLoops = ((numOfCats) * (numOfCats - 1)) / 2;
            for (int n = 0; n < numOfLoops; n++) {
                head = scan.nextInt();
                tail = scan.nextInt();
                dist = scan.nextInt();
                scan.nextLine();
                if (debug) {
                    System.out.println("I'm cat " + tail);
                    System.out.println("dist = " + dist);
                    System.out.println("head's distance = " + cf.cats[head].distance);
                }

                if (cf.cats[tail].relax(dist, cf.cats[head].distance, head)) {
                    int oldPrevious = cf.cats[tail].updatePrevious(head);
                    cf.changeRoute(tail, head, oldPrevious, dist);
                }
            }
            result = cf.sumMl() + numOfCats;
            if (result > numOfMl) {
                System.out.println("no");
            } else {
                System.out.println("yes");
            }
        }
        scan.close();
        
    }
}

class Cat {
    public int distance;
    public int previous;
    public boolean debug = false;

    Cat () {
        this.distance = -1;
        this.previous = -1;
    }

    public boolean relax(int distance, int offset, int previous) {
        if (debug) {
            System.out.println("this.distance = " + this.distance);
            System.out.println("offset + distance = " + (offset + distance));
        }
        if (this.distance == -1) {
            this.distance = distance + offset;
            return true;
        }
        if (this.distance <= offset + distance) {
            return false;
        }
        this.distance = distance + offset;
        return true;
    }

    public int updatePrevious(int previous) {
        int old = this.previous;
        this.previous = previous; 
        return old;
    }
}