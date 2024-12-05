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
3
function sortUpdate(update: Update, rules: Rule[]): Update {
    const dependencies = new Map<number, Set<number>>();
    update.forEach(page => dependencies.set(page, new Set()));

    for (const [a, b] of rules) {
        if (dependencies.has(a) && dependencies.has(b)) {
            dependencies.get(b)!.add(a);
        }
    }

    const sortedUpdate: Update = [];
    const visited = new Set<number>();

    function dfs(page: number): void {
        if (visited.has(page)) return;
        visited.add(page);
        dependencies.get(page)!.forEach(dep => dfs(dep));
        sortedUpdate.push(page);
    }

    update.forEach(page => dfs(page));
    return sortedUpdate;
}

const [rules, updates] = parseInput('input.txt');
const total = updates
    .map(update => sortUpdate(update, rules))
    .reduce((sum, update) => sum + update[Math.floor(update.length / 2)], 0);

console.log(total);
