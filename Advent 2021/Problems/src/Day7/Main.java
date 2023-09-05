package Day7;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static int compute_cost(ArrayList<Integer> v, int x) {
        int cost = 0;
        for (Integer a : v) {
            cost += Math.abs(a - x);
        }
        return cost;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new FileReader("src/Day7/input.txt"));
        String s = reader.readLine();
        StringTokenizer stringTokenizer = new StringTokenizer(s, ",");
        ArrayList<Integer> v = new ArrayList<>();
        while (stringTokenizer.hasMoreTokens()) {
            v.add(Integer.parseInt(stringTokenizer.nextToken()));
        }
        int low = v.get(0), high = v.get(0);
        for (Integer a : v) {
            if (a < low) {
                low = a;
            }
            if (a > high) {
                high = a;
            }
        }
        while ((high - low) > 2) {
            int mid1 = low + (high - low) / 3;
            int mid2 = high - (high - low) / 3;

            int cost1 = compute_cost(v, mid1);
            int cost2 = compute_cost(v, mid2);

            if (cost1 < cost2) {
                high = mid2;
            } else {
                low = mid1;
            }
        }
        System.out.println(compute_cost(v, (high + low) / 2));
    }
}
