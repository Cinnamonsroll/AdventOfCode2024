import java.io.*;
import java.util.*;

public class part_2 {
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
            for (int i = 0; i < (1 << (2 * opsCount)) && !found; i++) {
                int result = numbers[0];
                boolean valid = true;
                for (int j = 0; j < opsCount && valid; j++) {
                    int op = (i >> (2 * j)) & 3;
                    switch (op) {
                        case 0:
                            result += numbers[j + 1];
                            break;
                        case 1:
                            result -= numbers[j + 1];
                            break;
                        case 2:
                            result *= numbers[j + 1];
                            break;
                        case 3:
                            if (numbers[j + 1] == 0 || result % numbers[j + 1] != 0) {
                                valid = false;
                            } else {
                                result /= numbers[j + 1];
                            }
                            break;
                    }
                }
                if (valid && result == testValue) {
                    total += testValue;
                    found = true;
                }
            }
        }

        System.out.println(total);
        reader.close();
    }
}
