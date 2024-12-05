from typing import List, Tuple
from utils import read_lines


def parse_input(file_path: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    lines = read_lines(file_path)
    rules = []
    updates = []
    section = 0
    for line in lines:
        if not line.strip():
            section += 1
            continue
        if section == 0:
            rules.append(tuple(map(int, line.split('|'))))
        else:
            updates.append(list(map(int, line.split(','))))
    return rules, updates


def is_update_ordered(update: List[int], rules: List[Tuple[int, int]]) -> bool:
    page_indices = {page: i for i, page in enumerate(update)}
    for a, b in rules:
        if a in page_indices and b in page_indices:
            if page_indices[a] > page_indices[b]:
                return False
    return True


rules, updates = parse_input("input.txt")
middle_sum = sum(
    update[len(update) // 2] 
    for update in updates 
    if is_update_ordered(update, rules)
)
print(middle_sum)
