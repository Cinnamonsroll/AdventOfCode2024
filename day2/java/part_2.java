import java.io.*;
import java.util.*;

public class part_2 {
    public static boolean isSafeReport(List<Integer> report) {
        List<Integer> differences = new ArrayList<>();
        for (int i = 1; i < report.size(); i++) {
            differences.add(report.get(i) - report.get(i - 1));
        }

        boolean allIncreasing = differences.stream().allMatch(diff -> diff >= 1 && diff <= 3);
        boolean allDecreasing = differences.stream().allMatch(diff -> diff <= -1 && diff >= -3);

        return allIncreasing || allDecreasing;
    }

    public static boolean canBeMadeSafe(List<Integer> report) {
        for (int i = 0; i < report.size(); i++) {
            List<Integer> modifiedReport = new ArrayList<>(report);
            modifiedReport.remove(i);
            if (isSafeReport(modifiedReport)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        String inputFile = "input.txt";

        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile))) {
            String line;
            int safeCount = 0;

            while ((line = reader.readLine()) != null) {
                String[] numbers = line.split(" ");
                List<Integer> report = new ArrayList<>();
                for (String num : numbers) {
                    report.add(Integer.parseInt(num));
                }

                if (isSafeReport(report) || canBeMadeSafe(report)) {
                    safeCount++;
                }
            }

            System.out.println(safeCount);
        }
    }
}
