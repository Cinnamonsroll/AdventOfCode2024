def count_xmas(grid)
  word = "XMAS"
  directions = [
    [-1, 0], [1, 0], [0, -1], [0, 1],
    [-1, -1], [-1, 1], [1, -1], [1, 1]
  ]
  count = 0

  def valid(grid, r, c, dr, dc, word)
    word.each_char.with_index do |ch, i|
      nr = r + dr * i
      nc = c + dc * i
      return false if nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length
      return false if grid[nr][nc] != ch
    end
    true
  end

  grid.each_with_index do |row, r|
    row.each_with_index do |_, c|
      directions.each do |dr, dc|
        count += 1 if valid(grid, r, c, dr, dc, word)
      end
    end
  end

  count
end

grid = File.readlines("input.txt").map(&:strip).map(&:chars)
puts count_xmas(grid)
