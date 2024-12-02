import * as fs from 'fs';

const inputFile = "input.txt";

const fileContent = fs.readFileSync(inputFile, 'utf-8');
const lines = fileContent.trim().split('\n');

const leftList: number[] = [];
const rightList: number[] = [];

lines.forEach(line => {
    const [left, right] = line.split(' ').map(Number);
    leftList.push(left);
    rightList.push(right);
});

const rightCounts: Record<number, number> = {};
rightList.forEach(num => {
    rightCounts[num] = (rightCounts[num] || 0) + 1;
});

let similarityScore = 0;
leftList.forEach(num => {
    similarityScore += num * (rightCounts[num] || 0);
});

console.log(similarityScore);
