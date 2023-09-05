package Day2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day2/input.txt"));
        int h_pos = 0, depth = 0;
        String type;
        for (int i = 0; i < 1000; i++) {
            String s = bufferedReader.readLine();
            StringTokenizer st = new StringTokenizer(s);
            type = st.nextToken();
            if (type.compareTo("forward") == 0) {
                h_pos += Integer.parseInt(st.nextToken());
            } else if (type.compareTo("down") == 0) {
                depth += Integer.parseInt(st.nextToken());
            } else {
                depth -= Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(h_pos * depth);
    }
}
