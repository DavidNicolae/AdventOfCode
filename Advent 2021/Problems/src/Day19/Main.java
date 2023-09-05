package Day19;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day19/input.txt"));
        String s = bufferedReader.readLine();
        ArrayList<Beacon> first = new ArrayList<>();
        while (!(s = bufferedReader.readLine()).equals("")) {
            StringTokenizer stringTokenizer = new StringTokenizer(s, ",");
            first.add(new Beacon(Integer.parseInt(stringTokenizer.nextToken()),
                                Integer.parseInt(stringTokenizer.nextToken()),
                                Integer.parseInt(stringTokenizer.nextToken())));
        }
        for (int k = 0; k < 4; k++) {
            s = bufferedReader.readLine();
            System.out.println(s);
            ArrayList<Beacon> next = new ArrayList<>();
            while ((s = bufferedReader.readLine()) != null && !s.equals("")) {
                StringTokenizer stringTokenizer = new StringTokenizer(s, ",");
                next.add(new Beacon(Integer.parseInt(stringTokenizer.nextToken()),
                        Integer.parseInt(stringTokenizer.nextToken()),
                        Integer.parseInt(stringTokenizer.nextToken())));
            }
            for (int up = 0; up < 24; up++) {
                boolean found = false;
                HashMap<String, Integer> beacons = new HashMap<>();
                for (int i = 0; i < first.size(); i++) {
                    for (int j = 0; j < next.size(); j++) {
                        Beacon beacon = new Beacon(first.get(i), next.get(j).up(up));
                        if (!beacons.containsKey(beacon.toString())) {
                            beacons.put(beacon.toString(), 1);
                        } else {
                            beacons.put(beacon.toString(), beacons.get(beacon.toString()) + 1);
                        }
                    }
                }
                for (String s1 : beacons.keySet()) {
                    if (beacons.get(s1) >= 12) {
                        System.out.println("da");
                        found = true;
                        System.out.println(up);
                        StringTokenizer stringTokenizer = new StringTokenizer(s1, " ");
                        int x_offset = Integer.parseInt(stringTokenizer.nextToken());
                        int y_offset = Integer.parseInt(stringTokenizer.nextToken());
                        int z_offset = Integer.parseInt(stringTokenizer.nextToken());
                        for (Beacon beacon : next) {
                            Beacon temp = beacon.up(up);
                            Beacon converted = new Beacon(x_offset + temp.x, y_offset + temp.y, z_offset + temp.z);
                            boolean exists = false;
                            for (Beacon beacon1 : first) {
                                if (beacon1.equals(converted)) {
                                    System.out.println(beacon + " has been found in scanner 1");
                                    exists = true;
                                    break;
                                }
                            }
                            if (!exists) {
                                first.add(converted);
                            }
                        }
                        break;
                    }
                }
                if (found) {
                    break;
                }
            }
        }
//        System.out.println(first.size());
//        for (Beacon beacon : first) {
//            System.out.println(beacon);
//        }
        System.out.println(first.size());
    }
}
