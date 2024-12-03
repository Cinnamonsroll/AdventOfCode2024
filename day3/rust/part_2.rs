use std::fs;

fn main() {
    
    let memory = fs::read_to_string("input.txt").expect("Unable to read file");

    let regex = regex::Regex::new(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)").unwrap();

    let mut result = 0;
    let mut enabled = true;

    for cap in regex.captures_iter(&memory) {
        if let Some(matched) = cap.get(0) {
            if matched.as_str() == "do()" {
                enabled = true;
            } else if matched.as_str() == "don't()" {
                enabled = false;
            } else if enabled && matched.as_str().starts_with("mul") {
                let x: i32 = cap[1].parse().unwrap();
                let y: i32 = cap[2].parse().unwrap();
                result += x * y;
            }
        }
    }

    println!("{}", result);
}
