use std::collections::{HashMap, HashSet};
use std::fs::read_to_string;

type Rule = (i32, i32);
type Update = Vec<i32>;

fn parse_input(file_path: &str) -> (Vec<Rule>, Vec<Update>) {
    let content = read_to_string(file_path).unwrap();
    let mut rules = Vec::new();
    let mut updates = Vec::new();
    let mut section = 0;

    for line in content.lines() {
        let line = line.trim();
        if line.is_empty() {
            section += 1;
            continue;
        }

        if section == 0 {
            let parts: Vec<i32> = line.split('|')
                .map(|s| s.parse().unwrap())
                .collect();
            rules.push((parts[0], parts[1]));
        } else {
            let update: Vec<i32> = line.split(',')
                .map(|s| s.parse().unwrap())
                .collect();
            updates.push(update);
        }
    }

    (rules, updates)
}

fn sort_update(update: &[i32], rules: &[Rule]) -> Vec<i32> {
    let mut dependencies: HashMap<i32, HashSet<i32>> = update.iter()
        .map(|&page| (page, HashSet::new()))
        .collect();

    for &(a, b) in rules {
        if dependencies.contains_key(&a) && dependencies.contains_key(&b) {
            dependencies.get_mut(&b).unwrap().insert(a);
        }
    }

    let mut sorted_update = Vec::new();
    let mut visited = HashSet::new();

    fn dfs(
        page: i32,
        visited: &mut HashSet<i32>,
        dependencies: &HashMap<i32, HashSet<i32>>,
        sorted_update: &mut Vec<i32>,
    ) {
        if visited.contains(&page) {
            return;
        }
        visited.insert(page);
        for &dep in dependencies.get(&page).unwrap() {
            dfs(dep, visited, dependencies, sorted_update);
        }
        sorted_update.push(page);
    }

    for &page in update {
        dfs(page, &mut visited, &dependencies, &mut sorted_update);
    }

    sorted_update
}

fn main() {
    let (rules, updates) = parse_input("input.txt");
    let total: i32 = updates.iter()
        .map(|update| sort_update(update, &rules))
        .map(|sorted| sorted[sorted.len() / 2])
        .sum();

    println!("{}", total);
}
