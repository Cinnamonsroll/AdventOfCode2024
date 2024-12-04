use std::fs::read_to_string;

fn count_xmas(grid: &Vec<Vec<char>>) -> i32 {
    let word = "XMAS";
    let directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ];
    let rows = grid.len();
    let cols = grid[0].len();
    let mut count = 0;

    fn valid(grid: &Vec<Vec<char>>, r: i32, c: i32, dr: i32, dc: i32, word: &str) -> bool {
        for (i, ch) in word.chars().enumerate() {
            let nr = r + dr * i as i32;
            let nc = c + dc * i as i32;
            if nr < 0 || nr >= grid.len() as i32 || nc < 0 || nc >= grid[0].len() as i32 {
                return false;
            }
            if grid[nr as usize][nc as usize] != ch {
                return false;
            }
        }
        true
    }

    for r in 0..rows {
        for c in 0..cols {
            for &(dr, dc) in directions.iter() {
                if valid(grid, r as i32, c as i32, dr, dc, word) {
                    count += 1;
                }
            }
        }
    }

    count
}

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let grid: Vec<Vec<char>> = input
        .lines()
        .map(|line| line.chars().collect())
        .collect();

    println!("{}", count_xmas(&grid));
}
