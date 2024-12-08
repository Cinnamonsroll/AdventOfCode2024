total = 0

File.foreach('input.txt') do |line|
  test_value, nums = line.split(':')
  test_value = test_value.to_i
  numbers = nums.split.map(&:to_i)
  
  ops_count = numbers.size - 1
  found = false
  (0...2**ops_count).each do |i|
    break if found
    result = numbers[0]
    ops_count.times do |j|
      if (i >> j) & 1 == 0
        result += numbers[j + 1]
      else
        result *= numbers[j + 1]
      end
    end
    if result == test_value
      total += test_value
      found = true
    end
  end
end

puts total
