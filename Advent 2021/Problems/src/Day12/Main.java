package Day12;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static int paths = 0;
    public static HashMap<String, ArrayList<String>> adjacency_list = new HashMap<>();

    static void find_paths(String start ,ArrayList<String> visited, ArrayList<String> path) {
        if (start.equals("end")) {
            paths++;
            System.out.println(path);
            return;
        }
        if (start.charAt(0) > 90) {
            visited.add(start);
        }

        for (String next : adjacency_list.get(start)) {
            if (!visited.contains(next)) {
                ArrayList<String> new_path = new ArrayList<>(path);
                new_path.add(next);
                ArrayList<String> new_visited = new ArrayList<>(visited);
                find_paths(next, new_visited, new_path);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("src/Day12/input.txt"));
        String s;

        while ((s = bufferedReader.readLine()) != null) {
            StringTokenizer stringTokenizer = new StringTokenizer(s, "-");
            String first, second;
            first = stringTokenizer.nextToken();
            second = stringTokenizer.nextToken();
            if (!adjacency_list.containsKey(first)) {
                ArrayList<String> adj = new ArrayList<>();
                adj.add(second);
                adjacency_list.put(first, adj);
            } else {
                adjacency_list.get(first).add(second);
            }
            if (!second.equals("end") && !first.equals("start")) {
                if (!adjacency_list.containsKey(second)) {
                    ArrayList<String> adj = new ArrayList<>();
                    adj.add(first);
                    adjacency_list.put(second, adj);
                } else {
                    adjacency_list.get(second).add(first);
                }
            }
        }
        System.out.println(adjacency_list);
//        for (String start : adjacency_list.get("start")) {
//            ArrayList<String> visited = new ArrayList<>();
//            find_paths(start, visited);
//        }
        ArrayList<String> visited = new ArrayList<>();
        ArrayList<String> path = new ArrayList<>();
        path.add("start");
        find_paths("start", visited, path);
        System.out.println(paths);
    }
}
