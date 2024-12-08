total = 0
for line in open('input.txt'):
    test_value = int(line.split(':')[0])
    numbers = [int(x) for x in line.split(':')[1].strip().split()]
    ops_count = len(numbers) - 1
    
    for i in range(4 ** ops_count):
        ops = []
        temp = i
        for _ in range(ops_count):
            ops.append(['+', '-', '*', '/'][temp % 4])
            temp //= 4
            
        try:
            result = numbers[0]
            for idx, op in enumerate(ops):
                if op == '+': result += numbers[idx + 1]
                elif op == '-': result -= numbers[idx + 1]
                elif op == '*': result *= numbers[idx + 1]
                elif op == '/': 
                    if numbers[idx + 1] == 0 or result % numbers[idx + 1] != 0: raise ValueError
                    result //= numbers[idx + 1]
            
            if result == test_value:
                total += test_value
                break
        except:
            continue

print(total)