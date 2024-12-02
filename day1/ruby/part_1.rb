input_file = "input.txt"

left_list = []
right_list = []

File.foreach(input_file) do |line|
  left, right = line.split.map(&:to_i)
  left_list << left
  right_list << right
end

left_list.sort!
right_list.sort!

total_distance = left_list.each_with_index.sum { |left, i| (left - right_list[i]).abs }

puts total_distance
