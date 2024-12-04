def count_xmas(grid):
    word = "XMAS"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    rows, cols = len(grid), len(grid[0])
    count = 0

    def valid(r, c, dr, dc):
        for i in range(len(word)):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == word[i]):
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if valid(r, c, dr, dc):
                    count += 1
    return count

grid = [list(line.strip()) for line in open("input.txt")]
print(count_xmas(grid))
