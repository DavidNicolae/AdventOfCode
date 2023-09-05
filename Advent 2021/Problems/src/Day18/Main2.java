package Day18;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main2 {

    public static int calculate_sum(String sum) {
        boolean finished = false;
        while (!finished) {
            int i = 0;
            while (i < sum.length()) {
                char c = sum.charAt(i);
                if (c == '[') {
                    int start = i, end = sum.length();
                    for (int j = i + 1; j < sum.length(); j++) {
                        if (sum.charAt(j) == '[') {
                            start = j;
                        } else if (sum.charAt(j) == ']') {
                            end = j;
                            break;
                        }
                    }
                    String sum1 = sum.substring(0, start);
                    String sum2 = sum.substring(end + 1);
                    String reduce = sum.substring(start, end + 1);
                    StringTokenizer stringTokenizer = new StringTokenizer(reduce, "[,]");
                    int a = Integer.parseInt(stringTokenizer.nextToken()), b = Integer.parseInt(stringTokenizer.nextToken());
                    int result = a * 3 + b * 2;
                    sum = sum1 + result + sum2;
                    if (!sum.contains("[")) {
                        finished = true;
                        break;
                    }
                }
                i++;
            }
        }
        return Integer.parseInt(sum);
    }

    public static String reduce_sum(String sum) {
        int nested_counter, i = 0;
        boolean more_explosions = true, more_splits = true;
        while (more_explosions || more_splits) {
            more_explosions = false;
            nested_counter = 0;
            while (i < sum.length()) {
                char c = sum.charAt(i);
                if (c == '[') {
                    nested_counter++;
                    if (nested_counter == 5) {
                        more_explosions = true;
                        int val1 = 0, j = i + 1;
                        while (sum.charAt(j) != ',') {
                            val1 = val1 * 10 + Character.getNumericValue(sum.charAt(j));
                            j++;
                        }
                        j++;
                        int val2 = 0;
                        while (sum.charAt(j) != ']') {
                            val2 = val2 * 10 + Character.getNumericValue(sum.charAt(j));
                            j++;
                        }
                        j++;
                        String sum1 = sum.substring(0, i);
                        String sum2 = sum.substring(j);
                        int val11 = 0, p = 1, inc = 0;
                        boolean found = false;
                        for (j = sum1.length() - 1; j >= 0; j--) {
                            if (sum1.charAt(j) != ']' && sum1.charAt(j) != '[' && sum1.charAt(j) != ',') {
                                found = true;
                                val11 = val11 + Character.getNumericValue(sum1.charAt(j)) * p;
                                p *= 10;
                                inc++;
                            } else if (found) {
                                String sum11 = sum1.substring(0, j + 1), sum12 = sum1.substring(j + 1 + inc);
                                val11 += val1;
                                sum1 = sum11 + val11 + sum12;
                                break;
                            }
                        }
                        int val22 = 0;
                        inc = 0;
                        found = false;
                        for (j = 0; j <= sum2.length() - 1; j++) {
                            if (sum2.charAt(j) != ']' && sum2.charAt(j) != '[' && sum2.charAt(j) != ',') {
                                found = true;
                                val22 = val22 * 10 + Character.getNumericValue(sum2.charAt(j));
                                inc++;
                            } else if (found) {
                                String sum21 = sum2.substring(0, j - inc), sum22 = sum2.substring(j);
                                val22 += val2;
                                sum2 = sum21 + val22 + sum22;
                                break;
                            }
                        }
                        sum = sum1 + 0 + sum2;
                        i = -1;
                        nested_counter = 0;
                    }
                } else if (c == ']') {
                    nested_counter--;
                }
                i++;
            }
            more_splits = false;
            i = 0;
            while (i < sum.length()) {
                char c = sum.charAt(i);
                if (c != ',' && c != '[' && c != ']' && sum.charAt(i + 1) != ',' && sum.charAt(i + 1) != '[' && sum.charAt(i + 1) != ']') {
                    more_splits = true;
                    int val = 0, j = i;
                    while (sum.charAt(j) != ',' && sum.charAt(j) != '[' && sum.charAt(j) != ']') {
                        val = val * 10 + Character.getNumericValue(sum.charAt(j));
                        j++;
                    }
                    int val1 = val / 2;
                    int val2 = val - val1;
                    String sum1 = sum.substring(0, i);
                    String sum2 = sum.substring(j);
                    String new_pair = "[" + val1 + "," + val2 + "]";
                    sum = sum1 + new_pair + sum2;
                    i = 0;
                    break;
                }
                i++;
            }
        }
        return sum;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day18/input.txt"));
        String s;
        ArrayList<String> numbers = new ArrayList<>();
        ArrayList<String> sums = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        while ((s = bufferedReader.readLine()) != null) {
            numbers.add(s);
        }
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = 0; j < numbers.size(); j++) {
                sums.add(reduce_sum("[" + numbers.get(i) + "," + numbers.get(j) + "]"));
            }
        }
        for (int i = 0; i < sums.size(); i++) {
            int sum = calculate_sum(sums.get(i));
            if (sum > max) {
                max = sum;
            }
        }
        System.out.println(max);
    }
}
