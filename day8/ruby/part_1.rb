grid = File.readlines('input.txt').map(&:chomp).reject(&:empty?)
N, M = grid.size, grid[0].size
nodes = Hash.new { |h, k| h[k] = [] }

grid.each_with_index do |row, i|
  row.each_char.with_index do |c, j|
    nodes[c] << [i, j] if c != '.'
  end
end

antinodes = Set.new

nodes.each_value do |node_list|
  L = node_list.size
  L.times do |i|
    i.times do |j|
      node1, node2 = node_list[i], node_list[j]
      [[node1, node2], [node2, node1]].each do |pr1, pr2|
        x1, y1 = pr1[1], pr1[0]
        x2, y2 = pr2[1], pr2[0]
        newx = x2 + (x2 - x1)
        newy = y2 + (y2 - y1)
        antinodes << [newx, newy] if newx >= 0 && newx < M && newy >= 0 && newy < N
      end
    end
  end
end

puts antinodes.size
