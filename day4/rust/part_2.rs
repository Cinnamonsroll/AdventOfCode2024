use std::fs::read_to_string;

fn count_xmas(grid: &Vec<Vec<char>>) -> i32 {
    let rows = grid.len();
    let cols = grid[0].len();
    let mut ret = 0;

    fn check_xmas_x_shape(grid: &Vec<Vec<char>>, x: usize, y: usize) -> bool {
        if grid[x][y] != 'A' {
            return false;
        }

        let top_left = format!("{}{}", 
            grid[x-1][y-1], grid[x+1][y+1]);
        let top_right = format!("{}{}", 
            grid[x-1][y+1], grid[x+1][y-1]);

        (top_left == "MS" || top_left == "SM") && 
        (top_right == "MS" || top_right == "SM")
    }

    for x in 1..rows-1 {
        for y in 1..cols-1 {
            if check_xmas_x_shape(grid, x, y) {
                ret += 1;
            }
        }
    }

    ret
}

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let grid: Vec<Vec<char>> = input
        .lines()
        .map(|line| line.chars().collect())
        .collect();

    println!("{}", count_xmas(&grid));
}
