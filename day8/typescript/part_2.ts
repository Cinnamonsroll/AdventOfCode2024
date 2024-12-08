import * as fs from 'fs';

const grid = fs.readFileSync('input.txt', 'utf-8')
    .trim()
    .split('\n')
    .filter(line => line.length > 0);

const N = grid.length;
const M = grid[0].length;
const nodes = new Map<string, Array<[number, number]>>();

for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
        if (grid[i][j] !== '.') {
            if (!nodes.has(grid[i][j])) {
                nodes.set(grid[i][j], []);
            }
            nodes.get(grid[i][j])!.push([i, j]);
        }
    }
}

const antinodes = new Set<string>();

for (const nodeList of nodes.values()) {
    const L = nodeList.length;
    for (let i = 0; i < L; i++) {
        for (let j = 0; j < i; j++) {
            const node1 = nodeList[i];
            const node2 = nodeList[j];
            for (const [pr1, pr2] of [[node1, node2], [node2, node1]]) {
                const [y1, x1] = pr1;
                const [y2, x2] = pr2;
                const dx = x2 - x1;
                const dy = y2 - y1;
                antinodes.add(`${y2},${x2}`);
                let newX = x2 + dx;
                let newY = y2 + dy;
                while (newX >= 0 && newX < M && newY >= 0 && newY < N) {
                    antinodes.add(`${newY},${newX}`);
                    newX += dx;
                    newY += dy;
                }
            }
        }
    }
}

console.log(antinodes.size);
