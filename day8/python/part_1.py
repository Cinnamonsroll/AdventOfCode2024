grid = [line.strip() for line in open('input.txt') if line.strip()]
N, M = len(grid), len(grid[0])
nodes = {}
antinodes = set()

for i in range(N):
    for j in range(M):
        if grid[i][j] != '.':
            nodes[grid[i][j]] = nodes.get(grid[i][j], []) + [(i,j)]

for k in nodes:
    node_list = nodes[k]
    L = len(node_list)
    for i in range(L):
        for j in range(i):
            node1, node2 = node_list[i], node_list[j]
            x1, y1 = node1
            x2, y2 = node2
            newx, newy = x2 + (x2 - x1), y2 + (y2 - y1)
            if 0 <= newx < N and 0 <= newy < M:
                antinodes.add((newx,newy))
            x1, y1 = node2
            x2, y2 = node1
            newx, newy = x2 + (x2 - x1), y2 + (y2 - y1)
            if 0 <= newx < N and 0 <= newy < M:
                antinodes.add((newx,newy))

print(len(antinodes))