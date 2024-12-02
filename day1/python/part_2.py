from collections import Counter

input_file = "input.txt"

with open(input_file, 'r') as file:
    left_list = []
    right_list = []
    
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

right_counts = Counter(right_list)

similarity_score = 0
for num in left_list:
    similarity_score += num * right_counts[num]

print(similarity_score)
