package Day8;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day8/input.txt"));
        String s;
        int count = 0;
        ArrayList<Integer> unique_segments = new ArrayList<>();
        unique_segments.add(2);
        unique_segments.add(3);
        unique_segments.add(4);
        unique_segments.add(7);
        while ((s = bufferedReader.readLine()) != null) {
            StringTokenizer stringTokenizer = new StringTokenizer(s, "|");
            stringTokenizer.nextToken();
            String output = stringTokenizer.nextToken();
            StringTokenizer stringTokenizer1 = new StringTokenizer(output, " ");
            while (stringTokenizer1.hasMoreTokens()) {
                if (unique_segments.contains(stringTokenizer1.nextToken().length())) {
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}
