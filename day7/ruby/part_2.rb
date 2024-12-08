total = 0

File.foreach('input.txt') do |line|
  test_value, nums = line.split(':')
  test_value = test_value.to_i
  numbers = nums.split.map(&:to_i)
  
  ops_count = numbers.size - 1
  found = false
  (0...4**ops_count).each do |i|
    break if found
    result = numbers[0]
    valid = true
    ops_count.times do |j|
      op = (i >> (2 * j)) & 3
      case op
      when 0
        result += numbers[j + 1]
      when 1
        result -= numbers[j + 1]
      when 2
        result *= numbers[j + 1]
      when 3
        if numbers[j + 1] == 0 || result % numbers[j + 1] != 0
          valid = false
          break
        end
        result /= numbers[j + 1]
      end
    end
    if valid && result == test_value
      total += test_value
      found = true
    end
  end
end

puts total
