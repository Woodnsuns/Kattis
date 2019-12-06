import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Stack;

public class CatFeast {
    public PriorityQueue<Edge> edges;
    public boolean[] catsFed;
    public CatFeast(int numOfCats) {
        this.edges = new PriorityQueue<Edge>(numOfCats, ((edge1, edge2) -> (edge1.weight - edge2.weight)));
        this.catsFed = new boolean[numOfCats];
        for (int i = 0; i < numOfCats; i++) {
            this.catsFed[i] = false;
        }
    }

    public feed(int cat1, int cat2) {
        catsFed[cat1] = true;
        catsFed[cat2] = true;
    }
    public static void main(String[] args) {
        boolean debug = false;
        CatFeast cf;
        Scanner scan = new Scanner(System.in);
        int numOfTests = scan.nextInt();
        scan.nextLine();
        int numOfMl, numOfCats, numOfLoops, result;
        for (int i = 0; i < numOfTests; i++) {
            result = 0;
            int head, tail, distance;
            numOfMl = scan.nextInt();
            numOfCats = scan.nextInt();
            if (numOfMl < numOfCats) {
                System.out.println("no");
            }
            cf = new CatFeast(numOfCats);
            scan.nextLine();
            numOfLoops = (numOfCats * (numOfCats - 1)) / 2;
            for (int n = 0; n < numOfLoops; n++) {
                head = scan.nextInt();
                tail = scan.nextInt();
                distance = scan.nextInt();
                cf.edges.add(new Edge(head, tail, distance));
            }
            Stack<Edge> eTemps = new Stack<>();
            Edge e = cf.edges.poll();
            int[] pair = e.cats;
            cf.catsFed[pair[0]] = true;
            cf.catsFed[pair[1]] = true;
            result += e.weight;
            for (int n = 0; n < (numOfCats - 2); n++) {
                if (debug) {
                    System.out.println("We re finding " + (n + 2) + "th edge");
                }
                while (true) {
                    e = cf.edges.poll();
                    pair = e.cats;
                    if (debug) {
                        System.out.println("smallest edge now has weight " + e.weight);
                        System.out.println("The edge is between cat " + pair[0] + " and cat " + pair[1]);
                    }
                    if ((!cf.catsFed[pair[0]]) && !(cf.catsFed[pair[1]])) {
                        eTemps.push(e);
                        continue;
                    } else if (cf.catsFed[pair[0]] && cf.catsFed[pair[1]]) {
                        continue;
                    } else {
                        cf.catsFed[pair[0]] = true;
                        cf.catsFed[pair[1]] = true;
                    }
                    result += e.weight;
                    break;
                }
                while (!eTemps.empty()) {
                    cf.edges.add(eTemps.pop());
                }
            }
            result += numOfCats;
            if (debug) {
                System.out.println("result = " + result);
            }
            if (result <= numOfMl) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }
        scan.close();
    }
}

class Edge {
    public int[] cats;
    public int weight;

    public Edge(int head, int tail, int weight) {
        this.cats = new int[2];
        this.cats[0] = head;
        this.cats[1] = tail;
        this.weight = weight;
    }
}