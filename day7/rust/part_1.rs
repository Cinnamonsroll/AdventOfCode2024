use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").unwrap();
    let mut total = 0;

    for line in contents.lines() {
        let parts: Vec<&str> = line.split(':').collect();
        let test_value: i32 = parts[0].parse().unwrap();
        let numbers: Vec<i32> = parts[1]
            .trim()
            .split_whitespace()
            .map(|n| n.parse().unwrap())
            .collect();

        let ops_count = numbers.len() - 1;
        let mut found = false;
        for i in 0..(1 << ops_count) {
            if found {
                break;
            }
            let mut result = numbers[0];
            for j in 0..ops_count {
                if (i >> j) & 1 == 0 {
                    result += numbers[j + 1];
                } else {
                    result *= numbers[j + 1];
                }
            }
            if result == test_value {
                total += test_value;
                found = true;
            }
        }
    }

    println!("{}", total);
}
