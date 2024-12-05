use std::collections::HashMap;
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

fn is_update_ordered(update: &[i32], rules: &[Rule]) -> bool {
    let page_indices: HashMap<i32, usize> = update.iter()
        .enumerate()
        .map(|(i, &page)| (page, i))
        .collect();

    for &(a, b) in rules {
        if let (Some(&i1), Some(&i2)) = (page_indices.get(&a), page_indices.get(&b)) {
            if i1 > i2 {
                return false;
            }
        }
    }
    true
}

fn main() {
    let (rules, updates) = parse_input("input.txt");
    let middle_sum: i32 = updates.iter()
        .filter(|update| is_update_ordered(update, &rules))
        .map(|update| update[update.len() / 2])
        .sum();

    println!("{}", middle_sum);
}
