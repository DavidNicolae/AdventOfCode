package Day10;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Stack;

public class Main2 {

    static boolean is_opener(Character c) {
        return c == '(' || c == '{' || c == '[' || c == '<';
    }

    static int get_score(Character c) {
        if (c == ')') {
            return 1;
        }
        if (c == ']') {
            return 2;
        }
        if (c == '}') {
            return 3;
        }
        return 4;
    }
    public static void main(String[] args) throws Exception {
        HashMap<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
        map.put('<', '>');
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day10/input.txt"));
        String s;
        ArrayList<Long> scores = new ArrayList<>();
        while ((s = bufferedReader.readLine()) != null) {
            long score = 0;
            Stack<Character> stack = new Stack<>();
            boolean valid_line = true;
            int i;
            for (i = 0; i < s.length(); i++) {
                if (is_opener(s.charAt(i))) {
                    stack.add(s.charAt(i));
                } else {
                    if (stack.empty()) {
                        valid_line = false;
                        break;
                    }
                    Character last = stack.pop();
                    if (map.get(last) != s.charAt(i)) {
                        valid_line = false;
                        break;
                    }
                }
            }
            if (valid_line) {
                while (!stack.empty()) {
                    Character last = stack.pop();
                    score = score * 5 + get_score(map.get(last));
                }
                scores.add(score);
            }
        }
        scores.sort((Comparator.comparingLong(o -> o)));
        System.out.println(scores.get(scores.size() / 2));
    }
}
