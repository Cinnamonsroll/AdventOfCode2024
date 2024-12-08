import * as fs from 'fs';

const input = fs.readFileSync('input.txt', 'utf-8').trim().split('\n');
let total = 0;

for (const line of input) {
    const [testValue, nums] = line.split(':');
    const numbers = nums.trim().split(/\s+/).map(Number);
    const opsCount = numbers.length - 1;
    let found = false;

    for (let i = 0; i < (1 << opsCount) && !found; i++) {
        let result = numbers[0];
        for (let j = 0; j < opsCount; j++) {
            if (((i >> j) & 1) === 0) {
                result += numbers[j + 1];
            } else {
                result *= numbers[j + 1];
            }
        }
        if (result === Number(testValue)) {
            total += Number(testValue);
            found = true;
        }
    }
}

console.log(total);
