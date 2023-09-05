package Day16;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;

class Pair {
    int type;
    long size;
    int operation;

    public Pair(int type, long size, int operation) {
         this.type = type;
         this.size = size;
         this.operation = operation;
    }
}

public class Main2 {

    static long bin_to_dec(String s) {
        int pow_2 = s.length() - 1;
        long total = 0;
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
        ArrayList<Long> packets = new ArrayList<>();
        Stack<Integer> indexes = new Stack<>();
        Stack<Pair> operations = new Stack<>();
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
            id = (int) bin_to_dec(x.substring(3, 6));
            x = x.substring(6);
            int covered = 6;
            if (id == 4) {
                char keep_reading;
                String number = "";
                do {
                    if (x.length() == 0) {
                        x = map.get(s.charAt(i));
                        i++;
                    }
                    keep_reading = x.charAt(0);
                    x = x.substring(1);
                    if (x.length() <= 4) {
                        x = x.concat(map.get(s.charAt(i)));
                        i++;
                    }
                    number = number.concat(x.substring(0, 4));
                    x = x.substring(4);
                    covered += 5;
                } while (keep_reading != '0');
                packets.add(bin_to_dec(number));
                for (Pair pair : operations) {
                    if (pair.type == 0) {
                        pair.size -= covered;
                    }
                }
                if (operations.peek().type == 1) {
                    operations.peek().size -= 1;
                }
                while (!operations.empty() && operations.peek().size == 0) {
                    Pair pair = operations.pop();
                    int index = indexes.pop();
                    ArrayList<Long> new_packets = new ArrayList<>();
                    for (int k = 0; k < index; k++) {
                        new_packets.add(packets.get(k));
                    }
                    long sum = 0, product = 1, min = Integer.MAX_VALUE, max = Integer.MIN_VALUE, gt = -1, lt = -1, eq = -1;
                    if (pair.operation == 0 || pair.operation == 1 || pair.operation == 2 || pair.operation == 3) {
                        for (int k = index; k < packets.size(); k++) {
                            long v = packets.get(k);
                            sum += v;
                            product *= v;
                            if (v < min) {
                                min = v;
                            }
                            if (v > max) {
                                max = v;
                            }
                        }
                    } else {
                        long v = packets.get(index), v1 = packets.get(index + 1);
                        if (v > v1) {
                            gt = 1;
                        } else {
                            gt = 0;
                        }
                        if (v < v1) {
                            lt = 1;
                        } else {
                            lt = 0;
                        }
                        if (v == v1) {
                            eq = 1;
                        } else {
                            eq = 0;
                        }
                    }
                    if (pair.operation == 0) {
                        new_packets.add(sum);
                    } else if (pair.operation == 1) {
                        new_packets.add(product);
                    }
                    else if (pair.operation == 2) {
                        new_packets.add(min);
                    }
                    else if (pair.operation == 3) {
                        new_packets.add(max);
                    }
                    else if (pair.operation == 5) {
                        new_packets.add(gt);
                    }
                    else if (pair.operation == 6) {
                        new_packets.add(lt);
                    }
                    else if (pair.operation == 7){
                        new_packets.add(eq);
                    }
                    packets = new_packets;
                }
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

                covered += dim + 1;
                for (Pair pair : operations) {
                    if (pair.type == 0) {
                        pair.size -= covered;
                    }
                }
                if (!operations.empty() && operations.peek().type == 1) {
                    operations.peek().size -= 1;
                }

                long value = bin_to_dec(x.substring(0, dim));
                operations.add(new Pair(Character.getNumericValue(type), value, id));
                indexes.add(packets.size());
                x = x.substring(dim);
            }
        }
        System.out.println(packets);
    }
}