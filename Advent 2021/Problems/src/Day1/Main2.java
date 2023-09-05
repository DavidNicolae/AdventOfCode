package Day1;

import java.io.BufferedReader;
import java.io.FileReader;

public class Main2 {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day1/input.txt"));
        String s = bufferedReader.readLine();
        int[] v = new int[2000];
        v[0] = Integer.parseInt(s);
        for (int i = 1; i < 2000; i++) {
            s = bufferedReader.readLine();
            v[i] = Integer.parseInt(s);
        }
        int count = 0, prev = v[0] + v[1] + v[2], next;
        for (int i = 1; i < 1998; i++) {
            next = v[i] + v[i + 1] + v[i + 2];
            if (next > prev) {
                count++;
            }
            prev = next;
        }
        System.out.println(count);
        bufferedReader.close();
    }
}