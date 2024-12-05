import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class Part1 {
    private static class Rule {
        int a, b;
        Rule(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    private static class Input {
        List<Rule> rules;
        List<List<Integer>> updates;

        Input(List<Rule> rules, List<List<Integer>> updates) {
            this.rules = rules;
            this.updates = updates;
        }
    }

    private static Input parseInput(String filePath) throws Exception {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        List<Rule> rules = new ArrayList<>();
        List<List<Integer>> updates = new ArrayList<>();
        int section = 0;

        for (String line : lines) {
            line = line.trim();
            if (line.isEmpty()) {
                section++;
                continue;
            }

            if (section == 0) {
                String[] parts = line.split("\\|");
                rules.add(new Rule(
                    Integer.parseInt(parts[0]),
                    Integer.parseInt(parts[1])
                ));
            } else {
                List<Integer> update = new ArrayList<>();
                for (String num : line.split(",")) {
                    update.add(Integer.parseInt(num));
                }
                updates.add(update);
            }
        }

        return new Input(rules, updates);
    }

    private static boolean isUpdateOrdered(List<Integer> update, List<Rule> rules) {
        Map<Integer, Integer> pageIndices = new HashMap<>();
        for (int i = 0; i < update.size(); i++) {
            pageIndices.put(update.get(i), i);
        }

        for (Rule rule : rules) {
            if (pageIndices.containsKey(rule.a) && pageIndices.containsKey(rule.b)) {
                if (pageIndices.get(rule.a) > pageIndices.get(rule.b)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        Input input = parseInput("input.txt");
        int middleSum = input.updates.stream()
            .filter(update -> isUpdateOrdered(update, input.rules))
            .mapToInt(update -> update.get(update.size() / 2))
            .sum();

        System.out.println(middleSum);
    }
}
