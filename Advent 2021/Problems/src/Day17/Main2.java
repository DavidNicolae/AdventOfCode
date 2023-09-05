package Day17;

public class Main2 {

    static int x1 = 244, x2 = 303, y1 = -91, y2 = -54;

    static boolean check(int x, int y) {
        return x >= x1 && x <= x2 && y <= y2 && y >= y1;
    }

    public static void main(String[] args) throws Exception {
        // part 1
        int max_y = Math.abs(Math.min(y1, y2)) - 1;
        int total_y = (max_y + 1) * max_y / 2;
        System.out.println(total_y);

        //part 2
        int counter = 0;
        for (int i = 0; i <= x2; i++) {
            for (int j = y1; j <= Math.abs(y1); j++) {
                int x = i, y = j, xt = i, yt = j;
                boolean y_was_0 = y <= 0;
                while (xt <= x2 && yt >= y1) {
                    if (check(xt, yt)) {
                        System.out.println(i + " " + j);
                        counter++;
                        break;
                    }
                    if (x > 0) {
                        x--;
                    }
                    xt = xt + x;
                    y--;
                    yt = yt + y;
                }
            }
        }
        System.out.println(counter);
    }
}
