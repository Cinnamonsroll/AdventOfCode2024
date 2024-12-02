def is_safe_report(report)
    differences = report.each_cons(2).map { |a, b| b - a }
    all_increasing = differences.all? { |diff| diff.between?(1, 3) }
    all_decreasing = differences.all? { |diff| diff.between?(-3, -1) }
    all_increasing || all_decreasing
  end
  
  def can_be_made_safe(report)
    report.each_index do |i|
      modified_report = report[0...i] + report[i + 1..]
      return true if is_safe_report(modified_report)
    end
    false
  end
  
  input_file = "input.txt"
  
  safe_count = 0
  
  File.foreach(input_file) do |line|
    report = line.split.map(&:to_i)
    safe_count += 1 if is_safe_report(report) || can_be_made_safe(report)
  end
  
  puts safe_count
  