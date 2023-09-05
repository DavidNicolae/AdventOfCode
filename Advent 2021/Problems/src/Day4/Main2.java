package Day4;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class Main2 {
    static ArrayList<int[][]> boards = new ArrayList<>();
    static int[][] winner = new int[5][5];
    static int winning_nr;

    public static boolean bingo(int i, int j, int k, int nr) {
        // Se pastreaza ultima tabla castigatoare in state-ul in care se afla la momentul castigului
        int count_line = 0, count_column = 0;
        for (int a = 0; a < 5; a++) {
            if (boards.get(i)[j][a] == -1) {
                count_line++;
            }
            if (boards.get(i)[a][k] == -1) {
                count_column++;
            }
        }
        if (count_line == 5 || count_column == 5) {
            winner = boards.get(i);
            winning_nr = nr;
            return true;
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day4/input.txt"));
        ArrayList<Integer> numbers = new ArrayList<>();
        String s = bufferedReader.readLine();
        StringTokenizer stringTokenizer = new StringTokenizer(s, ", ");
        while (stringTokenizer.hasMoreTokens()) {
            numbers.add(Integer.parseInt(stringTokenizer.nextToken()));
        }
        s = bufferedReader.readLine();
        s = bufferedReader.readLine();
        int[][] board = new int[5][5];
        int line = -1, column = -1;
        while (true) {
            stringTokenizer = new StringTokenizer(s, " ");
            line++;
            if (line == 5) {
                boards.add(board);
                line = -1;
                board = new int[5][5];
            }
            while(stringTokenizer.hasMoreTokens()) {
                column++;
                board[line][column] = Integer.parseInt(stringTokenizer.nextToken());
            }
            column = -1;
            s = bufferedReader.readLine();
            if (s == null) {
                boards.add(board);
                break;
            }
        }

        for (int a : numbers) {
            ListIterator<int[][]> iterator = boards.listIterator();
            while (iterator.hasNext()) {
                int index = iterator.nextIndex();
                int[][] temp = iterator.next();
                for (int j = 0; j < 5; j++) {
                    for (int k = 0; k < 5; k++) {
                        if (temp[j][k] == a) {
                            temp[j][k] = -1;
                            if (bingo(index, j, k, a)) {
                                iterator.remove();
                            }
                        }
                    }
                }
            }
        }
        int sum = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (winner[i][j] != -1) {
                    sum += winner[i][j];
                }
            }
        }
        System.out.println(sum * winning_nr);
    }
}
