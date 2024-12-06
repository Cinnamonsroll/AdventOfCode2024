import sys
from typing import List, Tuple, Set
from utils import read_lines


def get_start_position(grid: List[List[str]]) -> Tuple[int, int]:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '^':
                return y, x
    return None


def simulate_guard_path(grid: List[List[str]], obstacle_y: int, obstacle_x: int, 
                       height: int, width: int, start_pos: Tuple[int, int],
                       obstacles: Set[Tuple[int, int]]) -> bool:
    y, x = start_pos
    direction = 0  
    
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    
    seen = set()
    steps = 0
    max_steps = height * width * 4  
    
    while steps < max_steps:
        
        next_y = y + dy[direction]
        next_x = x + dx[direction]
        
        
        if (not (0 <= next_y < height and 0 <= next_x < width) or
            (next_y, next_x) in obstacles or
            (next_y == obstacle_y and next_x == obstacle_x)):
            
            
            state = (y, x, direction)
            if state in seen:
                return True
            seen.add(state)
            
            direction = (direction + 1) % 4
        else:
            y, x = next_y, next_x
        
        steps += 1
    
    return False


def find_loop_positions(grid: List[List[str]]) -> int:
    height = len(grid)
    width = len(grid[0])
    start_pos = get_start_position(grid)
    if not start_pos:
        return 0
    
    
    obstacles = {(y, x) for y in range(height) for x in range(width) 
                if grid[y][x] == '#'}
    
    loop_count = 0
    
    
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '#' or (y, x) == start_pos:
                continue
            
            if simulate_guard_path(grid, y, x, height, width, start_pos, obstacles):
                loop_count += 1
    
    return loop_count


grid = [list(line) for line in read_lines("input.txt")]
result = find_loop_positions(grid)
print(result)