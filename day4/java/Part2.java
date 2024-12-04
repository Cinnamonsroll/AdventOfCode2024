import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Part2 {
    private static int countXmas(char[][] grid) {
        int ret = 0;

        for (int x = 1; x < grid.length - 1; x++) {
            for (int y = 1; y < grid[0].length - 1; y++) {
                if (checkXmasXShape(grid, x, y)) {
                    ret++;
                }
            }
        }

        return ret;
    }

    private static boolean checkXmasXShape(char[][] grid, int x, int y) {
        if (grid[x][y] != 'A') {
            return false;
        }

        String topLeft = "" + grid[x-1][y-1] + grid[x+1][y+1];
        String topRight = "" + grid[x-1][y+1] + grid[x+1][y-1];

        return (topLeft.equals("MS") || topLeft.equals("SM")) &&
               (topRight.equals("MS") || topRight.equals("SM"));
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
