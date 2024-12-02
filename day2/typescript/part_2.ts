import * as fs from 'fs';

const isSafeReport = (report: number[]): boolean => {
    const differences = report.slice(1).map((num, i) => num - report[i]);
    const allIncreasing = differences.every(diff => diff >= 1 && diff <= 3);
    const allDecreasing = differences.every(diff => diff <= -1 && diff >= -3);
    return allIncreasing || allDecreasing;
};

const canBeMadeSafe = (report: number[]): boolean => {
    for (let i = 0; i < report.length; i++) {
        const modifiedReport = [...report.slice(0, i), ...report.slice(i + 1)];
        if (isSafeReport(modifiedReport)) {
            return true;
        }
    }
    return false;
};

const inputFile = "input.txt";

const fileContent = fs.readFileSync(inputFile, 'utf-8');
const lines = fileContent.trim().split('\n');

let safeCount = 0;

lines.forEach(line => {
    const report = line.split(' ').map(Number);
    if (isSafeReport(report) || canBeMadeSafe(report)) {
        safeCount++;
    }
});

console.log(safeCount);
