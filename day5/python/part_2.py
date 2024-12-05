from typing import List, Tuple, Set, Dict
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


def sort_update(update: List[int], rules: List[Tuple[int, int]]) -> List[int]:
    dependencies = {page: set() for page in update}
    for a, b in rules:
        if a in dependencies and b in dependencies:
            dependencies[b].add(a)

    sorted_update = []
    visited = set()

    def dfs(page: int) -> None:
        if page in visited:
            return
        visited.add(page)
        for dep in dependencies[page]:
            dfs(dep)
        sorted_update.append(page)

    for page in update:
        dfs(page)

    return sorted_update


rules, updates = parse_input("input.txt")
total = sum(
    sorted_update[len(sorted_update) // 2]
    for update in updates
    if (sorted_update := sort_update(update, rules))
)
print(total)
