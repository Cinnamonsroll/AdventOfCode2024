total = 0
for line in open('input.txt'):
    test_value = int(line.split(':')[0])
    numbers = [int(x) for x in line.split(':')[1].strip().split()]
    ops_count = len(numbers) - 1
    
    for i in range(2 ** ops_count):
        ops = ['+' if (i >> j) & 1 == 0 else '*' for j in range(ops_count)]
        result = numbers[0]
        for idx, op in enumerate(ops):
            result = result + numbers[idx + 1] if op == '+' else result * numbers[idx + 1]
        if result == test_value:
            total += test_value
            break

print(total)