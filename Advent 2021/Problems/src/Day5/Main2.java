package Day5;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;

public class Main2 {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new FileReader("src/Day5/input.txt"));
        String s;
        int x1, x2, y1, y2;
        Map<String, Integer> map = new TreeMap<>();
        while ((s = reader.readLine()) != null) {
            StringTokenizer stringTokenizer = new StringTokenizer(s, ", ->");
            x1 = Integer.parseInt(stringTokenizer.nextToken());
            y1 = Integer.parseInt(stringTokenizer.nextToken());
            x2 = Integer.parseInt(stringTokenizer.nextToken());
            y2 = Integer.parseInt(stringTokenizer.nextToken());
            if (x1 == x2) {
                if (y1 < y2) {
                    for (int i = y1; i <= y2; i++) {
                        String key = x1 + " " + i;
                        if (map.containsKey(key)) {
                            map.replace(key, map.get(key) + 1);
                        } else {
                            map.put(key, 1);
                        }
                    }
                } else {
                    for (int i = y2; i <= y1; i++) {
                        String key = x1 + " " + i;
                        if (map.containsKey(key)) {
                            map.replace(key, map.get(key) + 1);
                        } else {
                            map.put(key, 1);
                        }
                    }
                }
            } else if (y1 == y2) {
                if (x1 < x2) {
                    for (int i = x1; i <= x2; i++) {
                        String key = i + " " + y1;
                        if (map.containsKey(key)) {
                            map.replace(key, map.get(key) + 1);
                        } else {
                            map.put(key, 1);
                        }
                    }
                } else {
                    for (int i = x2; i <= x1; i++) {
                        String key = i + " " + y1;
                        if (map.containsKey(key)) {
                            map.replace(key, map.get(key) + 1);
                        } else {
                            map.put(key, 1);
                        }
                    }
                }
            } else {
                int start_x;
                int start_y;
                int end_x;
                int end_y;
                if (x1 < x2) {
                    start_x = x1;
                    start_y = y1;
                    end_x = x2;
                    end_y = y2;
                } else {
                    start_x = x2;
                    start_y = y2;
                    end_x = x1;
                    end_y = y1;
                }
                if (start_y <= end_y) {
                    while (start_y <= end_y) {
                        String key = start_x + " " + start_y;
                        if (map.containsKey(key)) {
                            map.replace(key, map.get(key) + 1);
                        } else {
                            map.put(key, 1);
                        }
                        start_x++;
                        start_y++;
                    }
                } else {
                    while (start_y >= end_y) {
                        String key = start_x + " " + start_y;
                        if (map.containsKey(key)) {
                            map.replace(key, map.get(key) + 1);
                        } else {
                            map.put(key, 1);
                        }
                        start_x++;
                        start_y--;
                    }
                }
            }
        }
        int counter = 0;
        for (String key : map.keySet()) {
            if (map.get(key) > 1) {
                counter++;
            }
        }
        System.out.println(counter);
    }
}
