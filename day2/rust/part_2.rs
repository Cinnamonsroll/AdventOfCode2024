use std::fs;

fn is_safe_report(report: &[i32]) -> bool {
    let differences: Vec<i32> = report.windows(2).map(|w| w[1] - w[0]).collect();
    let all_increasing = differences.iter().all(|&diff| (1..=3).contains(&diff));
    let all_decreasing = differences.iter().all(|&diff| (-3..=-1).contains(&diff));
    all_increasing || all_decreasing
}

fn can_be_made_safe(report: &[i32]) -> bool {
    for i in 0..report.len() {
        let mut modified_report = report.to_vec();
        modified_report.remove(i);
        if is_safe_report(&modified_report) {
            return true;
        }
    }
    false
}

fn main() {
    let input_file = "input.txt";
    let contents = fs::read_to_string(input_file).unwrap();
    let lines: Vec<&str> = contents.lines().collect();

    let safe_count = lines.iter()
        .filter(|&&line| {
            let report: Vec<i32> = line.split_whitespace().map(|n| n.parse().unwrap()).collect();
            is_safe_report(&report) || can_be_made_safe(&report)
        })
        .count();

    println!("{}", safe_count);
}
