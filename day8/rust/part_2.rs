use std::collections::{HashMap, HashSet};
use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").unwrap();
    let grid: Vec<Vec<char>> = contents
        .lines()
        .filter(|line| !line.is_empty())
        .map(|line| line.chars().collect())
        .collect();

    let n = grid.len();
    let m = grid[0].len();
    let mut nodes: HashMap<char, Vec<(usize, usize)>> = HashMap::new();

    for i in 0..n {
        for j in 0..m {
            if grid[i][j] != '.' {
                nodes.entry(grid[i][j])
                    .or_insert_with(Vec::new)
                    .push((i, j));
            }
        }
    }

    let mut antinodes = HashSet::new();

    for node_list in nodes.values() {
        let l = node_list.len();
        for i in 0..l {
            for j in 0..i {
                let node1 = node_list[i];
                let node2 = node_list[j];
                for (pr1, pr2) in [(node1, node2), (node2, node1)] {
                    let (y1, x1) = pr1;
                    let (y2, x2) = pr2;
                    let dx = x2 as i32 - x1 as i32;
                    let dy = y2 as i32 - y1 as i32;
                    antinodes.insert((y2, x2));
                    let mut newx = x2 as i32 + dx;
                    let mut newy = y2 as i32 + dy;
                    while newx >= 0 && newx < m as i32 && newy >= 0 && newy < n as i32 {
                        antinodes.insert((newy as usize, newx as usize));
                        newx += dx;
                        newy += dy;
                    }
                }
            }
        }
    }

    println!("{}", antinodes.len());
}
