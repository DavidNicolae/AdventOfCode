package Day17;

public class Main {
    public static void main(String[] args) throws Exception {
        int x1 = 244, x2 = 303, y1 = -91, y2 = -54;
        int max_y = Math.abs(Math.min(y1, y2)) - 1;
        int total_y = (max_y + 1) * max_y / 2;
        System.out.println(total_y);
    }
}
