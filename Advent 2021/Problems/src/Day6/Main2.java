package Day6;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main2 {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day6/input.txt"));
        String s = bufferedReader.readLine();
        StringTokenizer stringTokenizer = new StringTokenizer(s, ",");
        Map<Integer, Long> fish = new TreeMap<>();
        while (stringTokenizer.hasMoreTokens()) {
            Integer key = Integer.parseInt(stringTokenizer.nextToken());
            if (fish.containsKey(key)) {
                fish.replace(key, fish.get(key) + 1);
            } else {
                fish.put(key, 1L);
            }
        }
        fish.put(0, 0L);
        fish.put(6, 0L);
        fish.put(7, 0L);
        fish.put(8, 0L);
        for (int j = 0; j < 256; j++) {
            long new_6 = 0;
            for (Integer key : fish.keySet()) {
                if (key == 0) {
                    new_6 = fish.get(key);
                }
                if (key != 8) {
                    fish.put(key, fish.get(key + 1));
                } else {
                    fish.replace(key, 0L);
                }
            }
            fish.replace(6, fish.get(6) + new_6);
            fish.replace(8, new_6);
        }
        long sum = 0;
        for (int key : fish.keySet()) {
            sum += fish.get(key);
        }
        System.out.println(sum);
    }
}
