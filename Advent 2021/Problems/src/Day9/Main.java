package Day9;

import java.io.BufferedReader;
import java.io.FileReader;

public class Main {

    static boolean isPosition(int x, int y) {
        if (x >= 0 && x < 100 && y >= 0 && y < 100) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day9/input.txt"));
        int[][] map = new int[100][100];
        String s;
        int line = 0;
        while ((s = bufferedReader.readLine()) != null) {
            for (int i = 0; i < s.length(); i++) {
                map[line][i] = Character.getNumericValue(s.charAt(i));
            }
            line++;
        }
        int total = 0;
        for (int i = 0; i < 100; i ++) {
            for (int j = 0; j < 100; j++) {
                if (isPosition(i - 1, j)) {
                    if (map[i][j] >= map[i - 1][j]) {
                        continue;
                    }
                }
                if (isPosition(i, j - 1)) {
                    if (map[i][j] >= map[i][j - 1]) {
                        continue;
                    }
                }
                if (isPosition(i + 1, j)) {
                    if (map[i][j] >= map[i + 1][j]) {
                        continue;
                    }
                }
                if (isPosition(i, j + 1)) {
                    if (map[i][j] >= map[i][j + 1]) {
                        continue;
                    }
                }
                total += map[i][j];
                total += 1;
            }
        }
        System.out.println(total);
    }
}
