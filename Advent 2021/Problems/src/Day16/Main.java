package Day16;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;

public class Main {

    static int bin_to_dec(String s) {
        int pow_2 = s.length() - 1;
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                total += Math.pow(2, pow_2 - i);
            }
        }
        return total;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day16/input.txt"));
        HashMap<Character, String> map = new HashMap<>();
        int version_sum = 0;
        map.put('0', "0000");
        map.put('1', "0001");
        map.put('2', "0010");
        map.put('3', "0011");
        map.put('4', "0100");
        map.put('5', "0101");
        map.put('6', "0110");
        map.put('7', "0111");
        map.put('8', "1000");
        map.put('9', "1001");
        map.put('A', "1010");
        map.put('B', "1011");
        map.put('C', "1100");
        map.put('D', "1101");
        map.put('E', "1110");
        map.put('F', "1111");
        String s = bufferedReader.readLine();
        String x = map.get(s.charAt(0));
        int i = 1;
        int id;
        while (i < s.length()) {
            while (x.length() < 6) {
                x = x.concat(map.get(s.charAt(i)));
                i++;
                if (i == s.length()) {
                    break;
                }
            }
            version_sum += bin_to_dec(x.substring(0, 3));
            id = bin_to_dec(x.substring(3, 6));
            x = x.substring(6);
            if (id == 4) {
                char finish;
                do {
                    if (x.length() == 0) {
                        x = map.get(s.charAt(i));
                        i++;
                    }
                    finish = x.charAt(0);
                    x = x.substring(1);
                    if (x.length() <= 4) {
                        x = x.concat(map.get(s.charAt(i)));
                        i++;
                    }
                    x = x.substring(4);
                } while (finish != '0');
            } else {
                if (x.length() == 0) {
                    x = x.concat(map.get(s.charAt(i)));
                    i++;
                }
                char type = x.charAt(0);
                x = x.substring(1);
                int dim = type == '1' ? 11 : 15;
                while (x.length() < dim) {
                    x = x.concat(map.get(s.charAt(i)));
                    i++;
                }
                x = x.substring(dim);
            }
        }
        System.out.println(version_sum);
    }
}