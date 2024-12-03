import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.regex.*;

public class part_1 {
    public static void main(String[] args) {
        try {
            String memory = new String(Files.readAllBytes(Paths.get("input.txt")));

            Pattern pattern = Pattern.compile("mul\\((\\d+),(\\d+)\\)");
            Matcher matcher = pattern.matcher(memory);

            int result = 0;

            while (matcher.find()) {
                int x = Integer.parseInt(matcher.group(1));
                int y = Integer.parseInt(matcher.group(2));
                result += x * y;
            }

            System.out.println(result);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
