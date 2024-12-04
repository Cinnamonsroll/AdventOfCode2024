from typing import List
from utils import Grid, read_lines
def count_xmas(grid: List[List[str]]) -> int:
    ret = 0
    grid_obj = Grid(grid)  
    
    def check_xmas_x_shape(x: int, y: int) -> bool:
        if grid_obj.get(x, y) != "A":
            return False
        
        
        top_left = grid_obj.get(x-1, y-1) + grid_obj.get(x+1, y+1)
        top_right = grid_obj.get(x-1, y+1) + grid_obj.get(x+1, y-1)
        
        return top_left in {"MS", "SM"} and top_right in {"MS", "SM"}

    
    for x in range(1, grid_obj.rows-1):  
        for y in range(1, grid_obj.cols-1):  
            if check_xmas_x_shape(x, y):
                ret += 1
                
    return ret


grid = [list(line.strip()) for line in read_lines("input.txt")]
print(count_xmas(grid))
