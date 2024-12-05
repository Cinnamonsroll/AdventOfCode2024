print(sum(left * sum(1 for r in [int(line.split()[1]) for line in open('input.txt')] if r == left) for left in [int(line.split()[0]) for line in open('input.txt')]))
