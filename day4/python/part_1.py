from typing import List
from utils import Grid, read_lines


def count_xmas(grid: List[List[str]]) -> int:
    word = "XMAS"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    grid_obj = Grid(grid)  
    count = 0

    def valid(r: int, c: int, dr: int, dc: int) -> bool:
        for i in range(len(word)):
            nr, nc = r + dr * i, c + dc * i
            if grid_obj.get(nr, nc) != word[i]:
                return False
        return True

    for r in range(grid_obj.rows):
        for c in range(grid_obj.cols):
            for dr, dc in directions:
                if valid(r, c, dr, dc):
                    count += 1
    return count



grid = [list(line.strip()) for line in read_lines("input.txt")]
print(count_xmas(grid))
