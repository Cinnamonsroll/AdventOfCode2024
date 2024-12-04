def count_xmas(grid)
  ret = 0

  def check_xmas_x_shape(grid, x, y)
    return false if grid[x][y] != 'A'

    top_left = grid[x-1][y-1] + grid[x+1][y+1]
    top_right = grid[x-1][y+1] + grid[x+1][y-1]

    (top_left == "MS" || top_left == "SM") &&
    (top_right == "MS" || top_right == "SM")
  end

  (1..grid.length-2).each do |x|
    (1..grid[0].length-2).each do |y|
      ret += 1 if check_xmas_x_shape(grid, x, y)
    end
  end

  ret
end

grid = File.readlines("input.txt").map(&:strip).map(&:chars)
puts count_xmas(grid)
