import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Part1 {
    private static int countXmas(char[][] grid) {
        String word = "XMAS";
        int[][] directions = {
            {-1, 0}, {1, 0}, {0, -1}, {0, 1},
            {-1, -1}, {-1, 1}, {1, -1}, {1, 1}
        };
        int count = 0;

        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                for (int[] dir : directions) {
                    if (valid(grid, r, c, dir[0], dir[1], word)) {
                        count++;
                    }
                }
            }
        }

        return count;
    }

    private static boolean valid(char[][] grid, int r, int c, int dr, int dc, String word) {
        for (int i = 0; i < word.length(); i++) {
            int nr = r + dr * i;
            int nc = c + dc * i;
            if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length) {
                return false;
            }
            if (grid[nr][nc] != word.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        List<String> lines = Files.readAllLines(Paths.get("input.txt"));
        char[][] grid = new char[lines.size()][];
        for (int i = 0; i < lines.size(); i++) {
            grid[i] = lines.get(i).toCharArray();
        }

        System.out.println(countXmas(grid));
    }
}
