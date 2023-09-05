package Day14;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day14/input.txt"));
        HashMap<String, Character> template = new HashMap<>();
        HashMap<String, Long> map = new HashMap<>();
        HashMap<Character, Long> occ = new HashMap<>();
        int steps = 40; // 10 for a) and 40 for b)
        long max = Long.MIN_VALUE, min = Long.MAX_VALUE;
        String polymer = bufferedReader.readLine();
        String s;
        bufferedReader.readLine();
        while ((s = bufferedReader.readLine()) != null) {
            StringTokenizer stringTokenizer = new StringTokenizer(s, "- >");
            template.put(stringTokenizer.nextToken(), stringTokenizer.nextToken().charAt(0));
        }
        int i;
        for (i = 0; i < polymer.length() - 1; i++) {
            if (occ.containsKey(polymer.charAt(i))) {
                occ.put(polymer.charAt(i), occ.get(polymer.charAt(i)) + 1);
            } else {
                occ.put(polymer.charAt(i), 1L);
            }
            if (map.containsKey(polymer.substring(i, i + 2))) {
                map.put(polymer.substring(i, i + 2), map.get(polymer.substring(i, i + 2)) + 1);
            } else {
                map.put(polymer.substring(i, i + 2), 1L);
            }
        }
        if (occ.containsKey(polymer.charAt(i))) {
            occ.put(polymer.charAt(i), occ.get(polymer.charAt(i)) + 1);
        } else {
            occ.put(polymer.charAt(i), 1L);
        }
        for (i = 0; i < steps; i++) {
            HashMap<String, Long> new_map = new HashMap<>();
            for (String key : map.keySet()) {
                if (occ.containsKey(template.get(key))) {
                    occ.put(template.get(key), occ.get(template.get(key)) + map.get(key));
                } else {
                    occ.put(template.get(key), map.get(key));
                }
                if (new_map.containsKey("" + template.get(key) + key.charAt(1))) {
                    new_map.put("" + template.get(key) + key.charAt(1), new_map.get("" + template.get(key) + key.charAt(1)) + map.get(key));
                } else {
                    new_map.put("" + template.get(key) + key.charAt(1), map.get(key));
                }
                if (new_map.containsKey("" + key.charAt(0) + template.get(key))) {
                    new_map.put("" + key.charAt(0) + template.get(key), new_map.get("" + key.charAt(0) + template.get(key)) + map.get(key));
                } else {
                    new_map.put("" + key.charAt(0) + template.get(key), map.get(key));
                }
            }
            map = new_map;
        }
        for (Character key : occ.keySet()) {
            if (occ.get(key) > max) {
                max = occ.get(key);
            }
            if (occ.get(key) < min) {
                min = occ.get(key);
            }
        }
        System.out.println(max - min);
    }
}
