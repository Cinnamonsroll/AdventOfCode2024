def parse_input(file_path)
  lines = File.readlines(file_path).map(&:strip)
  rules = []
  updates = []
  section = 0

  lines.each do |line|
    if line.empty?
      section += 1
      next
    end
    if section == 0
      rules << line.split('|').map(&:to_i)
    else
      updates << line.split(',').map(&:to_i)
    end
  end

  [rules, updates]
end

def is_update_ordered(update, rules)
  page_indices = update.each_with_index.to_h

  rules.each do |a, b|
    if page_indices.key?(a) && page_indices.key?(b)
      return false if page_indices[a] > page_indices[b]
    end
  end
  true
end

rules, updates = parse_input('input.txt')
middle_sum = updates
  .select { |update| is_update_ordered(update, rules) }
  .sum { |update| update[update.length / 2] }

puts middle_sum
