import * as fs from 'fs';

const grid = fs.readFileSync('input.txt', 'utf-8').trim().split('\n');
const N = grid.length;
const M = grid[0].length;
let startX = 0, startY = 0;

for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
        if (grid[i][j] === '^') {
            startY = i;
            startX = j;
            break;
        }
    }
}

const visited = new Set<string>();
visited.add(`${startY},${startX}`);
const queue: [number, number][] = [[startY, startX]];
const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
let maxDist = 0;

while (queue.length > 0) {
    const [y, x] = queue.shift()!;
    for (const [dy, dx] of dirs) {
        const newY = y + dy;
        const newX = x + dx;
        if (newY >= 0 && newY < N && newX >= 0 && newX < M && grid[newY][newX] !== '#') {
            const key = `${newY},${newX}`;
            if (!visited.has(key)) {
                visited.add(key);
                queue.push([newY, newX]);
                const dist = Math.abs(newY - startY) + Math.abs(newX - startX);
                maxDist = Math.max(maxDist, dist);
            }
        }
    }
}

console.log(maxDist);
