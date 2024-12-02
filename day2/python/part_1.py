def is_safe_report(report):
    differences = [report[i] - report[i - 1] for i in range(1, len(report))]
    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)
    return all_increasing or all_decreasing

input_file = "input.txt"

safe_count = 0

with open(input_file, 'r') as file:
    for line in file:
        report = list(map(int, line.split()))
        if is_safe_report(report):
            safe_count += 1

print(safe_count)
