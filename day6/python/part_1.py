import sys
from typing import List, Tuple
from utils import read_lines


def get_start_position(grid: List[List[str]]) -> Tuple[int, int]:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '^':
                return y, x
    return None


def simulate_guard_path(grid: List[List[str]]) -> int:
    height = len(grid)
    width = len(grid[0])
    
    start_pos = get_start_position(grid)
    if not start_pos:
        return 0
    
    y, x = start_pos
    direction = 0  
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    visited = {(y, x)}
    
    while True:
        next_y = y + dy[direction]
        next_x = x + dx[direction]
        
        if not (0 <= next_y < height and 0 <= next_x < width):
            break
            
        if grid[next_y][next_x] == '#':
            direction = (direction + 1) % 4
        else:
            y, x = next_y, next_x
            visited.add((y, x))
            
    return len(visited)


grid = [list(line) for line in read_lines("input.txt")]
result = simulate_guard_path(grid)
print(result)