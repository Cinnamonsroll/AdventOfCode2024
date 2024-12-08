import java.io.*;
import java.util.*;

public class part_1 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        String line;
        int total = 0;

        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(":");
            int testValue = Integer.parseInt(parts[0]);
            int[] numbers = Arrays.stream(parts[1].trim().split("\\s+"))
                                .mapToInt(Integer::parseInt)
                                .toArray();

            int opsCount = numbers.length - 1;
            boolean found = false;
            for (int i = 0; i < (1 << opsCount) && !found; i++) {
                int result = numbers[0];
                for (int j = 0; j < opsCount; j++) {
                    if (((i >> j) & 1) == 0) {
                        result += numbers[j + 1];
                    } else {
                        result *= numbers[j + 1];
                    }
                }
                if (result == testValue) {
                    total += testValue;
                    found = true;
                }
            }
        }

        System.out.println(total);
        reader.close();
    }
}
