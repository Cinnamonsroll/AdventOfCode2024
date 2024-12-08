import java.io.*;
import java.util.*;

public class part_2 {
    public static void main(String[] args) throws IOException {
        List<String> grid = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                grid.add(line);
            }
        }

        int N = grid.size();
        int M = grid.get(0).length();
        int startX = 0, startY = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid.get(i).charAt(j) == '^') {
                    startY = i;
                    startX = j;
                    break;
                }
            }
        }

        Set<String> visited = new HashSet<>();
        visited.add(startY + "," + startX);
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{startY, startX});
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int maxDist = 0;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int y = curr[0], x = curr[1];

            for (int[] dir : dirs) {
                int newY = y + dir[0];
                int newX = x + dir[1];
                if (newY >= 0 && newY < N && newX >= 0 && newX < M && grid.get(newY).charAt(newX) != '#') {
                    String key = newY + "," + newX;
                    if (!visited.contains(key)) {
                        visited.add(key);
                        queue.add(new int[]{newY, newX});
                        int dist = Math.abs(newY - startY) + Math.abs(newX - startX);
                        maxDist = Math.max(maxDist, dist);
                    }
                }
            }
        }

        System.out.println(maxDist);
    }
}
