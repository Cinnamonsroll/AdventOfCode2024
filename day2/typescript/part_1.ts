import * as fs from 'fs';

const isSafeReport = (report: number[]): boolean => {
    const differences = report.slice(1).map((num, i) => num - report[i]);
    const allIncreasing = differences.every(diff => diff >= 1 && diff <= 3);
    const allDecreasing = differences.every(diff => diff <= -1 && diff >= -3);
    return allIncreasing || allDecreasing;
};

const inputFile = "input.txt";

const fileContent = fs.readFileSync(inputFile, 'utf-8');
const lines = fileContent.trim().split('\n');

let safeCount = 0;

lines.forEach(line => {
    const report = line.split(' ').map(Number);
    if (isSafeReport(report)) {
        safeCount++;
    }
});

console.log(safeCount);
