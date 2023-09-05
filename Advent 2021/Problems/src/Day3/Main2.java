package Day3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Main2 {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day3/input.txt"));
        int[] ones = new int[12], zeros = new int[12], ones2 = new int[12], zeros2 = new int[12];
        int o2_val = 0, co2_val = 0;
        ArrayList<String> o2 = new ArrayList<>(), co2 = new ArrayList<>();
        for (int i = 0; i < 1000; i++) {
            String s = bufferedReader.readLine();
            o2.add(s);
            co2.add(s);
            for (int j = 0; j < 12; j++) {
                if (s.charAt(j) == '1') {
                    ones[j]++;
                    ones2[j]++;
                } else {
                    zeros[j]++;
                    zeros2[j]++;
                }
            }
        }
        String s;
        for (int i = 0; i < 12; i++) {
            if (o2.size() == 1) {
                break;
            }
            if (ones[i] >= zeros[i]) {
                for (int j = 0; j < o2.size(); j++) {
                    if (o2.get(j).charAt(i) == '0') {
                        s = o2.remove(j);
                        j--;
                        for (int k = 0; k < s.length(); k++) {
                            if (s.charAt(k) == '1') {
                                ones[k]--;
                            } else {
                                zeros[k]--;
                            }
                        }
                    }
                }
            } else {
                for (int j = 0; j < o2.size(); j++) {
                    if (o2.get(j).charAt(i) == '1') {
                        s = o2.remove(j);
                        j--;
                        for (int k = 0; k < s.length(); k++) {
                            if (s.charAt(k) == '1') {
                                ones[k]--;
                            } else {
                                zeros[k]--;
                            }
                        }
                    }
                }
            }
        }

        for (int i = 0; i < 12; i++) {
            if (co2.size() == 1) {
                break;
            }
            if (zeros2[i] <= ones2[i]) {
                for (int j = 0; j < co2.size(); j++) {
                    if (co2.get(j).charAt(i) == '1') {
                        s = co2.remove(j);
                        j--;
                        for (int k = 0; k < s.length(); k++) {
                            if (s.charAt(k) == '1') {
                                ones2[k]--;
                            } else {
                                zeros2[k]--;
                            }
                        }
                    }
                }
            } else {
                for (int j = 0; j < co2.size(); j++) {
                    if (co2.get(j).charAt(i) == '0') {
                        s = co2.remove(j);
                        j--;
                        for (int k = 0; k < s.length(); k++) {
                            if (s.charAt(k) == '1') {
                                ones2[k]--;
                            } else {
                                zeros2[k]--;
                            }
                        }
                    }
                }
            }
        }

        for (int i = 0; i < 12; i++) {
            if (o2.get(0).charAt(i) == '1') {
                o2_val += Math.pow(2, 12 - i - 1);
            }
            if (co2.get(0).charAt(i) == '1') {
                co2_val += Math.pow(2, 12 - i - 1);
            }
        }
        System.out.println(o2_val * co2_val);
    }
}
