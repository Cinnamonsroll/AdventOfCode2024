grid = File.readlines('input.txt').map(&:chomp)
N, M = grid.size, grid[0].size
start_x = start_y = 0

grid.each_with_index do |row, i|
  row.each_char.with_index do |cell, j|
    if cell == '^'
      start_y, start_x = i, j
      break
    end
  end
end

visited = {[start_y, start_x] => true}
queue = [[start_y, start_x]]
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

until queue.empty?
  y, x = queue.shift
  dirs.each do |dy, dx|
    new_y, new_x = y + dy, x + dx
    if new_y >= 0 && new_y < N && new_x >= 0 && new_x < M && grid[new_y][new_x] != '#'
      unless visited[[new_y, new_x]]
        visited[[new_y, new_x]] = true
        queue << [new_y, new_x]
      end
    end
  end
end

puts visited.size
