package Day6;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day6/input.txt"));
        String s = bufferedReader.readLine();
        StringTokenizer stringTokenizer = new StringTokenizer(s, ",");
        ArrayList<Integer> fish = new ArrayList<>();
        while (stringTokenizer.hasMoreTokens()) {
            fish.add(Integer.parseInt(stringTokenizer.nextToken()));
        }
        for (int j = 0; j < 80; j++) {
            ArrayList<Integer> temp = new ArrayList<>();
            for (int i = 0; i < fish.size(); i++) {
                if (fish.get(i) != 0) {
                    fish.set(i, fish.get(i) - 1);
                } else {
                    fish.set(i, 6);
                    temp.add(8);
                }
            }
            fish.addAll(fish.size(), temp);
        }
        System.out.println(fish.size());
    }
}
