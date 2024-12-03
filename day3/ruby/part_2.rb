memory = File.read('input.txt')
regex = /mul\((\d+),(\d+)\)|do\(\)|don't\(\)/
result = 0
enabled = true


memory.scan(regex) do |match|
  if match[0] == 'do()'
    enabled = true
  elsif match[0] == "don't()"
    enabled = false
  elsif enabled && match[0].start_with?('mul')
    x, y = match[0].match(/\d+/g).map(&:to_i)
    result += x * y
  end
end

puts result
