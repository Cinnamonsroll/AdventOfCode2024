input_file = "input.txt"

left_list = []
right_list = []

File.foreach(input_file) do |line|
  left, right = line.split.map(&:to_i)
  left_list << left
  right_list << right
end

right_counts = right_list.tally

similarity_score = left_list.sum { |num| num * (right_counts[num] || 0) }

puts similarity_score
