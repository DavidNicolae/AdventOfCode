package Day9;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;

class Point {
    int x;
    int y;
    ArrayList<Point> adj_positions;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
        adj_positions = new ArrayList<>();
    }
}

public class Main2 {

    static boolean isPosition(int x, int y) {
        return x >= 0 && x < 100 && y >= 0 && y < 100;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day9/input.txt"));
        int[][] map = new int[100][100];
        boolean[][] visited = new boolean[100][100];
        String s;
        int line = 0;
        while ((s = bufferedReader.readLine()) != null) {
            for (int i = 0; i < s.length(); i++) {
                map[line][i] = Character.getNumericValue(s.charAt(i));
            }
            line++;
        }
        ArrayList<Integer> basins = new ArrayList<>();
        for (int i = 0; i < 100; i ++) {
            for (int j = 0; j < 100; j++) {
                if (isPosition(i - 1, j)) {
                    if (map[i - 1][j] <= map[i][j]) {
                        continue;
                    }
                }
                if (isPosition(i, j - 1)) {
                    if (map[i][j - 1] <= map[i][j]) {
                        continue;
                    }
                }
                if (isPosition(i + 1, j)) {
                    if (map[i + 1][j] <= map[i][j]) {
                        continue;
                    }
                }
                if (isPosition(i, j + 1)) {
                    if (map[i][j + 1] <= map[i][j]) {
                        continue;
                    }
                }
                int basin_size = 0;
                visited[i][j] = true;
                LinkedList<Point> queue = new LinkedList<>();
                queue.add(new Point(i, j));

                while (queue.size() != 0) {
                    Point temp = queue.poll();
                    temp.adj_positions.add(new Point(temp.x - 1, temp.y));
                    temp.adj_positions.add(new Point(temp.x, temp.y - 1));
                    temp.adj_positions.add(new Point(temp.x + 1, temp.y));
                    temp.adj_positions.add(new Point(temp.x, temp.y + 1));
                    basin_size++;

                    for (Point p : temp.adj_positions) {
                        if (isPosition(p.x, p.y) && map[p.x][p.y] != 9 && !visited[p.x][p.y]) {
                            visited[p.x][p.y] = true;
                            queue.add(p);
                        }
                    }
                }
                basins.add(basin_size);
            }
        }
        basins.sort((o1, o2) -> o2 - o1);
        System.out.println(basins.get(0) * basins.get(1) * basins.get(2));
    }
}
