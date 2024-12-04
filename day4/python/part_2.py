def count_xmas(grid):
    ret = 0
    rows = len(grid)
    cols = len(grid[0])

    
    def check_xmas_x_shape(x, y):
        
        if grid[x][y] != "A":
            return False
        
        
        top_left = grid[x-1][y-1] + grid[x+1][y+1]  
        top_right = grid[x-1][y+1] + grid[x+1][y-1]  
        
        return top_left in {"MS", "SM"} and top_right in {"MS", "SM"}

    
    for x in range(1, rows-1):  
        for y in range(1, cols-1):  
            if check_xmas_x_shape(x, y):
                ret += 1
                
    return ret

grid = [list(line.strip()) for line in open("input.txt")]

print(count_xmas(grid))
