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
        for i in 0..(1 << (2 * ops_count)) {
            if found {
                break;
            }
            let mut result = numbers[0];
            let mut valid = true;
            for j in 0..ops_count {
                if !valid {
                    break;
                }
                let op = (i >> (2 * j)) & 3;
                match op {
                    0 => result += numbers[j + 1],
                    1 => result -= numbers[j + 1],
                    2 => result *= numbers[j + 1],
                    3 => {
                        if numbers[j + 1] == 0 || result % numbers[j + 1] != 0 {
                            valid = false;
                        } else {
                            result /= numbers[j + 1];
                        }
                    }
                    _ => unreachable!(),
                }
            }
            if valid && result == test_value {
                total += test_value;
                found = true;
            }
        }
    }

    println!("{}", total);
}
