package Day8;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;

public class Main2 {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day8/input.txt"));
        HashMap<Integer, ArrayList<Character>> decoder;
        int[] numbers = new int[] {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        ArrayList<String> inputs, outputs;
        String s;
        long total = 0;
        while ((s = bufferedReader.readLine()) != null) {
            decoder = new HashMap<>();
            for (int i = 1; i < 8; i++) {
                decoder.put(i, new ArrayList<>());
            }
            inputs = new ArrayList<>();
            outputs = new ArrayList<>();

            StringTokenizer stringTokenizer = new StringTokenizer(s, "|");
            String input = stringTokenizer.nextToken();
            String output = stringTokenizer.nextToken();
            StringTokenizer stringTokenizer1 = new StringTokenizer(input, " ");
            while(stringTokenizer1.hasMoreTokens()) {
                inputs.add(stringTokenizer1.nextToken());
            }
            inputs.sort(Comparator.comparingInt(String::length));
            stringTokenizer1 = new StringTokenizer(output, " ");
            while (stringTokenizer1.hasMoreTokens()) {
                outputs.add(stringTokenizer1.nextToken());
            }

            for (int i = 0; i < 3; i++) {
                if (inputs.get(0).indexOf(inputs.get(1).charAt(i)) != -1) {
                    decoder.get(3).add(inputs.get(1).charAt(i));
                    decoder.get(6).add(inputs.get(1).charAt(i));
                } else {
                    decoder.get(1).add(inputs.get(1).charAt(i));
                }
            }
            for (int i = 0; i < 4; i++) {
                if (!decoder.get(3).contains(inputs.get(2).charAt(i))) {
                    decoder.get(2).add(inputs.get(2).charAt(i));
                    decoder.get(4).add(inputs.get(2).charAt(i));
                }
            }
            for (int i = 0; i < 7; i++) {
                if (!decoder.get(1).contains(inputs.get(9).charAt(i)) &&
                    !decoder.get(2).contains(inputs.get(9).charAt(i)) &&
                    !decoder.get(3).contains(inputs.get(9).charAt(i)) &&
                    !decoder.get(4).contains(inputs.get(9).charAt(i))) {
                    decoder.get(5).add(inputs.get(9).charAt(i));
                    decoder.get(7).add(inputs.get(9).charAt(i));
                }
            }
            for (int i = 3; i < 6; i++) {
                String temp = inputs.get(i);
                if (temp.indexOf(decoder.get(3).get(0)) != -1 && temp.indexOf(decoder.get(3).get(1)) != -1) {
                    Character c2 = ' ', c4 = ' ', c5 = ' ', c7 = ' ';
                    for (int j = 0; j < 2; j++) {
                        if (temp.indexOf(decoder.get(4).get(j)) == -1) {
                            c4 = decoder.get(4).get(j);
                        } else {
                            c2 = decoder.get(2).get(j);
                        }
                        if (temp.indexOf(decoder.get(7).get(j)) == -1) {
                            c7 = decoder.get(7).get(j);
                        } else {
                            c5 = decoder.get(5).get(j);
                        }
                    }
                    decoder.get(4).remove(c4);
                    decoder.get(2).remove(c2);
                    decoder.get(7).remove(c7);
                    decoder.get(5).remove(c5);
                    break;
                }
            }
            for (int i = 3; i < 6; i++) {
                String temp = inputs.get(i);
                if (temp.indexOf(decoder.get(2).get(0)) != -1) {
                    Character c3 = ' ', c6 = ' ';
                    for (int j = 0; j < 2; j++) {
                        if (temp.indexOf(decoder.get(3).get(j)) != -1) {
                            c3 = decoder.get(3).get(j);
                        } else {
                            c6 = decoder.get(6).get(j);
                        }
                    }
                    decoder.get(3).remove(c3);
                    decoder.get(6).remove(c6);
                    break;
                }
            }
            String zero, one, two, three, four, five, six, seven, eight, nine;
            ArrayList<String> answers = new ArrayList<>();
            one = "" + decoder.get(3).get(0) + decoder.get(6).get(0);
            two = "" + decoder.get(1).get(0) + decoder.get(3).get(0) + decoder.get(4).get(0) + decoder.get(5).get(0) + decoder.get(7).get(0);
            three = "" + decoder.get(1).get(0) + decoder.get(3).get(0) + decoder.get(4).get(0) + decoder.get(6).get(0) + decoder.get(7).get(0);
            four = "" + decoder.get(2).get(0) + decoder.get(3).get(0) + decoder.get(4).get(0) + decoder.get(6).get(0);
            five = "" + decoder.get(1).get(0) + decoder.get(2).get(0) + decoder.get(4).get(0) + decoder.get(6).get(0) + decoder.get(7).get(0);
            six = "" + decoder.get(1).get(0) + decoder.get(2).get(0) + decoder.get(4).get(0) + decoder.get(5).get(0) + decoder.get(6).get(0) + decoder.get(7).get(0);
            seven = one + decoder.get(1).get(0);
            eight = six + decoder.get(3).get(0);
            nine = "" + decoder.get(1).get(0) + decoder.get(2).get(0) + decoder.get(3).get(0) + decoder.get(4).get(0) + decoder.get(6).get(0) + decoder.get(7).get(0);
            zero = "" + decoder.get(1).get(0) + decoder.get(2).get(0) + decoder.get(3).get(0) + decoder.get(5).get(0) + decoder.get(6).get(0) + decoder.get(7).get(0);

            answers.add(zero);
            answers.add(one);
            answers.add(two);
            answers.add(three);
            answers.add(four);
            answers.add(five);
            answers.add(six);
            answers.add(seven);
            answers.add(eight);
            answers.add(nine);

            long nr = 0, c = 1000;
            for (String o : outputs) {
                boolean done = false;
                for (int k = 0; k < answers.size(); k++) {
                    boolean found = true;
                    if (o.length() == answers.get(k).length()) {
                        for (int i = 0; i < answers.get(k).length(); i++) {
                            if (o.indexOf(answers.get(k).charAt(i)) == -1) {
                                found = false;
                                break;
                            }
                        }
                        if (found) {
                            nr += numbers[k] * c;
                            c /= 10;
                            done = true;
                        }
                    }
                    if (done) {
                        break;
                    }
                }
            }
            total += nr;
        }
        System.out.println(total);
    }
}
