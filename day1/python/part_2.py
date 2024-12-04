from utils import read_lines, count_frequency
lines = read_lines("input.txt")
left_list = []
right_list = []
for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)
right_counts = count_frequency(right_list)
similarity_score = sum(left * right_counts.get(left, 0) for left in left_list)


print(similarity_score)
