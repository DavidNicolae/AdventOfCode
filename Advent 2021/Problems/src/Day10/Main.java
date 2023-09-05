package Day10;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Stack;

public class Main {

    static boolean is_opener(Character c) {
        return c == '(' || c == '{' || c == '[' || c == '<';
    }

    static int get_score(Character c) {
        if (c == ')') {
            return 3;
        }
        if (c == ']') {
            return 57;
        }
        if (c == '}') {
            return 1197;
        }
        return 25137;
    }
    public static void main(String[] args) throws Exception {
        HashMap<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
        map.put('<', '>');
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day10/input.txt"));
        String s;
        int score = 0;
        while ((s = bufferedReader.readLine()) != null) {
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
            if (!valid_line) {
                score += get_score(s.charAt(i));
            }
        }
        System.out.println(score);
    }
}
