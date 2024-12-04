from utils import read_lines
lines = read_lines("input.txt")

left_list = []
right_list = []


for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)


left_list.sort()
right_list.sort()


total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))


print(total_distance)
