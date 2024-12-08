use std::collections::{HashSet, VecDeque};
use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").unwrap();
    let grid: Vec<Vec<char>> = contents.lines().map(|line| line.chars().collect()).collect();
    let (n, m) = (grid.len(), grid[0].len());
    let (mut start_x, mut start_y) = (0, 0);

    for i in 0..n {
        for j in 0..m {
            if grid[i][j] == '^' {
                start_y = i;
                start_x = j;
                break;
            }
        }
    }

    let mut visited = HashSet::new();
    visited.insert((start_y, start_x));
    let mut queue = VecDeque::new();
    queue.push_back((start_y, start_x));
    let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)];
    let mut max_dist = 0;

    while let Some((y, x)) = queue.pop_front() {
        for &(dy, dx) in &dirs {
            let new_y = y as i32 + dy;
            let new_x = x as i32 + dx;
            if new_y >= 0 && new_y < n as i32 && new_x >= 0 && new_x < m as i32 {
                let new_y = new_y as usize;
                let new_x = new_x as usize;
                if grid[new_y][new_x] != '#' && !visited.contains(&(new_y, new_x)) {
                    visited.insert((new_y, new_x));
                    queue.push_back((new_y, new_x));
                    let dist = (new_y as i32 - start_y as i32).abs() + (new_x as i32 - start_x as i32).abs();
                    max_dist = max_dist.max(dist);
                }
            }
        }
    }

    println!("{}", max_dist);
}
