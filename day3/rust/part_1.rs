use std::fs;

fn main() {
    
    let memory = fs::read_to_string("input.txt").expect("Unable to read file");

    
    let regex = regex::Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

    let mut result = 0;

    
    for cap in regex.captures_iter(&memory) {
        let x: i32 = cap[1].parse().unwrap();
        let y: i32 = cap[2].parse().unwrap();
        result += x * y;
    }

    println!("{}", result);
}
