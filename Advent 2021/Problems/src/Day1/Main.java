package Day1;

import java.io.BufferedReader;
import java.io.FileReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day1/input.txt"));
        String s = bufferedReader.readLine();
        int prev, next, count = 0;
        prev = Integer.parseInt(s);
        for (int i = 0; i < 1999; i++) {
            s = bufferedReader.readLine();
            next = Integer.parseInt(s);
            if (next > prev) {
                count++;
            }
            prev = next;
        }
        System.out.println(count);
        bufferedReader.close();
    }
}
