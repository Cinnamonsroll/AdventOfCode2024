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

    left_list.sort();
    right_list.sort();

    let total_distance: i32 = left_list.iter()
        .zip(right_list.iter())
        .map(|(l, r)| (l - r).abs())
        .sum();

    println!("{}", total_distance);
}
