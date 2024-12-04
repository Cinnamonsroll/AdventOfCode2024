import re
import math
from typing import List, Tuple, Dict, Any, Callable
from collections import Counter

class Grid:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0

    def get(self, x: int, y: int) -> int:
        """Fetches the value from the grid at coordinates (x, y), returns None if out of bounds."""
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return self.grid[x][y]
        return None

    def set(self, x: int, y: int, value: int):
        """Sets the value at the coordinates (x, y)."""
        if 0 <= x < self.rows and 0 <= y < self.cols:
            self.grid[x][y] = value

    def get_neighbors(self, x: int, y: int, diagonals: bool = False) -> List[Tuple[int, int]]:
        """Returns neighboring coordinates for (x, y), optionally including diagonals."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        if diagonals:
            directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                neighbors.append((nx, ny))
        return neighbors

    def __str__(self) -> str:
        """Returns a string representation of the grid for easier debugging."""
        return "\n".join("".join(map(str, row)) for row in self.grid)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def neighbors(self, diagonals=False) -> List['Point']:
        """Generates the 4 or 8 neighboring points for this point."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        if diagonals:
            directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

        neighbors = [Point(self.x + dx, self.y + dy) for dx, dy in directions]
        return neighbors

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)


class Pathfinding:
    @staticmethod
    def bfs(start: Point, goal: Point, grid: Grid) -> List[Point]:
        """Breadth-First Search to find the shortest path in a grid."""
        from collections import deque

        queue = deque([start])
        visited = set([start])
        parent_map = {start: None}

        while queue:
            current = queue.popleft()
            if current == goal:
                break

            for neighbor in current.neighbors():
                if grid.get(neighbor.x, neighbor.y) == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent_map[neighbor] = current

        
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = parent_map[current]
        return path[::-1]  
    
class Graph:
    def __init__(self, edges: List[Tuple[int, int]]):
        """Initialize a graph from a list of edges."""
        self.graph = {}
        for u, v in edges:
            if u not in self.graph:
                self.graph[u] = []
            if v not in self.graph:
                self.graph[v] = []
            self.graph[u].append(v)
            self.graph[v].append(u)

    def bfs(self, start: int, goal: int) -> List[int]:
        """Breadth-First Search to find the shortest path in an unweighted graph."""
        from collections import deque

        queue = deque([start])
        visited = {start}
        parent_map = {start: None}

        while queue:
            current = queue.popleft()
            if current == goal:
                break

            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent_map[neighbor] = current

        
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = parent_map[current]
        return path[::-1]  

    def __repr__(self):
        return f"Graph({self.graph})"


def read_lines(filename: str) -> List[str]:
    """Reads all lines from a file and returns them as a list of strings."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def read_ints(filename: str) -> List[int]:
    """Reads all integers found in a file and returns them as a list."""
    return [int(x) for x in re.findall(r'-?\d+', open(filename).read())]

def read_floats(filename: str) -> List[float]:
    """Reads all floating point numbers found in a file and returns them as a list."""
    return [float(x) for x in re.findall(r'-?\d+\.\d+', open(filename).read())]


def find_all_matches(text: str, pattern: str) -> List[str]:
    """Finds all matches for a given regex pattern in a string."""
    return re.findall(pattern, text)

def split_chunks(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """Splits a list into chunks of specified size."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome."""
    return s == s[::-1]


def gcd(a: int, b: int) -> int:
    """Returns the greatest common divisor of a and b."""
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    """Returns the least common multiple of a and b."""
    return abs(a * b) // math.gcd(a, b)

def mod_exp(base: int, exp: int, mod: int) -> int:
    """Calculates (base ^ exp) % mod efficiently."""
    return pow(base, exp, mod)

def factorial(n: int) -> int:
    """Returns the factorial of n."""
    return math.factorial(n)


def count_frequency(items: List[Any]) -> Dict[Any, int]:
    """Returns a dictionary with the frequency of each item in the list."""
    return dict(Counter(items))

def most_common(items: List[Any]) -> Any:
    """Returns the most common item in a list."""
    return Counter(items).most_common(1)[0][0]

def least_common(items: List[Any]) -> Any:
    """Returns the least common item in a list."""
    return Counter(items).most_common()[-1][0]


def permutations(lst: List[Any], r: int) -> List[List[Any]]:
    """Generates all permutations of length r from the list."""
    from itertools import permutations
    return [list(p) for p in permutations(lst, r)]

