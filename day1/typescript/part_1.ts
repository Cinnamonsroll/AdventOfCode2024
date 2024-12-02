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

leftList.sort((a, b) => a - b);
rightList.sort((a, b) => a - b);

const totalDistance = leftList.reduce((sum, left, i) => sum + Math.abs(left - rightList[i]), 0);

console.log(totalDistance);
