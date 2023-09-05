package Day15;

import java.io.BufferedReader;
import java.io.FileReader;

public class Main2 {

    static final int M1 = 100, N1 = 100, M = 5 * M1, N = 5 * N1;
    static int[][] m1 = new int[M1][N1];
    static int[][] m = new int[M][N];

    static int min(int[][] dp, int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
        int a1, a2, a3, a4;
        if (x1 < 0 || y1 < 0 || x1 >= M || y1 >= N) {
            a1 = Integer.MAX_VALUE;
        } else {
            a1 = dp[x1][y1];
        }
        if (x2 < 0 || y2 < 0 || x2 >= M || y2 >= N) {
            a2 = Integer.MAX_VALUE;
        } else {
            a2 = dp[x2][y2];
        }
        if (x3 < 0 || y3 < 0 || x3 >= M || y3 >= N) {
            a3 = Integer.MAX_VALUE;
        } else {
            a3 = dp[x3][y3];
        }
        if (x4 < 0 || y4 < 0 || x4 >= M || y4 >= N) {
            a4 = Integer.MAX_VALUE;
        } else {
            a4 = dp[x4][y4];
        }
        return Math.min(Math.min(a1, a2), Math.min(a3, a4));
    }

    static int min_cost_dp() {
        int[][] dp = new int[M][N];
        dp[0][0] = 0;
        for (int i = 1; i < M; i++) {
            dp[i][0] = dp[i - 1][0] + m[i][0];
        }
        for (int i = 1; i < N; i++) {
            dp[0][i] = dp[0][i - 1] + m[0][i];
        }
        for (int i = 1; i < M; i++) {
            for (int j = 1; j < N; j++) {
                dp[i][j] = Math.min(dp[i][j - 1], dp[i - 1][j]) + m[i][j];
            }
        }
        while (true) {
            boolean changed = false;
            for (int i = 1; i < M; i++) {
                for (int j = 1; j < N; j++) {
                    int temp = min(dp, i - 1, j, i, j - 1, i + 1, j, i, j + 1);
                    if (dp[i][j] > temp + m[i][j]) {
                        dp[i][j] = temp + m[i][j];
                        changed = true;
                    }
                }
            }
            if (!changed) {
                break;
            }
        }
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(dp[i][j] + " ");
            }
            System.out.println();
        }
        return dp[M - 1][N - 1];
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day15/input.txt"));
        String s;
        int line = 0;
        while ((s = bufferedReader.readLine()) != null) {
            for (int i = 0; i < N1; i++) {
                m1[line][i] = Character.getNumericValue(s.charAt(i));
            }
            line++;
        }
        int tile_i = -1, tile_j = -1;
        for (int i = 0; i < M; i++) {
            if (i % M1 == 0) {
                tile_i++;
            }
            for (int j = 0; j < N; j++) {
                if (j % N1 == 0) {
                    tile_j++;
                }
                if ((m[i][j] = (m1[i % M1][j % N1] + tile_i + tile_j) % 9) == 0) {
                    m[i][j] = 9;
                }
            }
            tile_j = -1;
        }

//        for (int i = 0; i < M; i++) {
//            for (int j = 0; j < N; j++) {
//                System.out.print(m[i][j]);
//            }
//            System.out.println();
//        }

        int cost = min_cost_dp();
        System.out.println(cost);
    }
}
