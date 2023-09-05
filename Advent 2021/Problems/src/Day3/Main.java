package Day3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day3/input.txt"));
        int[] ones = new int[12], zeros = new int[12], gamma = new int[12], epsilon = new int[12];
        int gamma_rate = 0, epsilon_rate = 0;
        for (int i = 0; i < 1000; i++) {
            String s = bufferedReader.readLine();
            for (int j = 0; j < 12; j++) {
                if (s.charAt(j) == '1') {
                    ones[j]++;
                } else {
                    zeros[j]++;
                }
            }
        }
        for (int i = 0; i < 12; i++) {
            if (ones[i] > zeros[i]) {
                gamma[i] = 1;
            } else {
                epsilon[i] = 1;
            }
        }
        for (int i = 0; i < 12; i++) {
            if (gamma[i] == 1) {
                gamma_rate += Math.pow(2, 12 - i - 1);
            }
            if (epsilon[i] == 1) {
                epsilon_rate += Math.pow(2, 12 - i - 1);
            }
        }
        System.out.println(gamma_rate * epsilon_rate);
    }
}
