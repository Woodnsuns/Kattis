import java.util.Scanner;

public class AirportCoffee {
    public long[] carts;
    public int numOfCarts;
    public boolean debug = true;
    AirportCoffee(int numOfCarts) {
        this.numOfCarts = numOfCarts;
        this.carts = new long[numOfCarts];
    }

    //Finds the shop furthest from current position before finish drinking coffee
    public int bstBeforeFinish(int currentCartIndex, long finishPos) {
        int low = currentCartIndex;
        int high = numOfCarts - 1;
        int mid = (low + high) / 2;
        while (true) {
            if ((high - low) <= 1) {
                if ((this.carts[low + 1] > finishPos) && (this.carts[low] <= finishPos)) {
                    if (debug) {
                        System.out.println("carts[low] = " + carts[low]);
                    }
                    return low;
                }
                
            }
            if (this.carts[mid] < finishPos) {
                low = mid;
            } else {
                high = mid;
            }
            mid = (low + high) / 2;
            if(debug) {
                System.out.println("Still in the loop of bstBeforeFinish");
                System.out.println("mid = " + mid + ", position at " + carts[mid]);
                System.out.println("high = " + high + ", low = " + low);
            }
        }
    }
    
    //Finds the shop nearest from current position after finish drinking coffee
    public int bstAfterFinish(int currentCartIndex, long finishPos) {
        int low = currentCartIndex;
        int high = numOfCarts - 1;
        int mid = (low + high) / 2;
        while (true) {
            if ((high - low) <= 1) {
                if ((this.carts[high - 1] < finishPos) && (this.carts[high] >= finishPos)) {
                    return high;
                }
            }
            if (this.carts[mid] > finishPos) {
                high = mid;
            } else {
                low = mid;
            }
            mid = (low + high) / 2;
            if(debug) {
                System.out.println("Still in the loop of bstAfterFinish");
                System.out.println("mid = " + mid + ", position at " + carts[mid]);
                System.out.println("finishPos = " + finishPos + ", carts[mid - 1] = " + carts[mid - 1]);
                System.out.println("high = " + high + ", low = " + low);
            }
        }

    }

    public static void main(String[] args) {
        AirportCoffee ac;
        long currentCart, boardingGate, nextBeforeFinish, nextAfterFinish, nextCart, coldPos, finishPos;
        int slowSpeed, fastSpeed, coldTime, drinkTime, numOfCarts, currentCartIndex, nextCartIndex;
        int nextBeforeFinishIndex, nextAfterFinishIndex;
        int numOfCups;
        long[] coffeeSpots;
        boolean debug = true;
    
        Scanner scan = new Scanner(System.in);
        boardingGate = scan.nextLong();
        slowSpeed = scan.nextInt();
        fastSpeed = scan.nextInt();
        coldTime = scan.nextInt();
        drinkTime = scan.nextInt();
        scan.nextLine();
        numOfCarts = scan.nextInt();
        ac = new AirportCoffee(numOfCarts);
        coffeeSpots = new long[numOfCarts];
        for (int i = numOfCarts - 1; i >= 0; i--) {
            ac.carts[i] = boardingGate - scan.nextInt();
        }
        
        if (numOfCarts == 0) {
            System.out.println ("0");
            return;
        } 
        if (numOfCarts == 1) {
            System.out.println("1");
            System.out.println("0");
            return;
        }
        

        currentCartIndex = 0;
        numOfCups = 0;
        currentCart = ac.carts[currentCartIndex];
        coldPos = currentCart + (slowSpeed * coldTime);
        finishPos = coldPos + (fastSpeed * drinkTime);
        numOfCups++;
        coffeeSpots[0] = currentCartIndex;
         
        double speed1, speed2, time1, time2;
        while (true) {
            if (debug) {
                System.out.println("currentCartIndex = " + currentCartIndex);
                System.out.println("numOfCarts = " + numOfCarts);
                System.out.println("current finish position = " + finishPos);
                System.out.println("boarding gate at " + boardingGate);
            }
            if (currentCartIndex >= numOfCarts - 1) {
                break;
            }
            if (finishPos >= ac.carts[numOfCarts - 1]) {
                if(debug) {
                    System.out.println("Getting out of loop hooray");
                }
                break;
            }

            nextBeforeFinishIndex = ac.bstBeforeFinish(currentCartIndex, finishPos);
            nextBeforeFinish = ac.carts[nextBeforeFinishIndex];
            nextAfterFinishIndex = ac.bstAfterFinish(currentCartIndex, finishPos);
            nextAfterFinish = ac.carts[nextAfterFinishIndex];
            if (nextBeforeFinishIndex == nextAfterFinishIndex) {
                currentCartIndex = nextBeforeFinishIndex;
                currentCart = nextBeforeFinish;
                continue;
            }
            if (debug) {
                System.out.println("nextBeforeFinishIndex = " + nextBeforeFinishIndex);
                System.out.println("nextAfterFinishIndex = " + nextAfterFinishIndex);
            }

            time1 = coldTime + drinkTime + ((nextAfterFinish - finishPos) / slowSpeed);
            if (((nextAfterFinish - nextBeforeFinish) / slowSpeed) > coldTime) {
                if ((((nextAfterFinish - nextBeforeFinish) - (coldTime * slowSpeed)) / fastSpeed) > drinkTime) {
                    time2 = coldTime + drinkTime - ((finishPos - nextBeforeFinish) / fastSpeed)
                            + coldTime + drinkTime + ((nextAfterFinish - (nextBeforeFinish + finishPos - currentCart)) / slowSpeed);        
                } else {
                    time2 = coldTime + drinkTime - ((finishPos - nextBeforeFinish) / fastSpeed) 
                            + coldTime + drinkTime - (nextBeforeFinish + (nextBeforeFinish + (finishPos - currentCart) - nextAfterFinish) / fastSpeed);
                }
            } else {
                time2 = ((nextAfterFinish - nextBeforeFinish) / slowSpeed);
            }
            if (debug) {
                System.out.println("time1 = " + time1);
                System.out.println("time2 = " + time2);
            }
            speed1 = (nextAfterFinish - currentCart) / time1;
            speed2 = (nextAfterFinish - currentCart) / time2;
            if (debug) {
                System.out.println("speed1 = " + speed1 + ", speed2 = " + speed2);
            }
            if (speed1 >= speed2) {
                numOfCups++;
                coffeeSpots[numOfCups - 1] = nextAfterFinishIndex;
                currentCartIndex = nextAfterFinishIndex;
                currentCart = nextAfterFinish;
                coldPos = currentCart + (slowSpeed * coldTime);
                finishPos = coldPos + (fastSpeed * drinkTime);

            } else {
                numOfCups++;
                coffeeSpots[numOfCups - 1] = nextBeforeFinishIndex;
                currentCartIndex = nextBeforeFinishIndex;
                currentCart = nextBeforeFinish;
                coldPos = currentCart + (slowSpeed * coldTime);
                finishPos = coldPos + (fastSpeed * drinkTime);
            }
            if (debug) {
                System.out.println("numOfCups currently = " + numOfCups);
                for (int i = 0; i < numOfCups; i++) {
                    System.out.println(coffeeSpots[i]);
                }
            }
        }
        System.out.println(numOfCups);
        for (int i = 0; i < numOfCups; i++) {
            System.out.printf(coffeeSpots[i] + " ");
        }

        System.out.println("\n");
        
        scan.close();
        return;
    }

}