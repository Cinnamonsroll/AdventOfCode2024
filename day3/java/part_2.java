import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.regex.*;

public class part_2 {
    public static void main(String[] args) {
        try {
            String memory = new String(Files.readAllBytes(Paths.get("input.txt")));

            Pattern pattern = Pattern.compile("mul\\((\\d+),(\\d+)\\)|do\\(\\)|don't\\(\\)");
            Matcher matcher = pattern.matcher(memory);

            int result = 0;
            boolean enabled = true;

            while (matcher.find()) {
                String matched = matcher.group();

                if (matched.equals("do()")) {
                    enabled = true;
                } else if (matched.equals("don't()")) {
                    enabled = false;
                } else if (enabled && matched.startsWith("mul")) {
                    int x = Integer.parseInt(matcher.group(1));
                    int y = Integer.parseInt(matcher.group(2));
                    result += x * y;
                }
            }

            System.out.println(result);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
