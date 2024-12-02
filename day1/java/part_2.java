import java.io.*;
import java.util.*;

public class part_2 {
    public static void main(String[] args) throws IOException {
        String inputFile = "input.txt";

        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile))) {
            String line;
            List<Integer> leftList = new ArrayList<>();
            List<Integer> rightList = new ArrayList<>();

            while ((line = reader.readLine()) != null) {
                String[] numbers = line.split(" ");
                leftList.add(Integer.parseInt(numbers[0]));
                rightList.add(Integer.parseInt(numbers[1]));
            }

            Map<Integer, Integer> rightCounts = new HashMap<>();
            for (int num : rightList) {
                rightCounts.put(num, rightCounts.getOrDefault(num, 0) + 1);
            }

            int similarityScore = 0;
            for (int num : leftList) {
                similarityScore += num * rightCounts.getOrDefault(num, 0);
            }

            System.out.println(similarityScore);
        }
    }
}
