import * as fs from 'fs';

type Direction = [number, number];

function countXmas(grid: string[][]): number {
    const word = "XMAS";
    const directions: Direction[] = [
        [-1, 0], [1, 0], [0, -1], [0, 1], 
        [-1, -1], [-1, 1], [1, -1], [1, 1]
    ];
    const rows = grid.length;
    const cols = grid[0].length;
    let count = 0;

    function valid(r: number, c: number, dr: number, dc: number): boolean {
        for (let i = 0; i < word.length; i++) {
            const nr = r + dr * i;
            const nc = c + dc * i;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] !== word[i]) {
                return false;
            }
        }
        return true;
    }

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            for (const [dr, dc] of directions) {
                if (valid(r, c, dr, dc)) {
                    count++;
                }
            }
        }
    }

    return count;
}

const grid: string[][] = fs.readFileSync('input.txt', 'utf-8')
    .split('\n')
    .map(line => line.split(''));

console.log(countXmas(grid)); 
