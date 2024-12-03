memory = File.read('input.txt')
regex = /mul\((\d+),(\d+)\)/
result = 0
memory.scan(regex) do |x, y|
  result += x.to_i * y.to_i
end

puts result