def combinations(lst: List[Any], r: int) -> List[List[Any]]:
    """Generates all combinations of length r from the list."""
    from itertools import combinations
    return [list(c) for c in combinations(lst, r)]


def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """Calculates the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """Calculates the Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def run_function_repeatedly(fn: Callable, n: int) -> Any:
    """Runs a function n times and returns the result of the nth run."""
    result = None
    for _ in range(n):
        result = fn()
    return result

def find_unique_elements(lst: List[Any]) -> List[Any]:
    """Returns the unique elements in a list."""
    return list(set(lst))

def flatten_list(nested_lst: List[List[Any]]) -> List[Any]:
    """Flattens a nested list into a single list."""
    return [item for sublist in nested_lst for item in sublist]


def transpose_grid(grid: List[List[Any]]) -> List[List[Any]]:
    """Transposes a 2D grid (list of lists)."""
    return list(map(list, zip(*grid)))

def rotate_grid(grid: List[List[Any]], clockwise: bool = True) -> List[List[Any]]:
    """Rotates a 2D grid 90 degrees clockwise or counterclockwise."""
    if clockwise:
        return list(map(list, zip(*grid[::-1])))
    else:
        return list(map(list, zip(*grid)))[::-1]

def flood_fill(grid: List[List[Any]], start: Tuple[int, int], target: Any, replacement: Any) -> None:
    """
    Performs a flood fill on the grid, replacing all connected target values with replacement value.
    Modifies the grid in place.
    """
    if not grid or target == replacement:
        return

    rows, cols = len(grid), len(grid[0])
    r, c = start

    if grid[r][c] != target:
        return

    def fill(r: int, c: int):
        if (0 <= r < rows and 0 <= c < cols and 
            grid[r][c] == target):
            grid[r][c] = replacement
            fill(r+1, c)
            fill(r-1, c)
            fill(r, c+1)
            fill(r, c-1)

    fill(r, c)

def binary_search(arr: List[Any], target: Any) -> int:
    """
    Performs binary search on a sorted list.
    Returns index if found, -1 if not found.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def sliding_window(sequence: List[Any], window_size: int) -> List[List[Any]]:
    """Returns a list of all possible contiguous windows of given size from the sequence."""
    if len(sequence) < window_size:
        return []
    return [sequence[i:i+window_size] for i in range(len(sequence)-window_size+1)]

def find_cycle(sequence: List[Any]) -> Tuple[int, int]:
    """
    Finds a cycle in a sequence using Floyd's Tortoise and Hare algorithm.
    Returns (start_index, cycle_length) or (-1, -1) if no cycle found.
    """
    if not sequence:
        return (-1, -1)

    
    next_elem = {i: sequence[i] for i in range(len(sequence))}
    
    
    tortoise = 0
    hare = 0
    
    
    while True:
        tortoise = next_elem.get(tortoise, -1)
        hare = next_elem.get(next_elem.get(hare, -1), -1)
        
        if tortoise == -1 or hare == -1:
            return (-1, -1)
        if tortoise == hare:
            break
    
    
    tortoise = 0
    while tortoise != hare:
        tortoise = next_elem[tortoise]
        hare = next_elem[hare]
    
    
    cycle_length = 1
    hare = next_elem[tortoise]
    while hare != tortoise:
        hare = next_elem[hare]
        cycle_length += 1
    
    return (tortoise, cycle_length)

def memoize(func: Callable) -> Callable:
    """Decorator to memoize function results."""
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def parse_grid(input_str: str) -> List[List[str]]:
    """Parses a string representation of a grid into a 2D list."""
    return [list(line.strip()) for line in input_str.strip().split('\n')]

def find_all_paths(graph: Dict[Any, List[Any]], start: Any, end: Any, 
                   visited: set = None) -> List[List[Any]]:
    """
    Finds all possible paths from start to end in a graph.
    Graph should be represented as a dictionary of node -> list of neighbors.
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    paths = []
    
    if start == end:
        paths.append([start])
    else:
        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                for path in find_all_paths(graph, neighbor, end, visited.copy()):
                    paths.append([start] + path)
    
    return paths

def count_if(sequence: List[Any], predicate: Callable[[Any], bool]) -> int:
    """Counts elements in sequence that satisfy the predicate function."""
    return sum(1 for item in sequence if predicate(item))

def group_by(items: List[Any], key_func: Callable[[Any], Any]) -> Dict[Any, List[Any]]:
    """Groups items by a key function."""
    result = {}
    for item in items:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result
