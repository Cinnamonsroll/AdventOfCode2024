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
            for node1, node2 in [(node_list[i], node_list[j]), (node_list[j], node_list[i])]:
                x1, y1 = node1
                x2, y2 = node2
                newx, newy = x2 + (x2 - x1), y2 + (y2 - y1)
                antinodes.add((x2,y2))
                while 0 <= newx < N and 0 <= newy < M:
                    antinodes.add((newx,newy))
                    newx += (x2 - x1)
                    newy += (y2 - y1)

print(len(antinodes))