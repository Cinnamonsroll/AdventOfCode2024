import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class Part2 {
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

    private static List<Integer> sortUpdate(List<Integer> update, List<Rule> rules) {
        Map<Integer, Set<Integer>> dependencies = new HashMap<>();
        for (int page : update) {
            dependencies.put(page, new HashSet<>());
        }

        for (Rule rule : rules) {
            if (dependencies.containsKey(rule.a) && dependencies.containsKey(rule.b)) {
                dependencies.get(rule.b).add(rule.a);
            }
        }

        List<Integer> sortedUpdate = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();

        for (int page : update) {
            dfs(page, visited, dependencies, sortedUpdate);
        }

        return sortedUpdate;
    }

    private static void dfs(int page, Set<Integer> visited, 
                          Map<Integer, Set<Integer>> dependencies, 
                          List<Integer> sortedUpdate) {
        if (visited.contains(page)) {
            return;
        }
        visited.add(page);
        for (int dep : dependencies.get(page)) {
            dfs(dep, visited, dependencies, sortedUpdate);
        }
        sortedUpdate.add(page);
    }

    public static void main(String[] args) throws Exception {
        Input input = parseInput("input.txt");
        int total = input.updates.stream()
            .map(update -> sortUpdate(update, input.rules))
            .mapToInt(update -> update.get(update.size() / 2))
            .sum();

        System.out.println(total);
    }
}
