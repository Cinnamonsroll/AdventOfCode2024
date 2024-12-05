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

def sort_update(update, rules)
  dependencies = update.each_with_object({}) { |page, hash| hash[page] = Set.new }

  rules.each do |a, b|
    if dependencies.key?(a) && dependencies.key?(b)
      dependencies[b].add(a)
    end
  end

  sorted_update = []
  visited = Set.new

  def dfs(page, visited, dependencies, sorted_update)
    return if visited.include?(page)
    visited.add(page)
    dependencies[page].each { |dep| dfs(dep, visited, dependencies, sorted_update) }
    sorted_update << page
  end

  update.each { |page| dfs(page, visited, dependencies, sorted_update) }
  sorted_update
end

rules, updates = parse_input('input.txt')
total = updates
  .map { |update| sort_update(update, rules) }
  .sum { |update| update[update.length / 2] }

puts total
