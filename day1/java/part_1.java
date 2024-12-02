import java.io.*;
import java.util.*;

public class part_1 {
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

            Collections.sort(leftList);
            Collections.sort(rightList);

            int totalDistance = 0;
            for (int i = 0; i < leftList.size(); i++) {
                totalDistance += Math.abs(leftList.get(i) - rightList.get(i));
            }

            System.out.println(totalDistance);
        }
    }
}
