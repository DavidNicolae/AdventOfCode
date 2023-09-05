package Day11;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.LinkedList;

public class Main2 {

    static boolean isPosition(int x, int y) {
        if (x >= 0 && x < 10 && y >= 0 && y < 10) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day11/input.txt"));
        String s;
        int[][] grid = new int[10][10];
        int lines = -1;
        while ((s = bufferedReader.readLine()) != null) {
            lines++;
            for (int i = 0; i < s.length(); i++) {
                grid[lines][i] = Character.getNumericValue(s.charAt(i));
            }
        }
        int total, step = 0;
        LinkedList<Position> explosions = new LinkedList<>();
        while (true) {
            total = 0;
            step++;
            int[][] exploded = new int[10][10];
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    grid[i][j]++;
                    if (grid[i][j] > 9) {
                        explosions.add(new Position(i, j));
                        exploded[i][j] = 1;
                    }
                }
            }
            while (!explosions.isEmpty()) {
                Position temp = explosions.poll();
                grid[temp.x][temp.y] = 0;
                total++;

                ArrayList<Position> adjacent = new ArrayList<>();
                adjacent.add(new Position(temp.x - 1, temp.y - 1));
                adjacent.add(new Position(temp.x - 1, temp.y));
                adjacent.add(new Position(temp.x - 1, temp.y + 1));
                adjacent.add(new Position(temp.x, temp.y - 1));
                adjacent.add(new Position(temp.x, temp.y + 1));
                adjacent.add(new Position(temp.x +  1, temp.y - 1));
                adjacent.add(new Position(temp.x + 1, temp.y));
                adjacent.add(new Position(temp.x + 1, temp.y + 1));

                for (Position p : adjacent) {
                    if (isPosition(p.x, p.y)) {
                        if (exploded[p.x][p.y] != 1) {
                            grid[p.x][p.y]++;
                            if (grid[p.x][p.y] > 9) {
                                explosions.add(p);
                                exploded[p.x][p.y] = 1;
                            }
                        }
                    }
                }
            }
            if (total == 100) {
                break;
            }
        }
        System.out.println(step);
    }
}
