package Day13;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day13/input.txt"));
        String s;
        ArrayList<String> folds = new ArrayList<>();
        ArrayList<Integer> x = new ArrayList<>();
        ArrayList<Integer> y = new ArrayList<>();
        int max_x = -1, max_y = -1;
        while ((s = bufferedReader.readLine()) != null) {
            StringTokenizer stringTokenizer = new StringTokenizer(s, ", ");
            if (stringTokenizer.hasMoreTokens()) {
                String s1 = stringTokenizer.nextToken(), s2;
                if (s1.equals("fold")) {
                    s1 = stringTokenizer.nextToken();
                    s1 = stringTokenizer.nextToken();
                    folds.add(s1);
                } else {
                    s2 = stringTokenizer.nextToken();
                    x.add(Integer.parseInt(s2));
                    y.add(Integer.parseInt(s1));
                    if (Integer.parseInt(s1) > max_y) {
                        max_y = Integer.parseInt(s1);
                    }
                    if (Integer.parseInt(s2) > max_x) {
                        max_x = Integer.parseInt(s2);
                    }
                }
            }
        }
        int[][] m = new int[max_x + 1][max_y + 1];
        for (int i = 0; i < x.size(); i++) {
            m[x.get(i)][y.get(i)] = 1;
        }
        StringTokenizer stringTokenizer = new StringTokenizer(folds.get(0), "=");
        String s1 = stringTokenizer.nextToken();
        String line = stringTokenizer.nextToken();
        int count = 0;
        if (s1.equals("y")) {
            for (int i = 0; i < Integer.parseInt(line); i++) {
                for (int j = 0; j < max_y + 1; j++) {
                    if (m[i][j] == 1) {
                        count++;
                        if (m[max_x - i][j] == 1) {
                            m[max_x - i][j] = 0;
                        }
                    }
                }
            }
            for (int i = Integer.parseInt(line) + 1; i < max_x + 1; i++) {
                for (int j = 0; j < max_y + 1; j++) {
                    if (m[i][j] == 1) {
                        count++;
                    }
                }
            }
        } else {
            for (int i = 0; i < max_x + 1; i++) {
                for (int j = 0; j < Integer.parseInt(line); j++) {
                    if (m[i][j] == 1) {
                        count++;
                        if (m[i][max_y - j] == 1) {
                            m[i][max_y - j] = 0;
                        }
                    }
                }
            }
            for (int i = 0; i < max_x + 1; i++) {
                for (int j = Integer.parseInt(line) + 1; j < max_y + 1; j++) {
                    if (m[i][j] == 1) {
                        count++;
                    }
                }
            }
        }
        System.out.println(count);
    }
}
