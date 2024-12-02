use std::collections::HashMap;
use std::fs;

fn main() {
    let input_file = "input.txt";
    let contents = fs::read_to_string(input_file).unwrap();
    let lines: Vec<&str> = contents.lines().collect();

    let mut left_list = Vec::new();
    let mut right_list = Vec::new();

    for line in lines {
        let numbers: Vec<i32> = line.split_whitespace().map(|n| n.parse().unwrap()).collect();
        left_list.push(numbers[0]);
        right_list.push(numbers[1]);
    }

    let mut right_counts = HashMap::new();
    for &num in &right_list {
        *right_counts.entry(num).or_insert(0) += 1;
    }

    let similarity_score: i32 = left_list.iter()
        .map(|&num| num * right_counts.get(&num).unwrap_or(&0))
        .sum();

    println!("{}", similarity_score);
}
