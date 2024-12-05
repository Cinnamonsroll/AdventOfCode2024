import * as fs from 'fs';

type Rule = [number, number];
type Update = number[];

function parseInput(filePath: string): [Rule[], Update[]] {
    const lines = fs.readFileSync(filePath, 'utf-8').trim().split('\n');
    const rules: Rule[] = [];
    const updates: Update[] = [];
    let section = 0;

    for (const line of lines) {
        if (!line.trim()) {
            section++;
            continue;
        }
        if (section === 0) {
            rules.push(line.split('|').map(Number) as Rule);
        } else {
            updates.push(line.split(',').map(Number));
        }
    }

    return [rules, updates];
}

function isUpdateOrdered(update: Update, rules: Rule[]): boolean {
    const pageIndices = new Map(update.map((page, i) => [page, i]));

    for (const [a, b] of rules) {
        if (pageIndices.has(a) && pageIndices.has(b)) {
            if (pageIndices.get(a)! > pageIndices.get(b)!) {
                return false;
            }
        }
    }
    return true;
}

const [rules, updates] = parseInput('input.txt');
const middleSum = updates
    .filter(update => isUpdateOrdered(update, rules))
    .reduce((sum, update) => sum + update[Math.floor(update.length / 2)], 0);

console.log(middleSum);
