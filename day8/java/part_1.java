import java.io.*;
import java.util.*;

public class part_1 {
    public static void main(String[] args) throws IOException {
        List<String> grid = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    grid.add(line);
                }
            }
        }

        int N = grid.size();
        int M = grid.get(0).length();
        Map<Character, List<int[]>> nodes = new HashMap<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                char c = grid.get(i).charAt(j);
                if (c != '.') {
                    nodes.computeIfAbsent(c, k -> new ArrayList<>()).add(new int[]{i, j});
                }
            }
        }

        Set<String> antinodes = new HashSet<>();

        for (List<int[]> nodeList : nodes.values()) {
            int L = nodeList.size();
            for (int i = 0; i < L; i++) {
                for (int j = 0; j < i; j++) {
                    int[] node1 = nodeList.get(i);
                    int[] node2 = nodeList.get(j);
                    int x1 = node1[1], y1 = node1[0];
                    int x2 = node2[1], y2 = node2[0];
                    int newX = x2 + (x2 - x1);
                    int newY = y2 + (y2 - y1);
                    if (newX >= 0 && newX < M && newY >= 0 && newY < N) {
                        antinodes.add(newY + "," + newX);
                    }
                    x1 = node2[1]; y1 = node2[0];
                    x2 = node1[1]; y2 = node1[0];
                    newX = x2 + (x2 - x1);
                    newY = y2 + (y2 - y1);
                    if (newX >= 0 && newX < M && newY >= 0 && newY < N) {
                        antinodes.add(newY + "," + newX);
                    }
                }
            }
        }

        System.out.println(antinodes.size());
    }
}
