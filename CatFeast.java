import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Stack;

public class CatFeast {
    public PriorityQueue<Edge> edges;
    public int[][] graph;
    public boolean[] catsFed;
    public boolean debug = false;
    int numOfCats;
    public CatFeast(int numOfCats) {
        this.graph = new int[numOfCats][numOfCats];
        this.edges = new PriorityQueue<Edge>(numOfCats, ((edge1, edge2) -> (edge1.weight - edge2.weight)));
        this.catsFed = new boolean[numOfCats];
        this.numOfCats = numOfCats;

        for (int i = 0; i < numOfCats; i++) {
            this.catsFed[i] = false;
            this.graph[i][i] = 0;
        }
    }

    public void visit(int v) {
        this.catsFed[v] = true;
        for (int i = 0; i < this.numOfCats; i++) {
            if (v == i) {
                continue;
            }
            if (debug) {
                System.out.println("Visiting cat " + i);
            }
            if (!this.catsFed[i]) {
                if (debug) {
                    System.out.println("Adding edge between " + v + " and " + i + " to pq.");
                }
                this.edges.add(new Edge(v, i, this.graph[v][i]));
            }
        }     
    }

    public static void main(String[] args) {
        boolean debug = false;
        CatFeast cf;
        Scanner scan = new Scanner(System.in);
        int numOfTests = scan.nextInt();
        scan.nextLine();
        int numOfMl, numOfCats, numOfLoops, result;
        for (int i = 0; i < numOfTests; i++) {
            numOfMl = scan.nextInt();
            numOfCats = scan.nextInt();
            result = 0;
            cf = new CatFeast(numOfCats);
            scan.nextLine();
            numOfLoops = ((numOfCats - 1) * numOfCats) / 2;
            int head, tail, distance;
            for (int n = 0; n < numOfLoops; n++) {
                head = scan.nextInt();
                tail = scan.nextInt();
                distance = scan.nextInt();
                cf.graph[head][tail] = distance;
                cf.graph[tail][head] = distance;
            }
            cf.visit(0);
            for (int n = 1; n < 5; n++) {
                cf.edges.add(new Edge(0, n, cf.graph[0][n]));
            }
            Edge e;
            int v, w;
            while (!cf.edges.isEmpty()) {
                e = cf.edges.poll();
                v = e.cats[0];
                w = e.cats[1];
                if (debug) {
                    System.out.println("Processing edge between " + e.cats[0] + " and " + e.cats[1]);
                    System.out.println("Weight of this edge is " + e.weight);
                }
                if (cf.catsFed[v] && cf.catsFed[w]) {
                    if (debug) {
                        System.out.println("Both visited, pass");
                    }
                    continue;
                }
                if (!cf.catsFed[v]) {
                    if (debug) {
                        System.out.println("" + v + " hasn't been visited.");
                    }
                    cf.visit(v);
                    result += e.weight;
                }
                if (!cf.catsFed[w]) {
                    if (debug) {
                        System.out.println("" + w + " hasn't been visited.");
                    }
                    cf.visit(w);
                    result += e.weight;
                }
            }
            if (debug) {
                System.out.println("required milk is " + (result + numOfCats));
            }
            if ((result + numOfCats) <= numOfMl) {
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